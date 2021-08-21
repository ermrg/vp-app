from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from app.forms.settings.settings_form import CollectorForm
from app.models import Collector
from app.services.settings.settingService import create_collector, get_all_collectors


def index(request):
    collectors = get_all_collectors()
    return render(request, 'app/backend/settings/collector/index.html', {'collectors': collectors})


def collector_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/collector/create.html')
    data = request.POST
    form = CollectorForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        create_collector(data)
        messages.success(request, 'Collector created successfully')
        return redirect('setting.collector.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create collector')
        #     return redirect('setting.disaster_name.create')


def delete_collector(request, id):
    collector = Collector.objects.get(pk=id)
    if request.method == "GET":
        collector.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.collector')

    return render(request, 'app/backend/settings/collector/index.html', {'collectors': collector})


def edit_collector(request, id):
    collector = Collector.objects.get(pk=id)
    return render(request, 'app/backend/settings/collector/edit.html', {'collector': collector})


def update_collector(request, id):
    data = request.POST
    collector = Collector.objects.get(pk=id)
    if data['name'] and data['name']:
        collector.name = data['name']
    if data['phone'] and data['phone']:
        collector.phone = data['phone']
    if data['password'] and data['password']:
        collector.password = data['password']
    collector.save()
    if request.is_ajax():
        data = list(collector.values())
        return JsonResponse(data, safe=False)
    return redirect('setting.collector')

