from app.models.settings.fiscal_year import FiscalYear


def write_stuff_here_to_make_available_all_over(request):
    fiscal_year = FiscalYear.objects.filter(status=1).first()
    return {
        'fy': fiscal_year
    }
