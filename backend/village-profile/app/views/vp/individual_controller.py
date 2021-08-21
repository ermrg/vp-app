from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.vp.individual_form import IndividualForm
from app.services.settings.localLevelService import get_all_local_levels
from app.services.settings.provinceService import get_all_province
from app.services.settings.discrictService import get_all_district
from app.services.vp.indivisualService import get_all_individual, add_new_individual


@login_required
def list_individual(request):
    individuals = get_all_individual(request)  # All database related logic are in Service
    return render(request, 'app/backend/vp/individual/index.html', {'individuals': individuals})


@login_required
def create_individual(request):
    # For get request
    provinces = get_all_province()
    districts = get_all_district()
    local_levels = get_all_local_levels()
    if request.method == 'GET':
        return render(request, 'app/backend/vp/individual/create.html',
                      {'provinces': provinces, 'districts': districts, 'local_levels': local_levels})

    # For post request
    form = IndividualForm(request.POST)  # CaptionForm is a form class using to validate form inputs
    if form.is_valid():
        try:
            individual = add_new_individual(request)  # From caption, all

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [individual])  # Convert single model to json before response
                return JsonResponse(data, safe=False)

            messages.success(request, 'Local level created successfully!')
            return redirect('individual')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Local Level')
            return redirect('color_option')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/vp/individual/create.html', {'form': form})
