from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.fiscal_year_form import FiscalYearForm
from app.services.settings.fiscalYearService import get_all_fiscal_year, add_new_fiscal_year, change_status_by_id


@login_required
def list_fiscal_year(request):
    fiscal_years = get_all_fiscal_year()
    return render(request, 'app/backend/settings/fiscal_year/index.html', {'fiscal_years': fiscal_years})


@login_required
def create_fiscal_year(request):
    # For get request
    if request.method == 'GET':
        return render(request, 'app/backend/settings/fiscal_year/create.html')

    # For post request
    form = FiscalYearForm(request.POST)
    if form.is_valid():
        try:
            fiscal_year = add_new_fiscal_year(request)

            # For ajax request
            if request.is_ajax():
                data = serializers.serialize('json', [fiscal_year])
                return JsonResponse(data, safe=False)

            messages.success(request, 'Color Option created successfully!')
            return redirect('fiscal_year')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Position')
            return redirect('fiscal_year')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/fiscal_year/create.html', {'form': form})


@login_required
def change_status(request):
    fy_id = request.POST['fyid']
    change_status_by_id(fy_id)
    return redirect('fiscal_year')
