from django.contrib import messages
from django.shortcuts import render, redirect
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from app.models.vp.house_detail import HouseDetail
from app.models.vp.household import Household
from app.models.vp.household_animal import HouseholdAnimal
from app.models.vp.household_business import HouseholdBusiness
from app.models.vp.household_expenses import HouseholdExpenses
from app.models.vp.household_helper import HouseholdHelper
from app.models.vp.household_income import HouseholdIncome
from app.models.vp.household_infrastructure import HouseholdInfrastructure
from app.models.vp.household_land import HouseholdLand
from app.models.vp.member import Member
from app.models.vp.member_deceased import MemberDeceased
from app.models.vp.rent_member import RentMember
from app.services.settings.settingService import get_all_animal_types, get_all_business_types, get_all_death_reasons, \
    get_all_genders, get_all_house_types, get_all_roof_types, get_all_land_types, get_all_income_sources, \
    get_all_education_statuses, get_all_marital_statuses, get_all_education_levels, get_all_main_occupations, \
    get_all_relation_with_hohs, get_all_disability_types, get_all_countries, get_all_technical_skills, \
    get_all_foreign_reasons, get_all_vaccine_names, get_all_disability_cards, get_all_water_sources, \
    get_all_cooking_fuels, get_all_light_fuels, get_all_garbage_managements, get_all_toilet_types, get_all_sewage_types, \
    get_all_disaster_names, get_all_house_damage_statuses, get_all_wards, get_all_bastis_by_ward, \
    get_all_mother_tongues, get_all_jaatis, get_all_religions, get_all_margas, get_all_bastis
from app.services.vp.householdService import get_all_household_animals, get_all_household_businesses, \
    get_all_household_deceased, get_all_household_incomes, get_all_househeads, get_all_household_infrastructures, \
    get_all_household_members, get_all_household_houses, get_all_household_lands, get_all_household_rents, \
    get_all_household_helpers, get_all_household_expenses, get_all_househead_by_id


def delete_household(request, id):
    household = Household.objects.get(id=id)
    if request.method == "GET":
        household.delete()
        messages.success(request, 'Household Deleted')
        return redirect('household')

    return render(request, 'app/backend/vp/household/index.html', {'households': household})


def edit_household(request, id):
    household = Household.objects.get(pk=id)
    wards = get_all_wards()
    # basti = get_all_bastis_by_ward(ward_id)
    basti = get_all_bastis()
    language = get_all_mother_tongues()
    jaati = get_all_jaatis()
    occupation = get_all_main_occupations()
    religion = get_all_religions()
    marga = get_all_margas()
    return render(request, 'app/backend/vp/household/reports/household/edit.html',
                  {'households': household, 'wards': wards, 'jaatis': jaati, 'mother_tongue': language,
                   'main_occupation': occupation, 'religion': religion, 'basti': basti, 'margas': marga})


def update_household(request, id):
    data = request.POST
    household = Household.objects.get(pk=id)
    household.ward_id = data['ward_no']
    household.basti_id = data['place_name']
    household.marga_id = data['marg_name']
    household.religion_id = data['religion']
    household.jaati_id = data['caste']
    household.mother_tongue_id = data['mother_tongue']
    household.main_occupation_id = data['main_occupation']
    household.responder_name = data['responder_name']
    household.house_num = data['house_no']
    household.num_of_member = data['member_no']
    household.latitude = data['lat'] if str(data['lat']).strip() else None
    household.longitude = data['long'] if str(data['long']).strip() else None
    household.responder_image = data['responder_photo']
    household.save()
    return redirect('household')


def report(request):
    return render(request, 'app/backend/vp/reports.html')


def animal_report(request):
    wards = get_all_wards()
    animals = get_all_animal_types()
    household_animals = get_all_household_animals(request)
    return render(request, 'app/backend/vp/household/reports/household_animal/list.html',
                  {'household_animals': household_animals, 'animal_types': animals, 'wards': wards})


def delete_animal_details(request, id):
    household_animal = HouseholdAnimal.objects.get(pk=id)
    if request.method == "GET":
        household_animal.delete()
        messages.success(request, 'Data Deleted')
        return redirect('animal_report')

    return render(request, 'app/backend/vp/household/reports/household_animal', {'household_animals': household_animal})


def edit_household_animal(request, id):
    animals = get_all_animal_types()
    household_animal = HouseholdAnimal.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_animal/edit.html',
                  {'household_animals': household_animal, 'animal_types': animals})


def update_household_animal(request, id):
    data = request.POST
    household_animal = HouseholdAnimal.objects.get(pk=id)
    household_animal.animal_type_id = data['animal_type']
    household_animal.count = data['animal_count']
    household_animal.remarks = data['animal_remarks']
    household_animal.save()
    return redirect('animal_report')


def business_report(request):
    wards = get_all_wards()
    business_types = get_all_business_types()
    household_businesses = get_all_household_businesses(request)
    return render(request, 'app/backend/vp/household/reports/household_business/list.html',
                  {'household_businesses': household_businesses, 'business_types': business_types, 'wards': wards})


def delete_business_details(request, id):
    household_business = HouseholdBusiness.objects.get(pk=id)
    if request.method == "GET":
        household_business.delete()
        messages.success(request, 'Data Deleted')
        return redirect('business_report')

    return render(request, 'app/backend/vp/household/reports/household_animal',
                  {'household_businesses': household_business})


def edit_household_business(request, id):
    business = get_all_business_types()
    household_business = HouseholdBusiness.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_business/edit.html',
                  {'household_businesses': household_business, 'business_types': business})


def update_household_business(request, id):
    data = request.POST
    household_business = HouseholdBusiness.objects.get(pk=id)
    household_business.business_type_id = data['business_type']
    household_business.business_place = data['business_location']
    household_business.money_invested = data['money_spend']
    household_business.save()
    return redirect('business_report')


def deceased_report(request):
    wards = get_all_wards()
    death_reasons = get_all_death_reasons()
    household_deceased = get_all_household_deceased(request)
    return render(request, 'app/backend/vp/household/reports/household_deceased/list.html',
                  {'household_deceased': household_deceased, 'wards': wards, 'death_reasons': death_reasons})


def delete_deceased_details(request, id):
    household_deceased = MemberDeceased.objects.get(pk=id)
    if request.method == "GET":
        household_deceased.delete()
        messages.success(request, 'Data Deleted')
        return redirect('deceased_report')

    return render(request, 'app/backend/vp/household/reports/household_deceased',
                  {'household_deceased': household_deceased})


def edit_household_deceased(request, id):
    death_reason = get_all_death_reasons()
    gender = get_all_genders()
    deceased_member = MemberDeceased.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_deceased/edit.html',
                  {'household_deceased': deceased_member, 'death_reasons': death_reason, 'genders': gender})


def update_household_deceased(request, id):
    data = request.POST
    deceased_member = MemberDeceased.objects.get(pk=id)
    deceased_member.name = data['expire_mm_name']
    deceased_member.gender_id = data['expire_mm_gender']
    deceased_member.age_on_death = data['expire_mm_age']
    deceased_member.month_of_death = data['expire_mm_month']
    deceased_member.reason_of_death_id = data['expire_reason']
    deceased_member.save()
    return redirect('deceased_report')


def household_income_report(request):
    wards = get_all_wards()
    income_sources = get_all_income_sources()
    household_incomes = get_all_household_incomes(request)
    return render(request, 'app/backend/vp/household/reports/household_income/list.html',
                  {'household_incomes': household_incomes, 'income_sources': income_sources, 'wards': wards})


def delete_household_income(request, id):
    household_incomes = HouseholdIncome.objects.get(pk=id)
    if request.method == "GET":
        household_incomes.delete()
        messages.success(request, 'Data Deleted')
        return redirect('household_income')

    return render(request, 'app/backend/vp/household/reports/household_income',
                  {'household_incomes': household_incomes})


def edit_household_income(request, id):
    income_source = get_all_income_sources()
    income = HouseholdIncome.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_income/edit.html',
                  {'household_incomes': income, 'income_source': income_source})


def update_household_income(request, id):
    data = request.POST
    household_income = HouseholdIncome.objects.get(pk=id)
    household_income.income_source_id = data['earning_source']
    household_income.start_date_bs = data['earning_from']
    household_income.amount = data['earning_amount']
    household_income.save()
    return redirect('income_report')


def househead_report(request):
    wards = get_all_wards()
    bastis = get_all_bastis()
    margas = get_all_margas()
    genders = get_all_genders()
    ethnics = get_all_jaatis()
    religions = get_all_religions()
    mother_tongues = get_all_mother_tongues()
    househead = get_all_househeads(request)
    return render(request, 'app/backend/vp/household/reports/househead/list.html',
                  {'househead': househead, 'wards': wards,
                   'bastis': bastis, 'margas': margas, 'genders': genders, 'ethnics': ethnics, 'religions': religions,
                   'mother_tongues': mother_tongues})


def delete_househead(request, id):
    househead = Member.objects.get(pk=id)
    if request.method == "GET":
        househead.delete()
        messages.success(request, 'Data Deleted')
        return redirect('househead_report')

    return render(request, 'app/backend/vp/household/reports/househead', {'househead': househead})


def edit_househead(request, id):
    gender = get_all_genders()
    education_status = get_all_education_statuses()
    relation = get_all_relation_with_hohs()
    marital_status = get_all_marital_statuses()
    education_level = get_all_education_levels()
    main_occupation = get_all_main_occupations()
    disability_types = get_all_disability_types()
    disability_cards = get_all_disability_cards()
    country = get_all_countries()
    technical_skill = get_all_technical_skills()
    foreign_reason = get_all_foreign_reasons()
    vaccine = get_all_vaccine_names()
    househead = Member.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/househead/edit.html',
                  {'househead': househead, 'genders': gender, 'education_status': education_status,
                   'education_level': education_level, 'main_occupation': main_occupation,
                   'marital_status': marital_status, 'relation': relation, 'disability_cards': disability_cards,
                   'disability_types': disability_types, 'country': country, 'technical_skill': technical_skill,
                   'abroad_reason': foreign_reason, 'vaccine': vaccine})


def update_househead(request, id):
    data = request.POST
    househead = Member.objects.get(pk=id)
    househead.name_nep = data['owner_name']
    # if househead.name_nep != data['owner_name']:
    #     household = Household.objects.get(pk=id)
    #     household.hoh_name = data['owner_name']
    #     household.save()
    # else:
    #     # household = Household.objects.get(pk=id)
    #     # household.hoh_name = data['owner_name']
    #     househead.save()
    househead.gender_id = data['owner_gender']
    househead.dob_bs = data['owner_dob']
    househead.citizenship_num = data['owner_citizen']
    househead.mobile_num = data['owner_contact']
    househead.education_status_id = data['owner_edu_status']
    househead.education_level_id = data['owner_edu_level']
    househead.main_occupation_id = data['owner_profession']
    househead.marital_status_id = data['owner_marital_status']
    househead.monthly_income = data['owner_monthly_salary'] if str(data['owner_monthly_salary']).strip() else None

    househead.has_disability = request.POST.get('familydisability_flag', False)

    househead.has_technical_training = request.POST.get('familytech_knowl_flag', False)

    househead.has_chronic_disease = request.POST.get('familydisease_flag', False)

    househead.foreign_stay = request.POST.get('familyforeign_stay_flag', False)

    househead.is_married = request.POST.get('familychild_marry_flag', False)

    househead.is_vaccinated = request.POST.get('familybasic_inject_flag', False)

    househead.disability_type_id = data['owner_disability_type']
    househead.disability_card_id = data['owner_disability_card_type']
    househead.disease_name = data['owner_disease_name']
    # househead.treatment_status = data['member_tret_present_status']
    # househead.name_nep = data['member_treatatment_status']
    househead.technical_skill_id = data['owner_tech_know_type']
    househead.foreign_reason_id = data['owner_foreign_stay_objective']
    househead.country_visited_id = data['owner_foreign_country']
    househead.vaccine_name_id = data['owner_injection_type']
    # househead.name_nep = data['mem_name']
    # househead.name_nep = data['mem_name']

    househead.save()
    return redirect('househead_report')


def helper_report(request):
    wards = get_all_wards()
    genders = get_all_genders()
    household_helper = get_all_household_helpers(request)
    return render(request, 'app/backend/vp/household/reports/household_helper/list.html',
                  {'household_helpers': household_helper, 'wards': wards, 'genders': genders})


def delete_helper_details(request, id):
    household_helper = HouseholdHelper.objects.get(pk=id)
    if request.method == "GET":
        household_helper.delete()
        messages.success(request, 'Data Deleted')
        return redirect('helper_report')

    return render(request, 'app/backend/vp/household/reports/household_helper/list.html',
                  {'household_helpers': household_helper})


def edit_household_helper(request, id):
    gender = get_all_genders()
    helper = HouseholdHelper.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_helper/edit.html',
                  {'household_helpers': helper, 'genders': gender})


def update_household_helper(request, id):
    data = request.POST
    household_helper = HouseholdHelper.objects.get(pk=id)
    household_helper.child_name = data['childlabour_name']
    household_helper.child_labor_status = data['childlabour_status']
    household_helper.gender_id = data['childlabour_gender']
    household_helper.age = data['childlabour_age']
    household_helper.start_date_bs = data['childlabour_fromdate']
    household_helper.save()
    return redirect('helper_report')


def member_report(request):
    wards = get_all_wards()
    genders = get_all_genders()
    marital_statuses = get_all_marital_statuses()
    education_levels = get_all_education_levels()
    education_statuses = get_all_education_statuses()
    technical_skills = get_all_technical_skills()
    disability_types = get_all_disability_types()
    disability_cards = get_all_disability_cards()
    foreign_reasons = get_all_foreign_reasons()
    countries = get_all_countries()
    main_occupations = get_all_main_occupations()
    household_members = get_all_household_members(request)
    return render(request, 'app/backend/vp/household/reports/household_member/list.html',
                  {'household_members': household_members, 'wards': wards, 'genders': genders,
                   'marital_statuses': marital_statuses,
                   'education_levels': education_levels, 'education_statuses': education_statuses,
                   'technical_skills': technical_skills,
                   'disability_types': disability_types, 'disability_cards': disability_cards,
                   'foreign_reasons': foreign_reasons,
                   'countries': countries, 'main_occupations': main_occupations})


def delete_member_details(request, id):
    household_member = Member.objects.get(pk=id)
    if request.method == "GET":
        household_member.delete()
        messages.success(request, 'Member Deleted')
        return redirect('member_report')

    return render(request, 'app/backend/vp/household/reports/household_member', {'household_members': household_member})


def edit_household_member(request, id):
    gender = get_all_genders()
    education_status = get_all_education_statuses()
    relation = get_all_relation_with_hohs()
    marital_status = get_all_marital_statuses()
    education_level = get_all_education_levels()
    main_occupation = get_all_main_occupations()
    disability_types = get_all_disability_types()
    disability_cards = get_all_disability_cards()
    country = get_all_countries()
    technical_skill = get_all_technical_skills()
    foreign_reason = get_all_foreign_reasons()
    vaccine = get_all_vaccine_names()
    member = Member.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_member/edit.html',
                  {'household_members': member, 'genders': gender, 'education_status': education_status,
                   'education_level': education_level, 'main_occupation': main_occupation,
                   'marital_status': marital_status, 'relation': relation, 'disability_cards': disability_cards,
                   'disability_types': disability_types, 'country': country, 'technical_skill': technical_skill,
                   'abroad_reason': foreign_reason, 'vaccine': vaccine})


def update_household_member(request, id):
    data = request.POST
    member = Member.objects.get(pk=id)
    member.name_nep = data['mem_name']
    member.gender_id = data['mem_gender']
    member.dob_bs = data['mem_dob']
    member.citizenship_num = data['mem_citizen']
    member.mobile_num = data['mem_contact']
    member.education_status_id = data['mem_edu_status']
    member.education_level_id = data['mem_edu_level']
    member.main_occupation_id = data['mem_profession']
    member.relation_with_hoh_id = data['relation_with_owner']
    member.monthly_income = data['mem_monthly_salary'] if str(data['mem_monthly_salary']).strip() else None

    member.has_disability = request.POST.get('familydisability_flag', False)

    member.has_technical_training = request.POST.get('familytech_knowl_flag', False)

    member.has_chronic_disease = request.POST.get('familydisease_flag', False)

    member.foreign_stay = request.POST.get('familyforeign_stay_flag', False)

    member.is_married = request.POST.get('familychild_marry_flag', False)

    member.is_vaccinated = request.POST.get('familybasic_inject_flag', False)
    member.disability_type_id = data['member_disability_type']
    member.disability_card_id = data['member_disability_card_type']
    member.disease_name = data['member_disease_name']
    member.treatment_status = data['member_tret_present_status']
    # member.name_nep = data['member_treatatment_status']
    member.technical_skill_id = data['member_tech_know_type']
    member.foreign_reason_id = data['member_foreign_stay_objective']
    member.country_visited_id = data['member_foreign_country']
    member.vaccine_name_id = data['member_injection_type']
    # member.name_nep = data['mem_name']
    # member.name_nep = data['mem_name']
    member.save()
    return redirect('member_report')


def house_report(request):
    wards = get_all_wards()
    house_types = get_all_house_types()
    roof_types = get_all_roof_types()
    household_houses = get_all_household_houses(request)
    return render(request, 'app/backend/vp/household/reports/household_house/list.html',
                  {'household_houses': household_houses, 'house_types': house_types, 'roof_types': roof_types,
                   'wards': wards})


def delete_house_details(request, id):
    household_house = HouseDetail.objects.get(pk=id)
    if request.method == "GET":
        household_house.delete()
        messages.success(request, 'Data Deleted')
        return redirect('house_report')

    return render(request, 'app/backend/vp/household/reports/household_house/list.html',
                  {'household_houses': household_house})


def edit_household_house(request, id):
    house_type = get_all_house_types()
    roof_type = get_all_roof_types()
    house = HouseDetail.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_house/edit.html',
                  {'household_houses': house, 'roof_type': roof_type, 'house_type': house_type})


def update_household_house(request, id):
    data = request.POST
    house_details = HouseDetail.objects.get(pk=id)
    house_details.house_type_id = data['home_type']
    house_details.roof_type_id = data['roof_type']
    house_details.build_year_ad = data['construct_year']
    house_details.map_pass = data['home_design']
    house_details.map_pass_date_ad = data['home_design_date']
    house_details.image = data['home_image']
    house_details.save()
    return redirect('house_report')


def land_report(request):
    wards = get_all_wards()
    land_types = get_all_land_types()
    household_lands = get_all_household_lands(request)
    return render(request, 'app/backend/vp/household/reports/household_land/list.html',
                  {'household_lands': household_lands, 'wards': wards, 'land_types': land_types})


def delete_land_details(request, id):
    household_land = HouseholdLand.objects.get(pk=id)
    if request.method == "GET":
        household_land.delete()
        messages.success(request, 'Data Deleted')
        return redirect('land_report')

    return render(request, 'app/backend/vp/household/reports/household_land', {'household_lands': household_land})


def edit_household_land(request, id):
    land_type = get_all_land_types()
    land = HouseholdLand.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_land/edit.html',
                  {'household_lands': land, 'land_type': land_type})


def update_household_land(request, id):
    data = request.POST
    household_land = HouseholdLand.objects.get(pk=id)
    household_land.land_type_id = data['land_type']
    household_land.area1 = data['land_area1']
    household_land.area2 = data['land_area2']
    household_land.area3 = data['land_area3']
    household_land.area4 = data['land_area4']
    household_land.kitta_no = data['kitta_no']
    household_land.irrigation = data['irrigation_facility']
    household_land.save()
    return redirect('land_report')


def rent_member_report(request):
    household_rents = get_all_household_rents(request)
    return render(request, 'app/backend/vp/household/reports/household_rent_member/list.html',
                  {'household_rents': household_rents})


def delete_household_rent(request, id):
    household_rent = RentMember.objects.get(pk=id)
    if request.method == "GET":
        household_rent.delete()
        messages.success(request, 'Data Deleted')
        return redirect('rent_member_report')

    return render(request, 'app/backend/vp/household/reports/household_rent_member',
                  {'household_rents': household_rent})


def edit_household_rent(request, id):
    rent = RentMember.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_rent_member/edit.html',
                  {'household_rents': rent})


def update_household_rent(request, id):
    data = request.POST
    household_rent = RentMember.objects.get(pk=id)
    household_rent.rent_member_head = data['rent_member_owner_name']
    household_rent.room_no = data['rent_member_room_count']
    household_rent.migrated_from = data['rent_member_from_place']
    household_rent.no_of_member = data['rent_member_count']
    household_rent.reason_for_migration = data['rent_member_reason']
    household_rent.save()
    return redirect('rent_member_report')


def expenses_report(request):
    wards = get_all_wards()
    household_expenses = get_all_household_expenses(request)
    return render(request, 'app/backend/vp/household/reports/household_expenses/list.html',
                  {'family_expenses': household_expenses, 'wards': wards})


def delete_household_expenses(request, id):
    household_expenses = HouseholdExpenses.objects.get(pk=id)
    if request.method == "GET":
        household_expenses.delete()
        messages.success(request, 'Data Deleted')
        return redirect('expenses_report')

    return render(request, 'app/backend/vp/household/reports/household_expenses/list.html',
                  {'family_expenses': household_expenses})


def edit_household_expenses(request, id):
    expenses = HouseholdExpenses.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_expenses/edit.html',
                  {'family_expenses': expenses})


def update_household_expenses(request, id):
    data = request.POST
    household_expenses = HouseholdExpenses.objects.get(pk=id)
    household_expenses.food_expenses = data['expense_food']
    household_expenses.education_expenses = data['expense_education']
    household_expenses.health_expenses = data['expense_health']
    household_expenses.other_expenses = data['expense_other']
    household_expenses.remarks = data['expense_remarks']
    household_expenses.save()
    return redirect('expenses_report')


def infrastructure_report(request):
    water_sources = get_all_water_sources()
    cooking_fuels = get_all_cooking_fuels()
    light_fuels = get_all_light_fuels()
    toilet_types = get_all_toilet_types()
    garbage_managements = get_all_garbage_managements()
    sewage_types = get_all_sewage_types()
    household_infrastructures = get_all_household_infrastructures(request)
    return render(request, 'app/backend/vp/household/reports/household_infrastructure/list.html',
                  {'household_infrastructures': household_infrastructures, 'water_sources': water_sources,
                   'cooking_fuels': cooking_fuels, 'light_fuels': light_fuels, 'toilet_types': toilet_types,
                   'garbage_managements': garbage_managements, 'sewage_types': sewage_types})


def delete_infrastructure_details(request, id):
    household_infrastructure = HouseholdInfrastructure.objects.get(pk=id)
    if request.method == "GET":
        household_infrastructure.delete()
        messages.success(request, 'Data Deleted')
        return redirect('infrastructure_report')

    return render(request, 'app/backend/vp/household/reports/household_infrastructure',
                  {'household_infrastructures': household_infrastructure})


#
# def edit_household_infrastructure(request, id):
#     water_sources = get_all_water_sources()
#     cooking_fuel = get_all_cooking_fuels()
#     light_fuel = get_all_light_fuels()
#     garbage_management = get_all_garbage_managements()
#     toilet_types = get_all_toilet_types()
#     sewage_types = get_all_sewage_types()
#     infrastructure = HouseholdInfrastructure.objects.get(pk=id)
#     return render(request, 'app/backend/vp/household/reports/household_infrastructure/edit.html',
#                   {'household_infrastructures': infrastructure, 'water_source': water_sources,
#                    'cooking_fuel': cooking_fuel, 'toilet_type': toilet_types, 'sewage_type': sewage_types,
#                    'garbage_management': garbage_management, 'light_fuel': light_fuel})


def edit_household_infrastructure(request, id):
    water_sources = get_all_water_sources()
    cooking_fuel = get_all_cooking_fuels()
    light_fuel = get_all_light_fuels()
    garbage_management = get_all_garbage_managements()
    toilet_types = get_all_toilet_types()
    sewage_types = get_all_sewage_types()
    disaster = get_all_disaster_names()
    house_status = get_all_house_damage_statuses()
    infrastructure = HouseholdInfrastructure.objects.get(pk=id)
    return render(request, 'app/backend/vp/household/reports/household_infrastructure/edit.html',
                  {'household_infrastructures': infrastructure, 'water_source': water_sources,
                   'cooking_fuel': cooking_fuel, 'toilet_type': toilet_types, 'sewage_type': sewage_types,
                   'garbage_management': garbage_management, 'light_fuel': light_fuel, 'house': house_status,
                   'disasters': disaster})


def update_household_infrastructure(request, id):
    data = request.POST
    infrastructure = HouseholdInfrastructure.objects.get(pk=id)
    infrastructure.water_source_id = data['water_source']
    infrastructure.cooking_fuel_id = data['fuel_cooking']
    infrastructure.light_fuel_id = data['fuel_light']
    infrastructure.sewage_type_id = data['sewage_type']
    infrastructure.toilet_type_id = data['toilet_type']
    infrastructure.garbage_management_id = data['fuel_garbage']

    infrastructure.save()
    return redirect('infrastructure_report')
