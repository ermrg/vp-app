from app.models.settings.local_level import LocalLevel


def get_all_local_levels():
    local_level = LocalLevel.objects.all()
    return local_level


def add_new_local_level(request):
    data = request.POST
    user = request.user
    local_level = LocalLevel.objects.create(
        name=data['name'] if data['name'] else '',
        code=data['code'] if data['code'] else '',
        district_id=data['district'] if data['district'] else None,
        province_id=data['province'] if data['province'] else None,

        status=1,
        user=user,
    )

    return local_level
