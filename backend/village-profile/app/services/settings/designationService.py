from app.models.settings.designation import Designation


def get_all_designation():
    designation = Designation.objects.all()
    return designation


def add_new_designation(request):
    data = request.POST
    user = request.user
    designation = Designation.objects.create(
        name=data['name'] if data['name'] else '',
        status=1,
        user=user,
    )

    return designation

