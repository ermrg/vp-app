from django.http import JsonResponse

from app.services.settings.settingService import get_all_wards, get_all_bastis, get_all_collectors


def get_wards(request):
    wards = get_all_wards()
    data = list(wards.values())
    return JsonResponse(data, safe=False)


def get_bastis(request):
    bastis = get_all_bastis()
    data = list(bastis.values())
    return JsonResponse(data, safe=False)


def get_collectors(request):
    collectors = get_all_collectors()
    data = list(collectors.values())
    return JsonResponse(data, safe=False)
