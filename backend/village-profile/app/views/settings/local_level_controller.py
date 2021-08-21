from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.local_level_form import LocalLevelForm
from app.services.settings.localLevelService import get_all_local_levels, add_new_local_level
from app.services.settings.provinceService import get_all_province
from app.services.settings.discrictService import get_all_district


@login_required
def list_local_level(request):
    local_levels = get_all_local_levels()  # All database related logic are in Service
    return render(request, 'app/backend/settings/local_level/index.html', {'local_levels': local_levels})


@login_required
def create_local_level(request):
    # For get request
    provinces = get_all_province()
    districts = get_all_district()
    if request.method == 'GET':
        return render(request, 'app/backend/settings/local_level/create.html', {'provinces': provinces, 'districts': districts})

    # For post request
    form = LocalLevelForm(request.POST)  # CaptionForm is a form class using to validate form inputs
    if form.is_valid():
        try:
            local_level = add_new_local_level(request)  # From caption, all

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [local_level])  # Convert single model to json before response
                return JsonResponse(data, safe=False)

            messages.success(request, 'Local level created successfully!')
            return redirect('local_level')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Local Level')
            return redirect('local_level')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/local_level/create.html', {'form': form})
