from app.models.vp.member import Member


def get_all_individual(request):
    office = request.user.profile.office
    individual = Member.objects.filter(office=office, status=1)
    return individual


def add_new_individual(request):
    data = request.POST
    user = request.user
    individual = Member.objects.create(
        name=data['name'] if data['name'] else '',
        code=data['code'] if data['code'] else '',
        district_id=data['district'] if data['district'] else None,
        province_id=data['province'] if data['province'] else None,
        local_level_id=data['local_level'] if data['local_level'] else None,

        status=1,
        user=user,
    )

    return individual
