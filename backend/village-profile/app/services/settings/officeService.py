from app.models.settings.office import Office


def get_all_office():
    office = Office.objects.all()
    return office


def add_new_office(request):
    data = request.POST
    user = request.user
    office = Office.objects.create(
        name=data['name'] if data['name'] else '',
        code=data['code'] if data['code'] else '',
        district_id=data['district'] if data['district'] else None,
        province_id=data['province'] if data['province'] else None,
        local_level_id=data['local_level'] if data['local_level'] else None,

        status=1,
        user=user,
    )

    return office
