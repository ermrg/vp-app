from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from app.forms.settings.settings_form import AnimalTypeForm, BastiForm, BusinessTypeForm, CookingFuelForm, CountryForm, \
    DisabilityTypeForm, DisasterForm, EducationLevelForm, EducationStatusForm, FacilityForm, FestivalForm, \
    ForeignReasonForm, GarbageManagementForm, HouseTypeForm, IncomeSourceForm, JaatiForm, LandTypeForm, LightFuelForm, \
    MainOccupationForm, MaritalStatusForm, MotherTongueForm, RelationWithHohForm, ReligionForm, RoofTypeForm, \
    SewageTypeForm, TechnicalSkillForm, ToiletTypeForm, VehicleTypeForm, WardForm, WaterSourceForm, MargaForm, \
    DeathReasonForm, VaccineNameForm, HouseDamageStatusForm
from app.models import AnimalType, Basti, BusinessType, CookingFuel, DeathReason, Country, DisabilityType, \
    EducationLevel, EducationStatus, Facility, LandType, LightFuel, MainOccupation, Marga, MaritalStatus, MotherTongue, \
    RelationWithHoh, Religion, RoofType, SewageType, TechnicalSkill, ToiletType, Ward, Disaster, Festival, \
    ForeignReason, GarbageManagement, HouseDamageStatus, HouseType, IncomeSource, Jaati, WaterSource, VehicleType
from app.models.settings.vaccine_name import VaccineName
from app.services.settings.localLevelService import get_all_local_levels
from app.services.settings.settingService import get_all_animal_types, create_animal_type, get_all_bastis, create_basti, \
    create_business_type, get_all_cooking_fuels, create_cooking_fuel, create_country, \
    get_all_countries, create_disability_type, get_all_disability_types, create_disaster_name, get_all_disaster_names, \
    create_education_level, get_all_education_levels, get_all_education_statuses, create_education_status, \
    create_facility, get_all_facilities, get_all_festivals, create_festival, get_all_foreign_reasons, \
    create_foreign_reason, get_all_garbage_managements, create_garbage_management, create_house_type, \
    get_all_house_types, get_all_income_sources, create_income_source, get_all_jaatis, create_jaati, get_all_land_types, \
    create_land_type, get_all_light_fuels, create_light_fuel, get_all_main_occupations, create_main_occupation, \
    get_all_marital_statuses, create_marital_status, get_all_mother_tongues, create_mother_tongue, \
    create_relation_with_hoh, get_all_relation_with_hohs, get_all_religions, create_religion, get_all_roof_types, \
    create_roof_type, get_all_sewage_types, create_sewage_type, get_all_technical_skills, create_technical_skill, \
    get_all_toilet_types, create_toilet_type, get_all_vehicle_types, create_vehicle_type, get_all_wards, create_ward, \
    get_all_water_sources, create_water_source, get_all_margas, create_marga, get_all_death_reasons, \
    create_death_reason, get_all_business_types, get_all_vaccine_names, create_vaccine_name, create_house_damage_status, \
    get_all_house_damage_statuses, get_all_bastis_by_ward


def create_setting(request):
    context = dict()
    local_levels = get_all_local_levels()
    return render(request, 'app/backend/settings/ward/create.html', {'local_levels': local_levels})


# household_animal Type
def animal_type(request):
    animals = get_all_animal_types()
    return render(request, 'app/backend/settings/animal_type/index.html', {'animals': animals})


def animal_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/animal_type/create.html')
    data = request.POST
    form = AnimalTypeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        animal = create_animal_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [animal])
            return JsonResponse(data, safe=False)

        messages.success(request, 'household_animal Type created successfully')
        return redirect('setting.animal_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create household_animal Type')
        #     return redirect('setting.animal_type.create')
    messages.error(request, 'Invalid Form')
    return redirect('setting.animal_type.create')


def delete_animal(request, id):
    animal = AnimalType.objects.get(pk=id)
    if request.method == "GET":
        animal.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.animal_type')

    return render(request, 'app/backend/settings/animal_type/index.html', {'animals': animal})


def edit_animal(request, id):
    animals = AnimalType.objects.get(pk=id)
    return render(request, 'app/backend/settings/animal_type/edit.html', {'animals': animals})


def update_animal(request, id):
    data = request.POST
    animal = AnimalType.objects.get(pk=id)
    # if data['name']:
    animal.name = data['name']
    animal.save()
    return redirect('setting.animal_type')


# Basti
def basti(request):
    bastis = get_all_bastis()
    return render(request, 'app/backend/settings/basti/index.html', {'bastis': bastis})


def basti_create(request):
    wards = get_all_wards()
    if request.method == 'GET':
        return render(request, 'app/backend/settings/basti/create.html', {'wards': wards})

    form = BastiForm(request.POST)
    if form.is_valid():
        # try:
        create_basti(form.cleaned_data)
        messages.success(request, 'Basti created successfully')
        return redirect('setting.basti.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Basti')
        #     return redirect('setting.basti.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.basti.create')


def delete_basti(request, id):
    basti = Basti.objects.get(pk=id)
    if request.method == "GET":
        basti.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.basti_name')

    return render(request, 'app/backend/settings/basti/index.html', {'bastis': basti})


def edit_basti(request, id):
    wards = get_all_wards()
    bastis = Basti.objects.get(pk=id)
    return render(request, 'app/backend/settings/basti/edit.html', {'bastis': bastis, 'wards': wards})


def update_basti(request, id):
    data = request.POST
    basti = Basti.objects.get(pk=id)
    if data['name']:
        basti.name = data['name']
        basti.ward_id = data['ward']
    basti.save()
    return redirect('setting.basti_name')


# Business Type
def business_type(request):
    businesses = get_all_business_types()
    return render(request, 'app/backend/settings/business_type/index.html', {'businesses': businesses})


def business_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/business_type/create.html')

    data = request.POST
    form = BusinessTypeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        business = create_business_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [business])
            return JsonResponse(data, safe=False)
        messages.success(request, 'Business Type created successfully')
        return redirect('setting.business_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create business type')
        #     return redirect('setting.basti.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.business_type.create')


def delete_business_type(request, id):
    business = BusinessType.objects.get(pk=id)
    if request.method == "GET":
        business.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.business_type')
    return render(request, 'app/backend/settings/business_type/index.html', {'businesses': business})


def edit_business_type(request, id):
    businesses = BusinessType.objects.get(pk=id)
    return render(request, 'app/backend/settings/business_type/edit.html', {'businesses': businesses})


def update_business_type(request, id):
    data = request.POST
    business = BusinessType.objects.get(pk=id)
    if data['name']:
        business.name = data['name']
    business.save()
    return redirect('setting.business_type')


# Cooking Fuel
def cooking_fuel(request):
    cooking_fuels = get_all_cooking_fuels()
    return render(request, 'app/backend/settings/cooking_fuel/index.html', {'cooking_fuels': cooking_fuels})


def cooking_fuel_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/cooking_fuel/create.html')

    data = request.POST
    form = CookingFuelForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        cooking = create_cooking_fuel(data)
        if request.is_ajax():
            data = serializers.serialize('json', [cooking])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Cooking Fuel created successfully')
        return redirect('setting.cooking_fuel.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Cooking Fuel')
        #     return redirect('setting.cooking_fuel.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.cooking_fuel.create')


def delete_cooking_fuel(request, id):
    cooking_fuel = CookingFuel.objects.get(pk=id)
    if request.method == "GET":
        cooking_fuel.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.cooking_fuel')

    return render(request, 'app/backend/settings/cooking_fuel/index.html', {'cooking_fuels': cooking_fuel})


def edit_cooking_fuel(request, id):
    cooking_fuel = CookingFuel.objects.get(pk=id)
    return render(request, 'app/backend/settings/cooking_fuel/edit.html', {'cooking_fuels': cooking_fuel})


def update_cooking_fuel(request, id):
    data = request.POST
    cooking_fuel= CookingFuel.objects.get(pk=id)
    if data['name']:
        cooking_fuel.name = data['name']
    cooking_fuel.save()
    return redirect('setting.cooking_fuel')


# Country
def country(request):
    countries = get_all_countries()
    return render(request, 'app/backend/settings/country/index.html', {'countries': countries})


def country_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/country/create.html')

    data = request.POST
    form = CountryForm(data)
    if form.is_valid():
        data = form.cleaned_data
        country = create_country(data)
        if request.is_ajax():
            data = serializers.serialize('json', [country])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Country Name created successfully')
        return redirect('setting.country.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create country')
        #     return redirect('setting.country.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.country.create')


def delete_country(request, id):
    country = Country.objects.get(pk=id)
    if request.method == "GET":
        country.delete()
        return redirect('setting.country')

    return render(request, 'app/backend/settings/country/index.html', {'countries': country})


def edit_country(request, id):
    country = Country.objects.get(pk=id)
    return render(request, 'app/backend/settings/country/edit.html', {'countries': country})


def update_country(request, id):
    data = request.POST
    country = Country.objects.get(pk=id)
    if data['name']:
        country.name = data['name']
    country.save()
    return redirect('setting.country')


# Death Reason
def death_reason(request):
    death_reasons = get_all_death_reasons()
    return render(request, 'app/backend/settings/death_reason/index.html', {'death_reasons': death_reasons})


def death_reason_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/death_reason/create.html')

    data = request.POST
    form = DeathReasonForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        death_reason = create_death_reason(data)
        if request.is_ajax():
            data = serializers.serialize('json', [death_reason])  # Convert single model to json before response
            return JsonResponse(data, safe=False)

        messages.success(request, 'Death Reason created successfully')
        return redirect('setting.death_reason.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Death Reason')
        #     return redirect('setting.death_reason.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.death_reason.create')


def delete_death_reason(request, id):
    death_reason = DeathReason.objects.get(pk=id)
    if request.method == "GET":
        death_reason.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.death_reason')

    return render(request, 'app/backend/settings/death_reason/index.html', {'death_reasons': death_reason})


def edit_death_reason(request, id):
    death_reason = DeathReason.objects.get(pk=id)
    return render(request, 'app/backend/settings/death_reason/edit.html', {'death_reasons': death_reason})


def update_death_reason(request, id):
    data = request.POST
    death_reason = DeathReason.objects.get(pk=id)
    if data['name']:
        death_reason.name = data['name']
    death_reason.save()
    return redirect('setting.death_reason')


# Disability Type
def disability_type(request):
    disability_types = get_all_disability_types()
    return render(request, 'app/backend/settings/disability_type/index.html', {'disability_types': disability_types})


def disability_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/disability_type/create.html')
    data = request.POST
    form = DisabilityTypeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        disability_type = create_disability_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [disability_type])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Disability Type created successfully')
        return redirect('setting.disability_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Disability Type')
        #     return redirect('setting.disability_type.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.disability_type.create')


def delete_disability_type(request, id):
    disability_type = DisabilityType.objects.get(pk=id)
    if request.method == "GET":
        disability_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.disability_type')

    return render(request, 'app/backend/settings/disability_type/index.html', {'disability_types': disability_type})


def edit_disability_type(request, id):
    disability_type = DisabilityType.objects.get(pk=id)
    return render(request, 'app/backend/settings/disability_type/edit.html', {'disability_types': disability_type})


def update_disability_type(request, id):
    data = request.POST
    disability_type = DisabilityType.objects.get(pk=id)
    if data['name']:
        disability_type.name = data['name']
    disability_type.save()
    return redirect('setting.disability_type')


# Disaster Type
def disaster_name(request):
    disaster_names = get_all_disaster_names()
    return render(request, 'app/backend/settings/disaster/index.html', {'disaster_names': disaster_names})


def disaster_name_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/disaster/create.html')

    form = DisasterForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        disaster = create_disaster_name(data)
        if request.is_ajax():
            data = serializers.serialize('json', [disaster])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Disaster Name created successfully')
        return redirect('setting.disaster_name.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Disaster Name')
        #     return redirect('setting.disaster_name.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.disaster_name.create')


def delete_disaster(request, id):
    disaster = Disaster.objects.get(pk=id)
    if request.method == "GET":
        disaster.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.disaster_name')

    return render(request, 'app/backend/settings/disaster/index.html', {'disaster_names': disaster})


def edit_disaster(request, id):
    disaster = Disaster.objects.get(pk=id)
    return render(request, 'app/backend/settings/disaster/edit.html', {'disaster_names': disaster})


def update_disaster(request, id):
    data = request.POST
    disaster = Disaster.objects.get(pk=id)
    if data['name']:
        disaster.name = data['name']
    disaster.save()
    return redirect('setting.disaster_name')


# Education Level
def education_level(request):
    education_levels = get_all_education_levels()
    return render(request, 'app/backend/settings/education_level/index.html', {'education_levels': education_levels})


def education_level_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/education_level/create.html')

    form = EducationLevelForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        education_level = create_education_level(data)
        if request.is_ajax():
            data = serializers.serialize('json', [education_level])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Education Level created successfully')
        return redirect('setting.education_level.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Education Level')
        #     return redirect('setting.education_level.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.education_level.create')


def delete_education_level(request, id):
    education_level = EducationLevel.objects.get(pk=id)
    if request.method == "GET":
        education_level.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.education_level')

    return render(request, 'app/backend/settings/education_level/index.html', {'education_levels': education_level})


def edit_education_level(request, id):
    education_level = EducationLevel.objects.get(pk=id)
    return render(request, 'app/backend/settings/education_level/edit.html', {'education_levels': education_level})


def update_education_level(request, id):
    data = request.POST
    education_level = EducationLevel.objects.get(pk=id)
    if data['name']:
        education_level.name = data['name']
    education_level.save()
    return redirect('setting.education_level')


# Education Status
def education_status(request):
    education_statuses = get_all_education_statuses()
    return render(request, 'app/backend/settings/education_status/index.html', {'education_statuses': education_statuses})


def education_status_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/education_status/create.html')

    form = EducationStatusForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        education_status = create_education_status(data)
        if request.is_ajax():
            data = serializers.serialize('json', [education_status])
            return JsonResponse(data, safe=False)
        messages.success(request, 'Education Status created successfully')
        return redirect('setting.education_status.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Education Status')
        #     return redirect('setting.education_status.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.education_status.create')


def delete_education_status(request, id):
    education_status = EducationStatus.objects.get(pk=id)
    if request.method == "GET":
        education_status.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.education_status')

    return render(request, 'app/backend/settings/education_status/index.html', {'education_statuses': education_status})


def edit_education_status(request, id):
    education_status = EducationStatus.objects.get(pk=id)
    return render(request, 'app/backend/settings/education_status/edit.html', {'education_statuses': education_status})


def update_education_status(request, id):
    data = request.POST
    education_status = EducationStatus.objects.get(pk=id)
    if data['name']:
        education_status.name = data['name']
    education_status.save()
    return redirect('setting.education_status')


# Facility
def facility(request):
    facilities = get_all_facilities()
    return render(request, 'app/backend/settings/facility/index.html', {'facilities': facilities})


def facility_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/facility/create.html')
    data = request.POST
    form = FacilityForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        facility = create_facility(data)
        if request.is_ajax():
            data = serializers.serialize('json', [facility])
            return JsonResponse (data, safe=False)

        messages.success(request, 'Facility created successfully')
        return redirect('setting.facility.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Facility')
        #     return redirect('setting.facility.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.facility.create')


def delete_facility(request, id):
    facility = Facility.objects.get(pk=id)
    if request.method == "GET":
        facility.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.facility')

    return render(request, 'app/backend/settings/facility/index.html', {'facilities': facility})


def edit_facility(request, id):
    facility = Facility.objects.get(pk=id)
    return render(request, 'app/backend/settings/facility/edit.html', {'facilities': facility})


def update_facility(request, id):
    data = request.POST
    facility = Facility.objects.get(pk=id)
    if data['name']:
        facility.name = data['name']
    facility.save()
    return redirect('setting.facility')


# Festival
def festival(request):
    festivals = get_all_festivals()
    return render(request, 'app/backend/settings/festival/index.html', {'festivals': festivals})


def festival_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/festival/create.html')

    data = request.POST
    form = FestivalForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        festival = create_festival(data)
        if request.is_ajax():
            data = serializers.serialize('json' [festival])
            return JsonResponse (data, safe=False)

        messages.success(request, 'Festival created successfully')
        return redirect('setting.festival.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Festival')
        #     return redirect('setting.festival.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.festival.create')


def delete_festival(request, id):
    festival = Festival.objects.get(pk=id)
    if request.method == "GET":
        festival.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.festival')

    return render(request, 'app/backend/settings/festival/index.html', {'festivals': festival})


def edit_festival(request, id):
    festival = Festival.objects.get(pk=id)
    return render(request, 'app/backend/settings/festival/edit.html', {'festivals': festival})


def update_festival(request, id):
    data = request.POST
    festival = Festival.objects.get(pk=id)
    if data['name']:
        festival.name = data['name']
    festival.save()
    return redirect('setting.festival')


# Foreign Reason
def foreign_reason(request):
    foreign_reasons = get_all_foreign_reasons()
    return render(request, 'app/backend/settings/foreign_reason/index.html', {'foreign_reasons': foreign_reasons})


def foreign_reason_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/foreign_reason/create.html')
    data = request.POST
    form = ForeignReasonForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        foreign_reason = create_foreign_reason(data)
        if request.is_ajax():
            data = serializers.serialize('json', [foreign_reason])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Foreign Reason created successfully')
        return redirect('setting.foreign_reason.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Foreign Reason')
        #     return redirect('setting.foreign_reason.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.foreign_reason.create')


def delete_foreign_reason(request, id):
    foreign_reason = ForeignReason.objects.get(pk=id)
    if request.method == "GET":
        foreign_reason.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.foreign_reason')

    return render(request, 'app/backend/settings/foreign_reason/index.html', {'foreign_reasons': foreign_reason})


def edit_foreign_reason(request, id):
    foreign_reason = ForeignReason.objects.get(pk=id)
    return render(request, 'app/backend/settings/foreign_reason/edit.html', {'foreign_reasons': foreign_reason})


def update_foreign_reason(request, id):
    data = request.POST
    foreign_reason = ForeignReason.objects.get(pk=id)
    if data['name']:
        foreign_reason.name = data['name']
    foreign_reason.save()
    return redirect('setting.foreign_reason')


# Garbage Management
def garbage_management(request):
    garbage_managements = get_all_garbage_managements()
    return render(request, 'app/backend/settings/garbage_management/index.html', {'garbage_managements': garbage_managements})


def garbage_management_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/garbage_management/create.html')

    data = request.POST
    form = GarbageManagementForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        garbage = create_garbage_management(data)
        if request.is_ajax():
            data = serializers.serialize('json', [garbage])
            return JsonResponse (data, safe=False)
        
        messages.success(request, 'Garbage Management Option created successfully')
        return redirect('setting.garbage_management.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Garbage Management')
        #     return redirect('setting.garbage_management.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.garbage_management.create')


def delete_garbage_management(request, id):
    garbage_management = GarbageManagement.objects.get(pk=id)
    if request.method == "GET":
        garbage_management.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.garbage_management')

    return render(request, 'app/backend/settings/garbage_management/index.html', {'garbage_managements': garbage_management})


def edit_garbage_management(request, id):
    garbage_management = GarbageManagement.objects.get(pk=id)
    return render(request, 'app/backend/settings/garbage_management/edit.html', {'garbage_managements': garbage_management})


def update_garbage_management(request, id):
    data = request.POST
    garbage_management = GarbageManagement.objects.get(pk=id)
    if data['name']:
        garbage_management.name = data['name']
    garbage_management.save()
    return redirect('setting.garbage_management')


# House Damage Status
def house_damage_status(request):
    house_damage_statuses = get_all_house_damage_statuses()
    return render(request, 'app/backend/settings/house_damage_status/index.html',
                  {'house_damage_statuses': house_damage_statuses})


def house_damage_status_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/house_damage_status/create.html')
    data = request.POST
    form = HouseDamageStatusForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        create_house_damage_status(data)
        messages.success(request, 'House Damage Status Option created successfully')
        return redirect('setting.house_damage_status.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create House Damage Status')
        #     return redirect('setting.house_damage_status.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.house_damage_status.create')


def delete_house_damage_status(request, id):
    house_damage_status = HouseDamageStatus.objects.get(pk=id)
    if request.method == "GET":
        house_damage_status.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.house_damage_status')

    return render(request, 'app/backend/settings/house_damage_status/index.html', {'house_damage_statuses': house_damage_status})


def edit_house_damage_status(request, id):
    house_damage_status = HouseDamageStatus.objects.get(pk=id)
    return render(request, 'app/backend/settings/house_damage_status/edit.html', {'house_damage_statuses': house_damage_status})


def update_house_damage_status(request, id):
    data = request.POST
    house_damage_status = HouseDamageStatus.objects.get(pk=id)
    if data['name']:
        house_damage_status.name = data['name']
    house_damage_status.save()
    return redirect('setting.house_damage_status')


# House Type
def house_type(request):
    house_types = get_all_house_types()
    return render(request, 'app/backend/settings/house_type/index.html', {'house_types': house_types})


def house_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/house_type/create.html')

    data = request.POST
    form = HouseTypeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        house_type = create_house_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [house_type])
            return JsonResponse(data, safe=False)

        messages.success(request, 'House Type created successfully')
        return redirect('setting.house_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create House Type')
        #     return redirect('setting.house_type.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.house_type.create')


def delete_house_type(request, id):
    house_type = HouseType.objects.get(pk=id)
    if request.method == "GET":
        house_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.house_type')

    return render(request, 'app/backend/settings/house_type/index.html', {'house_types': house_type})


def edit_house_type(request, id):
    house_type = HouseType.objects.get(pk=id)
    return render(request, 'app/backend/settings/house_type/edit.html', {'house_types': house_type})


def update_house_type(request, id):
    data = request.POST
    house_type = HouseType.objects.get(pk=id)
    if data['name']:
        house_type.name = data['name']
    house_type.save()
    return redirect('setting.house_type')


# Income Source
def income_source(request):
    income_sources = get_all_income_sources()
    return render(request, 'app/backend/settings/income_source/index.html', {'income_sources': income_sources})


def income_source_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/income_source/create.html')

    data = request.POST
    form = IncomeSourceForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        income = create_income_source(data)
        if request.is_ajax():
            data = serializers.serialize('json', [income])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Income Source created successfully')
        return redirect('setting.income_source.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Income Source')
        #     return redirect('setting.income_source.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.income_source.create')


def delete_income_source(request, id):
    income_source = IncomeSource.objects.get(pk=id)
    if request.method == "GET":
        income_source.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.income_source')

    return render(request, 'app/backend/settings/income_source/index.html', {'income_sources': income_source})


def edit_income_source(request, id):
    income_source = IncomeSource.objects.get(pk=id)
    return render(request, 'app/backend/settings/income_source/edit.html', {'income_sources': income_source})


def update_income_source(request, id):
    data = request.POST
    income_source = IncomeSource.objects.get(pk=id)
    if data['name']:
        income_source.name = data['name']
    income_source.save()
    return redirect('setting.income_source')


# Jaati
def jaati(request):
    jaatis = get_all_jaatis()
    return render(request, 'app/backend/settings/jaati/index.html', {'jaati': jaatis})


def jaati_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/jaati/create.html')
    data = request.POST
    form = JaatiForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        jaati = create_jaati(data)
        if request.is_ajax():
            data = serializers.serialize('json', [jaati])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Ethnics created successfully')
        return redirect('setting.jaati.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Ethnics')
        #     return redirect('setting.jaati.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.jaati.create')


def delete_jaati(request, id):
    jaati = Jaati.objects.get(pk=id)
    if request.method == "GET":
        jaati.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.jaati')

    return render(request, 'app/backend/settings/jaati/index.html', {'jaati': jaati})


def edit_jaati(request, id):
    jaati = Jaati.objects.get(pk=id)
    return render(request, 'app/backend/settings/jaati/edit.html', {'jaati': jaati})


def update_jaati(request, id):
    data = request.POST
    jaati = Jaati.objects.get(pk=id)
    if data['name']:
        jaati.name = data['name']
    jaati.save()
    return redirect('setting.jaati')


# Land Type
def land_type(request):
    land_types = get_all_land_types()
    return render(request, 'app/backend/settings/land_type/index.html', {'land_types': land_types})


def land_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/land_type/create.html')

    form = LandTypeForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        land_type = create_land_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [land_type])
            return JsonResponse(data, safe=False)
        messages.success(request, 'Land Type created successfully')
        return redirect('setting.land_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create BasLand Typeti')
        #     return redirect('setting.land_type.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.land_type.create')


def delete_land_type(request, id):
    land_type = LandType.objects.get(pk=id)
    if request.method == "GET":
        land_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.land_type')

    return render(request, 'app/backend/settings/land_type/index.html', {'land_types': land_type})


def edit_land_type(request, id):
    land_type = LandType.objects.get(pk=id)
    return render(request, 'app/backend/settings/land_type/edit.html', {'land_types': land_type})


def update_land_type(request, id):
    data = request.POST
    land_type = LandType.objects.get(pk=id)
    if data['name']:
        land_type.name = data['name']
    land_type.save()
    return redirect('setting.land_type')


# Light Fuel
def light_fuel(request):
    light_fuels = get_all_light_fuels()
    return render(request, 'app/backend/settings/light_fuel/index.html', {'light_fuels': light_fuels})


def light_fuel_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/light_fuel/create.html')
    data = request.POST
    form = LightFuelForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        light = create_light_fuel(data)
        if request.is_ajax():
            data = serializers.serialize('json', [light])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Light Fuel created successfully')
        return redirect('setting.light_fuel.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Light Fuel')
        #     return redirect('setting.light_fuel.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.light_fuel.create')


def delete_light_fuel(request, id):
    light_fuel = LightFuel.objects.get(pk=id)
    if request.method == "GET":
        light_fuel.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.light_fuel')

    return render(request, 'app/backend/settings/light_fuel/index.html', {'light_fuels': light_fuel})


def edit_light_fuel(request, id):
    light_fuel = LightFuel.objects.get(pk=id)
    return render(request, 'app/backend/settings/light_fuel/edit.html', {'light_fuels': light_fuel})


def update_light_fuel(request, id):
    data = request.POST
    light_fuel = LightFuel.objects.get(pk=id)
    if data['name']:
        light_fuel.name = data['name']
    light_fuel.save()
    return redirect('setting.light_fuel')


# Main Occupation
def main_occupation(request):
    main_occupations = get_all_main_occupations()
    return render(request, 'app/backend/settings/main_occupation/index.html', {'main_occupations': main_occupations})


def main_occupation_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/main_occupation/create.html')
    data = request.POST
    form = MainOccupationForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        main_occupaion = create_main_occupation(data)
        if request.is_ajax():
            data = serializers.serialize('json', [main_occupaion])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Main Occupation created successfully')
        return redirect('setting.main_occupation.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Main Occupation ')
        #     return redirect('setting.main_occupation.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.main_occupation.create')


def delete_main_occupation(request, id):
    main_occupation = MainOccupation.objects.get(pk=id)
    if request.method == "GET":
        main_occupation.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.main_occupation')

    return render(request, 'app/backend/settings/main_occupation/index.html', {'main_occupations': main_occupation})


def edit_main_occupation(request, id):
    main_occupation = MainOccupation.objects.get(pk=id)
    return render(request, 'app/backend/settings/main_occupation/edit.html', {'main_occupations': main_occupation})


def update_main_occupation(request, id):
    data = request.POST
    main_occupation = MainOccupation.objects.get(pk=id)
    if data['name']:
        main_occupation.name = data['name']
    main_occupation.save()
    return redirect('setting.main_occupation')


# Marga
def marga(request):
    margas = get_all_margas()
    return render(request, 'app/backend/settings/marga/index.html', {'margas': margas})


def marga_create(request):
    bastis = get_all_bastis()
    if request.method == 'GET':
        return render(request, 'app/backend/settings/marga/create.html', {'bastis': bastis})

    data = request.POST
    form = MargaForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        marga = create_marga(data)
        if request.is_ajax():
            data = serializers.serialize('json', [marga])  # Convert single model to json before response
            return JsonResponse(data, safe=False)

        messages.success(request, 'Marga created successfully')
        return redirect('setting.marga.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Marga')
        #     return redirect('setting.marga.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.marga.create')


def delete_marga(request, id):
    marga = Marga.objects.get(pk=id)
    if request.method == "GET":
        marga.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.marga')

    return render(request, 'app/backend/settings/marga/index.html', {'margas': marga})


def edit_marga(request, id):
    marga = Marga.objects.get(pk=id)
    return render(request, 'app/backend/settings/marga/edit.html', {'margas': marga})


def update_marga(request, id):
    data = request.POST
    marga = Marga.objects.get(pk=id)
    if data['name']:
        marga.name = data['name']
    marga.save()
    return redirect('setting.marga')


# Marital Status
def marital_status(request):
    marital_statuses = get_all_marital_statuses()
    return render(request, 'app/backend/settings/marital_status/index.html', {'marital_statuses': marital_statuses})


def marital_status_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/marital_status/create.html')

    form = MaritalStatusForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        marital_status = create_marital_status(data)
        if request.is_ajax():
            data = serializers.serialize('json', [marital_status])  # Convert single model to json before response
            return JsonResponse(data, safe=False)

        messages.success(request, 'Marital Status created successfully')
        return redirect('setting.marital_status.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Marital Status')
        #     return redirect('setting.marital_status.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.marital_status.create')


def delete_marital_status(request, id):
    marital_status = MaritalStatus.objects.get(pk=id)
    if request.method == "GET":
        marital_status.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.marital_status')

    return render(request, 'app/backend/settings/marital_status/index.html', {'marital_statuses': marital_status})


def edit_marital_status(request, id):
    marital_status = MaritalStatus.objects.get(pk=id)
    return render(request, 'app/backend/settings/marital_status/edit.html', {'marital_statuses': marital_status})


def update_marital_status(request, id):
    data = request.POST
    marital_status = MaritalStatus.objects.get(pk=id)
    if data['name']:
        marital_status.name = data['name']
    marital_status.save()
    return redirect('setting.marital_status')


# Mother Tongue
def mother_tongue(request):
    mother_tongues = get_all_mother_tongues()
    return render(request, 'app/backend/settings/mother_tongue/index.html', {'mother_tongues': mother_tongues})


def mother_tongue_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/mother_tongue/create.html')
    data = request.POST
    form = MotherTongueForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        mother_tongue = create_mother_tongue(data)
        if request.is_ajax():
            data = serializers.serialize('json', [mother_tongue])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Mother Tongue created successfully')
        return redirect('setting.mother_tongue.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Mother Tongue')
        #     return redirect('setting.mother_tongue.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.mother_tongue.create')


def delete_mother_tongue(request, id):
    mother_tongue = MotherTongue.objects.get(pk=id)
    if request.method == "GET":
        mother_tongue.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.mother_tongue')

    return render(request, 'app/backend/settings/mother_tongue/index.html', {'mother_tongues': mother_tongue})


def edit_mother_tongue(request, id):
    mother_tongue = MotherTongue.objects.get(pk=id)
    return render(request, 'app/backend/settings/mother_tongue/edit.html', {'mother_tongues': mother_tongue})


def update_mother_tongue(request, id):
    data = request.POST
    mother_tongue = MotherTongue.objects.get(pk=id)
    if data['name']:
        mother_tongue.name = data['name']
    mother_tongue.save()
    return redirect('setting.mother_tongue')


# Relation With HouseHead
def relation_with_hoh(request):
    relation_with_hoh = get_all_relation_with_hohs()
    return render(request, 'app/backend/settings/relation_with_hoh/index.html', {'relation_with_hoh': relation_with_hoh})


def relation_with_hoh_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/relation_with_hoh/create.html')
    data = request.POST
    form = RelationWithHohForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        relation = create_relation_with_hoh(data)
        if request.is_ajax():
            data = serializers.serialize('json', [relation])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Relation With HouseHead created successfully')
        return redirect('setting.relation_with_hoh.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Relation With HouseHead')
        #     return redirect('setting.relation_with_hoh.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.relation_with_hoh.create')


def delete_relation_with_hoh(request, id):
    relation_with_hoh = RelationWithHoh.objects.get(pk=id)
    if request.method == "GET":
        relation_with_hoh.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.relation_with_hoh')

    return render(request, 'app/backend/settings/relation_with_hoh/index.html', {'relation_with_hoh': relation_with_hoh})


def edit_relation_with_hoh(request, id):
    relation_with_hoh = RelationWithHoh.objects.get(pk=id)
    return render(request, 'app/backend/settings/relation_with_hoh/edit.html', {'relation_with_hoh': relation_with_hoh})


def update_relation_with_hoh(request, id):
    data = request.POST
    relation_with_hoh = RelationWithHoh.objects.get(pk=id)
    if data['name']:
        relation_with_hoh.name = data['name']
    relation_with_hoh.save()
    return redirect('setting.relation_with_hoh')


# Religion
def religion(request):
    religions = get_all_religions()
    return render(request, 'app/backend/settings/religion/index.html', {'religions': religions})


def religion_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/religion/create.html')

    data = request.POST
    form = ReligionForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        religion = create_religion(data)
        if request.is_ajax():
            data = serializers.serialize('json', [religion])  # Convert single model to json before response
            return JsonResponse(data, safe=False)

    messages.success(request, 'Religion created successfully')
    return redirect('setting.religion.create')
    # except Exception:
    #     if request.is_ajax():
    #         return HttpResponse('Failed')
    #     messages.error(request, 'Can not create Religion')
    #     return redirect('setting.religion.create')
    messages.error(request, ' Invalid Form')
    return redirect('setting.religion.create')


def delete_religion(request, id):
    religion = Religion.objects.get(pk=id)
    if request.method == "GET":
        religion.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.religion')

    return render(request, 'app/backend/settings/religion/index.html', {'religions': religion})


def edit_religion(request, id):
    religion = Religion.objects.get(pk=id)
    return render(request, 'app/backend/settings/religion/edit.html', {'religions': religion})


def update_religion(request, id):
    data = request.POST
    religion = Religion.objects.get(pk=id)
    if data['name']:
        religion.name = data['name']
    religion.save()
    return redirect('setting.religion')


# Roof Type
def roof_type(request):
    roof_types = get_all_roof_types()
    return render(request, 'app/backend/settings/roof_type/index.html', {'roof_types': roof_types})


def roof_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/roof_type/create.html')
    data = request.POST
    form = RoofTypeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        roof_type = create_roof_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [roof_type])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Roof Type created successfully')
        return redirect('setting.roof_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Roof Type')
        #     return redirect('setting.roof_type.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.roof_type.create')


def delete_roof_type(request, id):
    roof_type = RoofType.objects.get(pk=id)
    if request.method == "GET":
        roof_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.roof_type')

    return render(request, 'app/backend/settings/roof_type/index.html', {'roof_types': roof_type})


def edit_roof_type(request, id):
    roof_type = RoofType.objects.get(pk=id)
    return render(request, 'app/backend/settings/roof_type/edit.html', {'roof_types': roof_type})


def update_roof_type(request, id):
    data = request.POST
    roof_type = RoofType.objects.get(pk=id)
    if data['name']:
        roof_type.name = data['name']
    roof_type.save()
    return redirect('setting.roof_type')


# Sewage Type
def sewage_type(request):
    sewage_types = get_all_sewage_types()
    return render(request, 'app/backend/settings/sewage_type/index.html', {'sewage_types': sewage_types})


def sewage_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/sewage_type/create.html')

    form = SewageTypeForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        sewage_type = create_sewage_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [sewage_type])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Sewage Type created successfully')
        return redirect('setting.sewage_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Sewage Type')
        #     return redirect('setting.sewage_type.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.sewage_type.create')


def delete_sewage_type(request, id):
    sewage_type = SewageType.objects.get(pk=id)
    if request.method == "GET":
        sewage_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.sewage_type')

    return render(request, 'app/backend/settings/sewage_type/index.html', {'sewage_types': sewage_type})


def edit_sewage_type(request, id):
    sewage_type = SewageType.objects.get(pk=id)
    return render(request, 'app/backend/settings/sewage_type/edit.html', {'sewage_type': sewage_type})


def update_sewage_type(request, id):
    data = request.POST
    sewage_type = SewageType.objects.get(pk=id)
    if data['name']:
        sewage_type.name = data['name']
    sewage_type.save()
    return redirect('setting.sewage_type')


# Technical Skill
def technical_skill(request):
    technical_skills = get_all_technical_skills()
    return render(request, 'app/backend/settings/technical_skill/index.html', {'technical_skills': technical_skills})


def technical_skill_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/technical_skill/create.html')
    data = request.POST
    form = TechnicalSkillForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        technical_skill = create_technical_skill(data)
        if request.is_ajax():
            data = serializers.serialize('json', [technical_skill])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Technical Skill created successfully')
        return redirect('setting.technical_skill.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create Technical Skill')
        #     return redirect('setting.technical_skill.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.technical_skill.create')


def delete_technical_skill(request, id):
    technical_skill = TechnicalSkill.objects.get(pk=id)
    if request.method == "GET":
        technical_skill.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.technical_skill')

    return render(request, 'app/backend/settings/technical_skill/index.html', {'technical_skills': technical_skill})


def edit_technical_skill(request, id):
    technical_skill = TechnicalSkill.objects.get(pk=id)
    return render(request, 'app/backend/settings/technical_skill/edit.html', {'technical_skills': technical_skill})


def update_technical_skill(request, id):
    data = request.POST
    technical_skill = TechnicalSkill.objects.get(pk=id)
    if data['name']:
        technical_skill.name = data['name']
    technical_skill.save()
    return redirect('setting.technical_skill')


# Toilet Type
def toilet_type(request):
    toilet_types = get_all_toilet_types()
    return render(request, 'app/backend/settings/toilet_type/index.html', {'toilet_types': toilet_types})


def toilet_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/toilet_type/create.html')

    form = ToiletTypeForm(request.POST)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        toilet_type = create_toilet_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [toilet_type])
            return JsonResponse(data, safe=False)
        messages.success(request, 'Toilet Type created successfully')
        return redirect('setting.toilet_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create toilet type')
        #     return redirect('setting.disaster_name.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.toilet_type.create')


def delete_toilet_type(request, id):
    toilet_type = ToiletType.objects.get(pk=id)
    if request.method == "GET":
        toilet_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.toilet_type')

    return render(request, 'app/backend/settings/toilet_type/index.html', {'toilet_types': toilet_type})


def edit_toilet_type(request, id):
    toilet_type = ToiletType.objects.get(pk=id)
    return render(request, 'app/backend/settings/toilet_type/edit.html', {'toilet_types': toilet_type})


def update_toilet_type(request, id):
    data = request.POST
    toilet_type = ToiletType.objects.get(pk=id)
    if data['name']:
        toilet_type.name = data['name']
    toilet_type.save()
    return redirect('setting.toilet_type')


# Vaccine Name
def vaccine_name(request):
    vaccine_names = get_all_vaccine_names()
    return render(request, 'app/backend/settings/vaccine_name/index.html', {'vaccine_names': vaccine_names})


def vaccine_name_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/vaccine_name/create.html')

    data = request.POST
    form = VaccineNameForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        vaccine = create_vaccine_name(data)
        if request.is_ajax():
            data = serializers.serialize('json', [vaccine])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Vaccine Name created successfully')
        return redirect('setting.vaccine_name.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create vaccine name')
        #     return redirect('setting.disaster_name.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.vaccine_name.create')


def delete_vaccine(request, id):
    vaccine = VaccineName.objects.get(pk=id)
    if request.method == "GET":
        vaccine.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.vaccine_name')

    return render(request, 'app/backend/settings/vaccine_name/index.html', {'vaccine_names': vaccine})


def edit_vaccine(request, id):
    vaccine = VaccineName.objects.get(pk=id)
    return render(request, 'app/backend/settings/vaccine_name/edit.html', {'vaccine_names': vaccine})


def update_vaccine(request, id):
    data = request.POST
    vaccine = VaccineName.objects.get(pk=id)
    if data['name']:
        vaccine.name = data['name']
    vaccine.save()
    return redirect('setting.vaccine_name')


# Vehicle Type
def vehicle_type(request):
    vehicle_types = get_all_vehicle_types()
    return render(request, 'app/backend/settings/vehicle_type/index.html', {'vehicle_types': vehicle_types})


def vehicle_type_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/vehicle_type/create.html')

    data = request.POST
    form = VehicleTypeForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        vehicle = create_vehicle_type(data)
        if request.is_ajax():
            data = serializers.serialize('json', [vehicle])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Vehicle Type created successfully')
        return redirect('setting.vehicle_type.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create vehicle type')
        #     return redirect('setting.disaster_name.create')
        messages.error(request, 'Invalid Form')
        return redirect('setting.vehicle_type.create')


def delete_vehicle_type(request, id):
    vehicle_type = VehicleType.objects.get(pk=id)
    if request.method == "GET":
        vehicle_type.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.vehicle_type')

    return render(request, 'app/backend/settings/vehicle_type/index.html', {'vehicle_types': vehicle_type})


def edit_vehicle_type(request, id):
    vehicle_type = VehicleType.objects.get(pk=id)
    return render(request, 'app/backend/settings/vehicle_type/edit.html', {'vehicle_types': vehicle_type})


def update_vehicle_type(request, id):
    data = request.POST
    vehicle_type = VehicleType.objects.get(pk=id)
    if data['name']:
        vehicle_type.name = data['name']
    vehicle_type.save()
    return redirect('setting.vehicle_type')


# Ward
def ward(request):
    wards = get_all_wards()
    return render(request, 'app/backend/settings/ward/index.html', {'wards': wards})


def get_basti_by_ward(request, id):
    if request.is_ajax():
        basti_by_ward = get_all_bastis_by_ward(id)
        data = serializers.serialize('json', basti_by_ward)
        return JsonResponse(data, safe=False)


def ward_create(request):
    local_levels = get_all_local_levels()
    if request.method == 'GET':
        return render(request, 'app/backend/settings/ward/create.html', {'local_levels': local_levels})
    data = request.POST
    form = WardForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        create_ward(data)
        messages.success(request, 'Ward created successfully')
        return redirect('setting.ward.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create ward')
        #     return redirect('setting.disaster_name.create')
        messages.error(request, 'Invalid Form ')
        return redirect('setting.ward.create')


def delete_ward(request, id):
    ward = Ward.objects.get(pk=id)
    if request.method == "GET":
        ward.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.ward')

    return render(request, 'app/backend/settings/ward/index.html', {'wards': ward})


def edit_ward(request, id):
    ward = Ward.objects.get(pk=id)
    return render(request, 'app/backend/settings/ward/edit.html', {'wards': ward})


def update_ward(request, id):
    data = request.POST
    ward = Ward.objects.get(pk=id)
    if data['name']:
        ward.name = data['name']
    ward.save()
    return redirect('setting.ward')


# Water Source
def water_source(request):
    water_sources = get_all_water_sources()
    return render(request, 'app/backend/settings/water_source/index.html', {'water_sources': water_sources})


def water_source_create(request):
    if request.method == 'GET':
        return render(request, 'app/backend/settings/water_source/create.html')
    data = request.POST
    form = WaterSourceForm(data)
    if form.is_valid():
        # try:
        data = form.cleaned_data
        water = create_water_source(data)
        if request.is_ajax():
            data = serializers.serialize('json', [water])
            return JsonResponse(data, safe=False)

        messages.success(request, 'Water Source created successfully')
        return redirect('setting.water_source.create')
        # except Exception:
        #     if request.is_ajax():
        #         return HttpResponse('Failed')
        #     messages.error(request, 'Can not create water source')
        #     return redirect('setting.disaster_name.create')
        messages.error(request, 'Invalid Form ')
        return redirect('setting.water_source.create')


def delete_water_source(request, id):
    water_source = WaterSource.objects.get(pk=id)
    if request.method == "GET":
        water_source.delete()
        messages.success(request, 'Data Deleted')
        return redirect('setting.water_source')

    return render(request, 'app/backend/settings/water_source/index.html', {'water_sources': water_source})


def edit_water_source(request, id):
    water_source = WaterSource.objects.get(pk=id)
    return render(request, 'app/backend/settings/water_source/edit.html', {'water_sources': water_source})


def update_water_source(request, id):
    data = request.POST
    water_source = WaterSource.objects.get(pk=id)
    if data['name']:
        water_source.name = data['name']
    water_source.save()
    return redirect('setting.water_source')

