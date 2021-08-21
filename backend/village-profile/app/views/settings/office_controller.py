from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.office_form import OfficeForm
from app.services.settings.localLevelService import get_all_local_levels
from app.services.settings.officeService import get_all_office, add_new_office
from app.services.settings.provinceService import get_all_province
from app.services.settings.discrictService import get_all_district


@login_required
def list_office(request):
    offices = get_all_office()  # All database related logic are in Service
    return render(request, 'app/backend/settings/office/index.html', {'offices': offices})


@login_required
def create_office(request):
    # For get request
    provinces = get_all_province()
    districts = get_all_district()
    local_levels = get_all_local_levels()
    if request.method == 'GET':
        return render(request, 'app/backend/settings/office/create.html',
                      {'provinces': provinces, 'districts': districts, 'local_levels': local_levels})

    # For post request
    form = OfficeForm(request.POST)  # CaptionForm is a form class using to validate form inputs
    if form.is_valid():
        try:
            office = add_new_office(request)  # From caption, all

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [office])  # Convert single model to json before response
                return JsonResponse(data, safe=False)

            messages.success(request, 'Local level created successfully!')
            return redirect('office')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Local Level')
            return redirect('office')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/office/create.html', {'form': form})
