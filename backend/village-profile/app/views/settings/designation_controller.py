from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.designation_form import DesignationForm
from app.services.settings.designationService import get_all_designation, add_new_designation


@login_required
def list_designation(request):
    designations = get_all_designation()  # All database related logic are in Service
    return render(request, 'app/backend/settings/designation/index.html', {'designations': designations})


@login_required
def create_designation(request):
    # For get request
    if request.method == 'GET':
        return render(request, 'app/backend/settings/designation/create.html')

    # For post request
    form = DesignationForm(request.POST)  # CaptionForm is a form class using to validate form inputs
    if form.is_valid():
        try:
            designation = add_new_designation(request)  # From caption, all

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [designation])  # Convert single model to json before response
                return JsonResponse(data, safe=False)

            messages.success(request, 'Designation created successfully!')
            return redirect('designation')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Position')
            return redirect('designation')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/designation/create.html', {'form': form})
