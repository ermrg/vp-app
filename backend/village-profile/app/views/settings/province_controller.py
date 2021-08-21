from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.province_form import ProvinceForm
from app.services.settings.provinceService import get_all_province, add_new_province


@login_required
def list_province(request):
    provinces = get_all_province()
    return render(request, 'app/backend/settings/province/index.html', {'provinces': provinces})


@login_required
def create_province(request):
    # For get request
    if request.method == 'GET':
        return render(request, 'app/backend/settings/province/create.html')

    # For post request
    form = ProvinceForm(request.POST)
    if form.is_valid():
        try:
            province = add_new_province(request)

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [province])
                return JsonResponse(data, safe=False)

            messages.success(request, 'Province created successfully!')
            return redirect('province')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Province')
            return redirect('province')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/province/create.html', {'form': form})
