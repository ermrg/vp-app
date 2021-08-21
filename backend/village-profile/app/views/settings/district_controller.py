from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.district_form import DistrictForm
from app.services.settings.discrictService import get_all_district, add_new_district
from app.services.settings.provinceService import get_all_province


@login_required
def list_district(request):
    districts = get_all_district()  # All database related logic are in Service
    return render(request, 'app/backend/settings/district/index.html', {'districts': districts})


@login_required
def create_district(request):
    provinces = get_all_province()
    # For get request
    if request.method == 'GET':
        return render(request, 'app/backend/settings/district/create.html', {'provinces': provinces})

    # For post request
    form = DistrictForm(request.POST)  # CaptionForm is a form class using to validate form inputs
    if form.is_valid():
        try:
            district = add_new_district(request)  # From caption, all

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [district])  # Convert single model to json before response
                return JsonResponse(data, safe=False)

            messages.success(request, 'District created successfully!')
            return redirect('district')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create District')
            return redirect('district')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/district/create.html', {'form': form})
