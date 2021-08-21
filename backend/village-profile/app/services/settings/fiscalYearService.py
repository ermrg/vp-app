from app.models import FiscalYear


def get_all_fiscal_year():
    fiscal_year = FiscalYear.objects.all()
    return fiscal_year


def add_new_fiscal_year(request):
    data = request.POST
    user = request.user
    fiscal_year = FiscalYear.objects.create(
        year=data['year'] if data['year'] else '',
        code=data['code'] if data['code'] else '',
        # start_date_ad='',
        # end_date_ad='',
        # start_date_bs='',
        # end_date_bs='',
        status=0,
        user=user,
    )

    return fiscal_year


def change_status_by_id(fy_id):
    all_fy = get_all_fiscal_year()
    all_fy.update(status=0)

    fy = FiscalYear.objects.get(pk=fy_id)
    fy.status = 1
    fy.save()


def get_active_fiscal_year():
    return FiscalYear.objects.filter(status=1).first()


def get_fiscal_year_by_ad(data_ad):
    return FiscalYear.objects.filter(start_date_ad__lte=data_ad, end_date_ad__gte=data_ad).first()
