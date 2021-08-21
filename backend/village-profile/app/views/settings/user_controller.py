from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from app.models.settings.office import Office
from app.templatetags.role_check import is_super_admin, is_admin

from app.models.settings.designation import Designation
from app.models.settings.district import District
from app.models.settings.local_level import LocalLevel
from app.models.settings.profile import Profile
from app.models.settings.province import Province


@user_passes_test(is_admin)
def create_user(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        provinces = Province.objects.all()
        districts = District.objects.all()
        local_levels = LocalLevel.objects.all()
        designations = Designation.objects.all()
        offices = Office.objects.all()
        return render(request, 'app/backend/user/create.html',
                      {'groups': groups, 'provinces': provinces, 'designations': designations, 'districts': districts,
                       'local_levels': local_levels, 'offices': offices})
    # try:

    data = request.POST
    office = Office.objects.get(pk=data['office'])
    if office:
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            is_superuser=0,
            is_staff=0,
            is_active=1,
            date_joined=datetime.now()
        )
        user.groups.add(data['role'])
        user.set_password(data['password'])
        user.save()

        Profile.objects.create(
            user=user,
            designation_id=data['designation'],
            local_level=office.local_level,
            district=office.district,
            province=office.province,
            office=office,
            status=1,
            created_by=request.user.id
        )
        messages.success(request, 'User added successfully!')
        return redirect('create_user')
    messages.error(request, 'Can not create User. Check your inputs.')
    return redirect('create_user')
    # except Exception as e:
    #     messages.error(request, 'Can not create User. Check your inputs.')
    #     return redirect('list_user')


@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.user == user:
        messages.error(request, 'Can not edit self as other user.')
        return redirect('list_user')

    try:

        data = request.POST
        if data['username'] != user.username:
            user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.groups.clear()
        user.groups.add(data['role'])
        user.save()

        profile = user.profile

        profile.group_id = data['role']
        profile.save()

        messages.success(request, 'User updated successfully!')
        return redirect('list_user')
    except Exception as e:
        messages.error(request, 'Can not update User.')
        return redirect('edit_user', user_id)


@user_passes_test(is_admin)
def list_user(request):
    profiles = Profile.objects.filter(status=1)
    return render(request, 'app/backend/user/list.html', {'profiles': profiles})


@user_passes_test(is_super_admin)
def delete_user(request, user_id):
    try:
        obj = User.objects.get(id=user_id)
        if request.user != obj:
            messages.success(request, 'User deleted successfully!')
            # obj.is_active = 0
            # obj.save()
            obj.delete()
        else:
            messages.error(request, "Don't delete yourself!")
        # obj.delete()
        return redirect('list_user')
    except Exception as e:
        messages.error(request, 'Can not delete User')
        return redirect('list_user')
