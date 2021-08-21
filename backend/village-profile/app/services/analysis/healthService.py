from app.models.vp.member import Member


                                    # Vaccinated or Not
def get_all_vaccinated():
    vaccinated = Member.objects.filter(is_vaccinated=1).count()
    return vaccinated


def get_all_non_vaccinated():
    non_vaccinated = Member.objects.filter(is_vaccinated=0).count()
    return non_vaccinated
