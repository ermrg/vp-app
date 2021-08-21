from app.models.settings.district import District


def get_all_district():
    district = District.objects.all()
    return district


def add_new_district(request):
    data = request.POST
    user = request.user
    district = District.objects.create(
        name=data['name'] if data['name'] else '',
        code=data['code'] if data['code'] else '',
        province_id=data['province'] if data['province'] else None,
        status=1,
        user=user,
    )

    return district

