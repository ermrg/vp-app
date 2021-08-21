from app.models.vp.household import Household
from app.models.vp.household_business import HouseholdBusiness
from app.models.vp.household_income import HouseholdIncome
from app.models.vp.member import Member


                                            # Bank AC
def get_all_with_bank_ac():
    with_bank_ac = Household.objects.filter(has_bank_acc=1).count()
    return with_bank_ac


def get_all_without_bank_ac():
    without_bank_ac = Household.objects.filter(has_bank_acc=0).count()
    return without_bank_ac


                                            # Income Source
def get_all_vegetable_agriculture():
    vegetable_agriculture = HouseholdIncome.objects.filter(source=1).count()
    return vegetable_agriculture


def get_all_animal_husbandry():
    animal_husbandry = HouseholdIncome.objects.filter(source=2).count()
    return animal_husbandry


def get_all_chicken_farm():
    chicken_farm = HouseholdIncome.objects.filter(source=3).count()
    return chicken_farm


def get_all_fish_farm():
    fish_farm = HouseholdIncome.objects.filter(source=4).count()
    return fish_farm


def get_all_indigence_labour():
    indigence_labour = HouseholdIncome.objects.filter(source=5).count()
    return indigence_labour


def get_all_business():
    business = HouseholdIncome.objects.filter(source=6).count()
    return business


def get_all_foreign_employment():
    foreign_employment = HouseholdIncome.objects.filter(source=7).count()
    return foreign_employment


def get_all_goverment_job():
    goverment_job = HouseholdIncome.objects.filter(source=8).count()
    return goverment_job


def get_all_non_gov_jobs():
    non_gov_jobs = HouseholdIncome.objects.filter(source=9).count()
    return non_gov_jobs


def get_all_house_rent():
    house_rent = HouseholdIncome.objects.filter(source=10).count()
    return house_rent


def get_all_land_rent():
    land_rent = HouseholdIncome.objects.filter(source=11).count()
    return land_rent


                                # Foreign Employed countries
def get_all_employed_in_australia():
    employed_in_australia = Member.objects.filter(country_visited=1, foreign_reason=1).count()
    return employed_in_australia


def get_all_employed_in_bahrain():
    employed_in_bahrain = Member.objects.filter(country_visited=2, foreign_reason=1).count()
    return employed_in_bahrain


def get_all_employed_in_korea():
    employed_in_korea = Member.objects.filter(country_visited=5, foreign_reason=1).count()
    return employed_in_korea


def get_all_employed_in_dubai():
    employed_in_dubai = Member.objects.filter(country_visited=7, foreign_reason=1).count()
    return employed_in_dubai


def get_all_employed_in_germany():
    employed_in_germany = Member.objects.filter(country_visited=8, foreign_reason=1).count()
    return employed_in_germany


def get_all_employed_in_india():
    employed_in_india = Member.objects.filter(country_visited=10, foreign_reason=1).count()
    return employed_in_india


def get_all_employed_in_iraq():
    employed_in_iraq = Member.objects.filter(country_visited=17, foreign_reason=1).count()
    return employed_in_iraq


def get_all_employed_in_israel():
    employed_in_israel = Member.objects.filter(country_visited=18, foreign_reason=1).count()
    return employed_in_israel


def get_all_employed_in_japan():
    employed_in_japan = Member.objects.filter(country_visited=19, foreign_reason=1).count()
    return employed_in_japan


def get_all_employed_in_kuwait():
    employed_in_kuwait = Member.objects.filter(country_visited=20, foreign_reason=1).count()
    return employed_in_kuwait


def get_all_employed_in_malaysia():
    employed_in_malaysia = Member.objects.filter(country_visited=23, foreign_reason=1).count()
    return employed_in_malaysia


def get_all_employed_in_qatar():
    employed_in_qatar = Member.objects.filter(country_visited=26, foreign_reason=1).count()
    return employed_in_qatar


def get_all_employed_in_saudi():
    employed_in_saudi = Member.objects.filter(country_visited=27, foreign_reason=1).count()
    return employed_in_saudi


def get_all_employed_in_america():
    employed_in_america = Member.objects.filter(country_visited=32, foreign_reason=1).count()
    return employed_in_america


def get_all_employed_in_england():
    employed_in_england = Member.objects.filter(country_visited=31, foreign_reason=1).count()
    return employed_in_england





