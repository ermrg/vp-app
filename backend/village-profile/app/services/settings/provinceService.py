from app.models.settings.province import Province


def get_all_province():
    province = Province.objects.all()
    return province


def add_new_province(request):
    data = request.POST
    user = request.user
    province = Province.objects.create(
        name=data['name'] if data['name'] else '',
        code=data['code'] if data['code'] else '',

        status=1,
        user=user,
    )

    return province

