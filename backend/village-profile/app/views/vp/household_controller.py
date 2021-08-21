from django.contrib import messages
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.vp.household_form import HouseholdDetailForm, HouseholdLandForm, HouseholdAnimalForm, \
    HouseholdInfrastructureForm, HouseholdEarthquakeStatusForm, HouseholdOtherForm, \
    HouseholdDeceasedForm, HouseholdOwnerForm, HouseDetailForm, RentMemberForm, LandDetailsForm, AnimalDetailsForm, \
    BusinessDetailsForm, VehicleDetailForm, OtherFacilityForm, FestivalForm, FamilyExpensesForm, \
    FamilyIncomeForm, MemberForm, HelperForm
from app.models.vp.household import Household
from app.resources import HouseholdResource, HouseheadResource, MemberResource, HouseDetailsResource, DeceasedResource, \
    LandResource, AnimalResource, BusinessTypesResource, FestivalResource, IncomeResource, ChildLabourResource, \
    ExpensesResource, VehicleResource, FacilityResource, InfrastructureResource, RentMemberResource
from app.services.settings.localLevelService import get_all_local_levels
from app.services.settings.provinceService import get_all_province
from app.services.settings.discrictService import get_all_district
from app.services.settings.settingService import get_all_business_types, get_all_jaatis, get_all_animal_types, \
    get_all_death_reasons, get_all_mother_tongues, get_all_main_occupations, get_all_education_levels, \
    get_all_education_statuses, get_all_marital_statuses, get_all_house_types, get_all_roof_types, get_all_land_types, \
    get_all_festivals, get_all_vehicle_types, get_all_facilities, get_all_income_sources, get_all_water_sources, \
    get_all_light_fuels, get_all_cooking_fuels, get_all_garbage_managements, get_all_sewage_types, get_all_toilet_types, \
    get_all_disability_types, get_all_foreign_reasons, get_all_vaccine_names, get_all_religions, \
    get_all_technical_skills, get_all_countries, get_all_relation_with_hohs, get_all_bastis, get_all_margas, \
    get_all_wards, get_all_disaster_names, get_all_house_damage_statuses, get_all_disability_cards, get_all_genders
from app.services.vp.householdService import get_all_household, get_household_by_id, save_deceased_member, \
    save_household_detail, save_member, save_house_details, save_rent_members, save_land_details, save_animals_details, \
    save_business_details, save_helper, save_vehicle_details, save_other_facility, save_infrastructure, \
    save_festivals_details, save_family_income, save_family_expenses, save_househead


# noinspection PyUnresolvedReferences
@login_required
def list_household(request):
    households = get_all_household(request)
    return render(request, 'app/backend/vp/household/index.html', {'households': households})


@login_required
def create_household(request, hh_id=None):
    context = dict()
    context['provinces'] = get_all_province()
    context['districts'] = get_all_district()
    context['local_levels'] = get_all_local_levels()
    context['households'] = get_household_by_id(hh_id)
    context['business_types'] = get_all_business_types()
    context['jaatis'] = get_all_jaatis()
    context['animal_types'] = get_all_animal_types()
    context['death_reasons'] = get_all_death_reasons()
    context['mother_tongue'] = get_all_mother_tongues()
    context['main_occupation'] = get_all_main_occupations()
    context['education_level'] = get_all_education_levels()
    context['education_status'] = get_all_education_statuses()
    context['marital_status'] = get_all_marital_statuses()
    context['house_type'] = get_all_house_types()
    context['roof_type'] = get_all_roof_types()
    context['land_type'] = get_all_land_types()
    context['festival'] = get_all_festivals()
    context['vehicle_type'] = get_all_vehicle_types()
    context['facility'] = get_all_facilities()
    context['income_source'] = get_all_income_sources()
    context['water_source'] = get_all_water_sources()
    context['light_fuel'] = get_all_light_fuels()
    context['cooking_fuel'] = get_all_cooking_fuels()
    context['sewage_type'] = get_all_sewage_types()
    context['toilet_type'] = get_all_toilet_types()
    context['garbage_management'] = get_all_garbage_managements()
    context['disability'] = get_all_disability_types()
    context['abroad_reason'] = get_all_foreign_reasons()
    context['vaccine'] = get_all_vaccine_names()
    context['religion'] = get_all_religions()
    context['technical_skill'] = get_all_technical_skills()
    context['country'] = get_all_countries()
    context['basti'] = get_all_bastis()
    context['wards'] = get_all_wards()
    context['disasters'] = get_all_disaster_names()
    context['house_statuses'] = get_all_house_damage_statuses()
    context['margas'] = get_all_margas()
    context['disability_cards'] = get_all_disability_cards()
    context['genders'] = get_all_genders()
    context['relation'] = get_all_relation_with_hohs()

    return render(request, 'app/backend/vp/household/create.html', context)


# Household Details
def add_household(request):
    data = request.POST
    form = HouseholdDetailForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        household_detail = save_household_detail(data)
        if request.is_ajax():
            data = serializers.serialize('json', [household_detail])  # Convert single model to json before response
            return JsonResponse(data, safe=False)

        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')
    messages.error(request, 'Can not create household')
    return redirect('create_household')


def update_household(request, hh_id):
    return JsonResponse(hh_id, safe=False)


# House Head
def add_househead(request, hh_id):
    data = request.POST
    form = HouseholdOwnerForm(data)  # HH Owner form
    if form.is_valid():
        # try:
        data = form.cleaned_data
        data['is_hh'] = True  # Remove this for memeber create
        member = save_househead(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [member])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create House Head Member')
    return redirect('create_household')


def update_househead(request, hoh_id):
    return JsonResponse(hoh_id, safe=False)


# Household Member
def add_member(request, hh_id):
    data = request.POST
    form = MemberForm(data)  # HH Owner form
    if form.is_valid():
        # try:
        data = form.cleaned_data
        member = save_member(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [member])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Household Member')
    return redirect('create_household')


# def update_member(request, hoh_id):
#     return JsonResponse(hoh_id, safe=False)


# Deceased Member
def add_deceased(request, hh_id):
    data = request.POST
    form = HouseholdDeceasedForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        deceased_member = save_deceased_member(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [deceased_member])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Deceased Member')
    return redirect('create_household')


# House Details
def add_house_details(request, hh_id):
    data = request.POST
    form = HouseDetailForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        house_details = save_house_details(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [house_details])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create House Details')
    return redirect('create_household')


# Rent Members
def add_rent_member(request, hh_id):
    data = request.POST
    form = RentMemberForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        rent_member = save_rent_members(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [rent_member])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Rent Members')
    return redirect('create_household')


# Land Details
def add_land_details(request, hh_id):
    data = request.POST
    form = LandDetailsForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        land_details = save_land_details(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [land_details])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Land Details')
    return redirect('create_household')


# household_animal Details
def add_animals_details(request, hh_id):
    data = request.POST
    form = AnimalDetailsForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        animals_details = save_animals_details(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [animals_details])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create household_animal Details')
    return redirect('create_household')


# Business Details
def add_business_details(request, hh_id):
    data = request.POST
    form = BusinessDetailsForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        business_details = save_business_details(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [business_details])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create household_business Details')
    return redirect('create_household')


# Festival
def add_festivals(request, hh_id):
    festivals = request.POST.getlist('festival_name')
    form = FestivalForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        for festival in festivals:
            fest = dict()
            fest['festival_id'] = festival
            fest['festival_remarks'] = data['festival_remarks']
            save_festivals_details(fest, hh_id)

        if request.is_ajax():
            # data = serializers.serialize('json', [festivals])  # Convert single model to json before response
            return JsonResponse("Success", safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create household_festival Details')
    return redirect('create_household')


# Child Labour Details
def add_helper(request, hh_id):
    data = request.POST
    form = HelperForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        helper = save_helper(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [helper])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create House Helper Details')
    return redirect('create_household')


# Family Income Details
def add_income(request, hh_id):
    data = request.POST
    form = FamilyIncomeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        family_income = save_family_income(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [family_income])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Income Details')
    return redirect('create_household')


# Family Expenses Details
def add_expenses(request, hh_id):
    data = request.POST
    form = FamilyExpensesForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        family_expenses = save_family_expenses(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [family_expenses])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Expenses Details')
    return redirect('create_household')


# Vehicle Details
def add_vehicle_details(request, hh_id):
    data = request.POST
    form = VehicleDetailForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        vehicle_details = save_vehicle_details(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [vehicle_details])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Vehicle Details')
    return redirect('create_household')


# Other Facility
def add_other_facility(request, hh_id):
    data = request.POST
    form = OtherFacilityForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        other_facility = save_other_facility(data, hh_id)
        if request.is_ajax():
            data = serializers.serialize('json', [other_facility])  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Other Facility')
    return redirect('create_household')


# Infrastructure
def add_infrastructure(request, hh_id):
    data = request.POST
    form = HouseholdInfrastructureForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        infrastructure = save_infrastructure(data, hh_id)

        if request.is_ajax():
            data = serializers.serialize('json', infrastructure)  # Convert single model to json before response
            return JsonResponse(data, safe=False)
        # except Exception:
        #     #     if request.is_ajax():
        #     #         return HttpResponse('Failed')
        #     #     messages.error(request, 'Can not create Household')
        #     #     return redirect('create_household')

    messages.error(request, 'Can not create Other Facility')
    return redirect('create_household')

