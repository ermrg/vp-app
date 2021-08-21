from app.forms.vp.household_form import  HouseholdDetailForm, HouseholdLandForm, \
    HouseholdAnimalForm, HouseholdInfrastructureForm, HouseholdEarthquakeStatusForm, HouseholdOtherForm
from app.models.vp.house_detail import HouseDetail
from app.models.vp.household import Household
from app.models.vp.household_animal import HouseholdAnimal
from app.models.vp.household_business import HouseholdBusiness
from app.models.vp.household_helper import HouseholdHelper
from app.models.vp.household_education import HouseholdEducation
from app.models.vp.household_expenses import HouseholdExpenses
from app.models.vp.household_facility import HouseholdFacility
from app.models.vp.household_festival import HouseholdFestival
from app.models.vp.household_fuel import HouseholdFuel
from app.models.vp.household_healthpost import HouseholdHealthPost
from app.models.vp.household_income import HouseholdIncome
from app.models.vp.household_infrastructure import HouseholdInfrastructure
from app.models.vp.household_land import HouseholdLand
from app.models.vp.household_natural_disaster import HouseholdNaturalDisaster
from app.models.vp.household_public_transport import HouseholdPublicTransport
from app.models.vp.household_sewage import HouseholdSewage
from app.models.vp.household_vehicle import HouseholdVehicle
from app.models.vp.household_watersource import HouseholdWaterSource
from app.models.vp.member import Member
from app.models.vp.member_deceased import MemberDeceased
from app.models.vp.rent_member import RentMember
from app.services.settings.settingService import create_basti


def get_household_by_id(hh_id):
    try:
        household = Household.objects.get(pk=hh_id)
    except Exception:
        household = None
    return household


def get_all_household(request):
    # office = request.user.profile.office
    household = Household.objects.filter(status=1)
    return household

#
# # def add_new_household(request):
# #     user = request.user
# #     form = HouseholdHouseholdForm(request.POST)
# #     if form.is_valid():
# #         hh = Household()
# #         hh.hoh_name = form.cleaned_data['hoh_name']
# #         hh.hoh_id = form.cleaned_data['hoh']
# #         hh.hh_no = form.cleaned_data['hh_no']
# #         hh.no_of_m = form.cleaned_data['no_of_m']
# #         hh.contact = form.cleaned_data['contact']
# #         hh.basti = form.cleaned_data['basti']
# #         hh.ward = form.cleaned_data['ward']
# #         hh.street = form.cleaned_data['street']
# #         hh.local_level_id = form.cleaned_data['local_level']
# #
# #         hh.key = form.cleaned_data['key']
# #         hh.office_id = user.profile.office_id
# #         hh.status = 1
# #         hh.step = 2
# #         hh.user_id = user.id
# #         hh.save()
# #         return hh
# #     return None
#
#
# def update_household(data, hh_id):
#     hh = get_household_by_id(hh_id)
#     hh.hoh_name = data['hoh_name']
#     hh.hoh_id = data['hoh']
#     hh.hh_no = data['hh_no']
#     hh.no_of_m = data['no_of_m']
#     hh.contact = data['contact']
#     hh.basti = data['basti']
#     hh.ward = data['ward']
#     hh.street = data['street']
#     hh.local_level_id = data['local_level']
#
#     hh.key = data['key']
#     hh.office_id = data['office_id']
#     hh.status = 1
#     hh.step = 2 if hh.step < 2 else hh.step
#     hh.user_id = data['user_id']
#     hh.save()
#     return hh
#
#
# def update_household_detail(data, hh_id):
#     hh = get_household_by_id(hh_id)
#     hh.ethnicity = data['ethnicity']
#     hh.mother_tongue = data['mother_tongue']
#     hh.type_of_residence = data['type_of_residence']
#     hh.bank_account = data['bank_account']
#     hh.occupation1 = data['occupation1']
#     hh.occupation2 = data['occupation2']
#     hh.remarks = data['remarks']
#     hh.is_migrated = data['is_migrated']
#     hh.is_married = data['is_married']
#     hh.migration_year = data['migration_year']
#     hh.step = 3 if hh.step < 3 else hh.step
#     hh.save()
#     return hh
#
#
# def update_household_land(data, hh_id):
#     hh = get_household_by_id(hh_id)
#
#     land = HouseholdLand()
#     land.type = data['type']
#     land.area = data['area']
#     land.kitta_no = data['kitta_no']
#     land.garden = data['garden']
#     land.irrigation = data['irrigation']
#     land.remarks = data['remarks']
#     land.household = hh
#     land.office_id = data['office_id']
#     land.user_id = data['user_id']
#     land.status = 1
#     land.save()
#     hh.step = 4 if hh.step < 4 else hh.step
#     hh.save()
#     return hh
#
#
# def update_household_animal(data, hh_id):
#     hh = get_household_by_id(hh_id)
#     animal = HouseholdAnimal()
#     animal.name = data['name']
#     animal.count = data['count']
#     animal.remarks = data['remarks']
#     animal.household = hh
#     animal.office_id = data['office_id']
#     animal.user_id = data['user_id']
#     animal.status = 1
#     animal.save()
#     hh.step = 5 if hh.step < 5 else hh.step
#     hh.save()
#     return hh
#
#
# def update_household_other_info(vehicle_data, festival_data, facility_data, hh_id):
#     hh = get_household_by_id(hh_id)
#     vehicle = HouseholdVehicle()
#     vehicle.name = vehicle_data['name']
#     vehicle.count = vehicle_data['count']
#     vehicle.remarks = vehicle_data['remarks']
#     vehicle.household = hh
#     vehicle.office_id = vehicle_data['office_id']
#     vehicle.user_id = vehicle_data['user_id']
#     vehicle.status = 1
#     vehicle.save()
#
#     festival = HouseholdFestival()
#     festival.name = festival_data['name']
#     festival.remarks = festival_data['remarks']
#     festival.household = hh
#     festival.office_id = festival_data['office_id']
#     festival.user_id = festival_data['user_id']
#     festival.status = 1
#     festival.save()
#
#     facility = HouseholdFacility()
#     facility.name = facility_data['name']
#     facility.count = facility_data['count']
#     facility.remarks = facility_data['remarks']
#     facility.household = hh
#     facility.office_id = facility_data['office_id']
#     facility.user_id = facility_data['user_id']
#     facility.status = 1
#     facility.save()
#
#     hh.step = 10
#     hh.save()
#     return hh
#
#
# def get_create_process_step(hh, step_):
#     if hh:
#         if hh.step == 10:
#             step = 1
#         elif step_ < hh.step:
#             step = step_
#         else:
#             step = hh.step
#     else:
#         step = 1
#     return step


# Household Detail Save
def save_household_detail(data):

    # if 'new_place_name' in data:
    #     new_basti = dict()
    #     new_basti['name'] = data['new_place_name']
    #     new_basti = create_basti(new_basti)
    #     data['place_name'] = new_basti.id

    household = Household()
    household.ward_id = data['ward_no']
    household.basti_id = data['place_name']
    household.marga_id = data['marg_name']
    household.religion_id = data['religion']
    household.jaati_id = data['caste']
    household.main_occupation_id = data['main_occupation']
    household.mother_tongue_id = data['mother_tongue']
    household.has_bank_acc = data['bank_ac']
    household.has_cooperative_acc = data['co_ac']
    household.has_garden = data['garden']
    household.member_with_life_insurance = data['life_insurance']
    household.member_with_health_insurance = data['health_insurance']
    household.responder_name = data['responder_name']
    household.house_num = data['house_no']
    household.reason_of_death_id = data['member_no']
    household.resident_type = data['migration_status']
    household.mobile_num = data['mobile_no']
    household.latitude = data['lat']
    household.longitude = data['long']
    household.responder_image = data['responder_photo']
    household.status = 1
    household.save()
    return household


# Deceased Member Save
def save_deceased_member(data, hh_id):
    hh = get_household_by_id(hh_id)
    deceased = MemberDeceased()
    house_hold = Household.objects.get(pk=hh_id)
    deceased.ward_id = house_hold.ward_id
    deceased.name = data['expire_mm_name']
    deceased.age_on_death = data['expire_mm_age']
    deceased.gender_id = data['expire_mm_gender']
    deceased.hh_id = hh.id
    deceased.reason_of_death_id = data['expire_reason']
    deceased.remarks = data['expire_remarks']
    deceased.month_of_death = data['expire_mm_month']
    deceased.save()
    return deceased


def get_all_household_deceased(request):
    household_deceased = MemberDeceased.objects.all()
    return household_deceased


# Member Save
def save_member(data, hh_id):
    hh = get_household_by_id(hh_id)
    member = Member()
    member.hh_id = hh.id
    house_hold = Household.objects.get(pk=hh_id)
    member.ward_id = house_hold.ward_id
    member.name_nep = data['mem_name']
    member.gender_id = data['mem_gender']
    member.dob_ad = data['mem_dob']
    member.citizenship_num = data['mem_citizen']
    member.mobile_num = data['mem_contact']
    member.education_status_id = data['mem_edu_status']
    member.education_level_id = data['mem_edu_level']
    member.main_occupation_id = data['mem_profession']
    member.monthly_income = data['mem_monthly_salary']
    member.marital_status_id = data['mem_marital_status']
    member.relation_with_hoh_id = data['relation_with_owner']

    member.save()
    return member


def get_all_household_members(request):
    household_member = Member.objects.all()
    return household_member


# Member Save
def save_househead(data, hh_id):
    hh = get_household_by_id(hh_id)
    member = Member()
    member.hh = hh
    house_hold = Household.objects.get(pk=hh_id)
    member.ward_id = house_hold.ward_id
    member.name_eng = data['owner_name']
    member.gender_id = data['owner_gender']
    member.dob_ad = data['owner_dob']
    member.citizenship_num = data['owner_citizen']
    member.mobile_num = data['owner_contact']
    member.education_status_id = data['owner_edu_status']
    member.education_level_id = data['owner_edu_level']
    member.main_occupation_id = data['owner_profession']
    member.monthly_income = data['owner_monthly_salary']
    member.marital_status_id = data['owner_marital_status']
    # member.relation_with_hoh = data['relation_with_owner']

    member.save()
    if 'is_hh' in data:
        hh.hoh = member
        hh.hoh_name = member.name_eng
        hh.save()
    return member


def get_all_househeads(request):
    househead = Member.objects.filter(relation_with_hoh_id=1)
    return househead


def get_all_househead_by_id(hh_id):
    househeadz = Member.objects.filter(relation_with_hoh_id=1, hh_id=hh_id)
    return househeadz


# House Details
def save_house_details(data, hh_id):
    hh = get_household_by_id(hh_id)
    details = HouseDetail()
    house_hold = Household.objects.get(pk=hh_id)
    details.ward_id = house_hold.ward_id
    details.house_num = data['house_no']
    details.house_type_id = data['home_type']
    details.hh_id = hh.id  # hh.id
    details.roof_type_id = data['roof_type']
    details.build_year_bs = data['construct_year']
    details.map_pass = data['home_design']
    details.map_pass_date_bs = data['home_design_date']
    details.member_id = data['home_owner']
    details.image = data['home_image']
    details.save()
    return details


def get_all_household_houses(request):
    house = HouseDetail.objects.all()
    return house


# Rent Members
def save_rent_members(data, hh_id):
    hh = get_household_by_id(hh_id)
    rent_member = RentMember()
    house_hold = Household.objects.get(pk=hh_id)
    rent_member.ward_id = house_hold.ward_id
    rent_member.rent_member_head = data['rent_member_owner_name']
    rent_member.migrated_from = data['rent_member_from_place']
    rent_member.hh_id = hh.id  # hh.id
    rent_member.no_of_member = data['rent_member_count']
    rent_member.room_no = data['rent_member_room_count']
    rent_member.reason_for_migration = data['rent_member_reason']

    rent_member.save()
    return rent_member


def get_all_household_rents(request):
    rent = RentMember.objects.all()
    return rent


# Land Details
def save_land_details(data, hh_id):
    hh = get_household_by_id(hh_id)
    land_details = HouseholdLand()
    house_hold = Household.objects.get(pk=hh_id)
    land_details.ward_id = house_hold.ward_id
    land_details.land_type_id = data['land_type']
    land_details.area1 = data['land_area1']
    land_details.hh_id = hh.id  # hh.id
    land_details.area2 = data['land_area2']
    land_details.area3 = data['land_area3']
    land_details.area4 = data['land_area4']
    land_details.irrigation = data['irrigation_facility']
    land_details.kitta_no = data['kitta_no']
    land_details.remarks = data['land_remarks']

    land_details.save()
    return land_details


def get_all_household_lands(request):
    land = HouseholdLand.objects.all()
    return land


# household_animal Details
def save_animals_details(data, hh_id):
    hh = get_household_by_id(hh_id)
    animals_details = HouseholdAnimal()
    house_hold = Household.objects.get(pk=hh_id)
    animals_details.ward_id = house_hold.ward_id
    animals_details.count = data['animal_count']
    animals_details.animal_type_id = data['animal_type']
    animals_details.ward_id = data['ward']
    animals_details.hh_id = hh.id  # hh.id
    animals_details.remarks = data['animal_remarks']

    animals_details.save()
    return animals_details


def get_all_household_animals(request):
    household_animals = HouseholdAnimal.objects.all()
    return household_animals


# Business Details
def save_business_details(data, hh_id):
    hh = get_household_by_id(hh_id)
    business_details = HouseholdBusiness()
    house_hold = Household.objects.get(pk=hh_id)
    business_details.ward_id = house_hold.ward_id
    business_details.business_type_id = data['business_type']
    business_details.is_registered = data['reg_status']
    business_details.money_invested = data['money_spend']
    business_details.business_place = data['business_location']
    business_details.hh_id = hh.id  # hh.id
    business_details.remarks = data['business_remarks']

    business_details.save()
    return business_details


def get_all_household_businesses(request):
    household_businesses = HouseholdBusiness.objects.all()
    return household_businesses


# Child Labour Details
def save_helper(data, hh_id):
    hh = get_household_by_id(hh_id)
    helper = HouseholdHelper()
    house_hold = Household.objects.get(pk=hh_id)
    helper.ward_id = house_hold.ward_id
    helper.child_name = data['childlabour_name']
    helper.child_labor_status = data['childlabour_status']
    helper.start_date_bs = data['childlabour_fromdate']
    helper.household_id = hh.id  # hh.id
    helper.remarks = data['childlabour_remarks']
    helper.gender_id = data['childlabour_gender']
    helper.age = data['childlabour_age']

    helper.save()
    return helper


def get_all_household_helpers(request):
    household_helpers = HouseholdHelper.objects.all()
    return household_helpers


# Family Income Details
def save_family_income(data, hh_id):
    hh = get_household_by_id(hh_id)
    family_income = HouseholdIncome()
    house_hold = Household.objects.get(pk=hh_id)
    family_income.ward_id = house_hold.ward_id
    family_income.source_id = data['earning_source']
    family_income.amount = data['earning_amount']
    family_income.start_date_bs = data['earning_from']
    family_income.hh_id = hh.id  # hh.id
    family_income.remarks = data['earning_remarks']

    family_income.save()
    return family_income


def get_all_household_incomes(request):
    household_incomes = HouseholdIncome.objects.all()
    return household_incomes


# Family Expenses Details
def save_family_expenses(data, hh_id):
    hh = get_household_by_id(hh_id)
    family_expenses = HouseholdExpenses()
    house_hold = Household.objects.get(pk=hh_id)
    family_expenses.ward_id = house_hold.ward_id
    family_expenses.food_expenses = data['expense_food']
    family_expenses.health_expenses = data['expense_health']
    family_expenses.education_expenses = data['expense_education']
    family_expenses.other_expenses = data['expense_other']
    family_expenses.hh_id = hh.id  # hh.id
    family_expenses.remarks = data['expense_remarks']

    family_expenses.save()
    return family_expenses


def get_all_household_expenses(request):
    household_expenses = HouseholdExpenses.objects.all()
    return household_expenses


# Vehicle Details
def save_vehicle_details(data, hh_id):
    hh = get_household_by_id(hh_id)
    vehicle_details = HouseholdVehicle()
    house_hold = Household.objects.get(pk=hh_id)
    vehicle_details.ward_id = house_hold.ward_id
    vehicle_details.vehicle_type_id = data['vehicles_type']
    vehicle_details.is_available = data['vehicles_availability']
    vehicle_details.count = data['vehicles_count']
    vehicle_details.hh_id = hh.id  # hh.id
    vehicle_details.remarks = data['vehicles_remarks']

    vehicle_details.save()
    return vehicle_details


# Festival Details
def save_festivals_details(data, hh_id):
    hh = get_household_by_id(hh_id)
    household_festivals = HouseholdFestival()
    house_hold = Household.objects.get(pk=hh_id)
    household_festivals.ward_id = house_hold.ward_id
    household_festivals.festival_id = data['festival_id']
    household_festivals.hh_id = hh.id  # hh.id
    household_festivals.remarks = data['festival_remarks']

    household_festivals.save()
    return household_festivals


# Other Facility
def save_other_facility(data, hh_id):
    hh = get_household_by_id(hh_id)
    other_facility = HouseholdFacility()
    house_hold = Household.objects.get(pk=hh_id)
    other_facility.ward_id = house_hold.ward_id
    other_facility.name_id = data['facility_name']
    other_facility.is_available = data['facility_availability']
    other_facility.count = data['facility_count']
    other_facility.hh_id = hh.id  # hh.id
    other_facility.remarks = data['facility_remarks']

    other_facility.save()
    return other_facility


# Infrastructure
def save_infrastructure(data, hh_id):
    hh = get_household_by_id(hh_id)

    household_education = HouseholdEducation()
    house_hold = Household.objects.get(pk=hh_id)
    household_education.ward_id = house_hold.ward_id
    household_education.hh_id = hh.id  # hh.id
    household_education.primary_distance = data['edu_prim_distance']
    household_education.secondary_distance = data['edu_sec_distance']
    household_education.higher_secondary_distance = data['edu_higsec_distance']
    household_education.save()

    household_water_source = HouseholdWaterSource()
    house_hold = Household.objects.get(pk=hh_id)
    household_water_source.ward_id = house_hold.ward_id
    household_water_source.hh_id = hh.id  # hh.id
    household_water_source.water_source_id = data['water_source']
    household_water_source.distance = data['water_distance']
    household_water_source.unit = data['water_distance_unit']
    household_water_source.time = data['water_time']
    household_water_source.has_private_tap = data['tap_type']
    household_water_source.save()

    household_fuel = HouseholdFuel()
    household_fuel.hh_id = hh.id  # hh.id
    house_hold = Household.objects.get(pk=hh_id)
    household_fuel.ward_id = house_hold.ward_id
    household_fuel.light_fuel_id = data['fuel_light']
    household_fuel.cooking_fuel_id = data['fuel_cooking']
    household_fuel.garbage_management_id = data['fuel_garbage']
    household_fuel.save()

    household_public_transport = HouseholdPublicTransport()
    household_public_transport.hh_id = hh.id  # hh.id
    house_hold = Household.objects.get(pk=hh_id)
    household_public_transport.ward_id = house_hold.ward_id
    household_public_transport.distance = data['trans_distance']
    household_public_transport.possible_distance = data['trans_possi_distance']
    household_public_transport.road_width = data['road_width']
    household_public_transport.save()

    household_sewage = HouseholdSewage()
    household_sewage.hh_id = hh.id  # hh.id
    house_hold = Household.objects.get(pk=hh_id)
    household_sewage.ward_id = house_hold.ward_id
    household_sewage.toilet_type_id = data['toilet_type']
    household_sewage.sewage_type_id = data['sewage_type']
    household_sewage.save()

    household_healthpost = HouseholdHealthPost()
    household_healthpost.hh_id = hh.id  # hh.id
    house_hold = Household.objects.get(pk=hh_id)
    household_healthpost.ward_id = house_hold.ward_id
    household_healthpost.time = data['health_time']
    household_healthpost.distance = data['health_distance']
    household_healthpost.save()

    household_disaster = HouseholdNaturalDisaster()
    household_disaster.hh_id = hh.id  # hh.id
    house_hold = Household.objects.get(pk=hh_id)
    household_disaster.ward_id = house_hold.ward_id
    household_disaster.disaster_id = data['disaster']
    household_disaster.current_status_id = data['current_state']
    household_disaster.save()

    return household_disaster,  household_education, household_water_source, household_fuel, household_public_transport, household_sewage, household_healthpost


def get_all_household_infrastructures(request):

    household_infrastructures = HouseholdInfrastructure.objects.all()

    return household_infrastructures


