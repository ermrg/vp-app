from app.models import DisabilityCard, Gender, Collector
from app.models.settings.animal_type import AnimalType
from app.models.settings.basti import Basti
from app.models.settings.business_type import BusinessType
from app.models.settings.cooking_fuel import CookingFuel
from app.models.settings.country import Country
from app.models.settings.death_reason import DeathReason
from app.models.settings.disability_type import DisabilityType
from app.models.settings.disaster import Disaster
from app.models.settings.education_level import EducationLevel
from app.models.settings.education_status import EducationStatus
from app.models.settings.facility import Facility
from app.models.settings.festival import Festival
from app.models.settings.foreign_reason import ForeignReason
from app.models.settings.garbage_management import GarbageManagement
from app.models.settings.house_damage_status import HouseDamageStatus
from app.models.settings.house_type import HouseType
# import model here


# household_animal Type
from app.models.settings.income_source import IncomeSource
from app.models.settings.jaati import Jaati
from app.models.settings.land_type import LandType
from app.models.settings.light_fuel import LightFuel
from app.models.settings.main_occupation import MainOccupation
from app.models.settings.marga import Marga
from app.models.settings.marital_status import MaritalStatus
from app.models.settings.mother_tongue import MotherTongue
from app.models.settings.relation_with_hoh import RelationWithHoh
from app.models.settings.religion import Religion
from app.models.settings.roof_type import RoofType
from app.models.settings.sewage_type import SewageType
from app.models.settings.technical_skill import TechnicalSkill
from app.models.settings.toilet_type import ToiletType
from app.models.settings.vaccine_name import VaccineName
from app.models.settings.vehicle_type import VehicleType
from app.models.settings.ward import Ward
from app.models.settings.water_source import WaterSource


def get_all_animal_types():
    return AnimalType.objects.filter(status=1)


def get_animal_type_by_id(id_):
    return AnimalType.objects.get(pk=id_)


def get_animal_type_by_name(name):
    return AnimalType.objects.filter(name=name).first()


def create_animal_type(data):
    animal_type = AnimalType()
    animal_type.name = data['name']
    animal_type.status = 1
    animal_type.save()
    return animal_type


# Basti
def get_all_bastis():
    return Basti.objects.filter(status=1)


def get_all_bastis_by_ward(ward_id):
    return Basti.objects.filter(ward_id=ward_id);


def get_basti_by_id(id_):
    return Basti.objects.get(pk=id_)


def get_basti_by_name(name):
    return Basti.objects.filter(name=name).first()


def create_basti(data):
    basti = Basti()
    basti.ward_id = data['ward']
    basti.name = data['name']
    basti.status = 1
    basti.save()
    return basti


# Business Type
def get_all_business_types():
    return BusinessType.objects.filter(status=1)


def get_business_type_by_id(id_):
    return BusinessType.objects.get(pk=id_)


def get_business_type_by_name(name):
    return BusinessType.objects.filter(name=name).first()


def create_business_type(data):
    business_type = BusinessType()
    business_type.name = data['name']
    business_type.status = 1
    business_type.save()
    return business_type


# Cooking Fuel
def get_all_cooking_fuels():
    return CookingFuel.objects.filter(status=1)


def get_cooking_fuel_by_id(id_):
    return CookingFuel.objects.get(pk=id_)


def get_cooking_fuel_by_name(name):
    return CookingFuel.objects.filter(name=name).first()


def create_cooking_fuel(data):
    cooking_fuel = CookingFuel()
    cooking_fuel.name = data['name']
    cooking_fuel.status = 1
    cooking_fuel.save()
    return cooking_fuel


# Country
def get_all_countries():
    return Country.objects.filter(status=1)


def get_country_by_id(id_):
    return Country.objects.get(pk=id_)


def get_country_by_name(name):
    return Country.objects.filter(name=name).first()


def create_country(data):
    country = Country()
    country.name = data['name']
    country.status = 1
    country.save()
    return country


# Death Reason
def get_all_death_reasons():
    return DeathReason.objects.filter(status=1)


def get_death_reason_by_id(id_):
    return DeathReason.objects.get(pk=id_)


def get_death_reason_by_name(name):
    return DeathReason.objects.filter(name=name).first()


def create_death_reason(data):
    death_reason = DeathReason()
    death_reason.name = data['name']
    death_reason.status = 1
    death_reason.save()
    return death_reason


# Disability Type
def get_all_disability_types():
    return DisabilityType.objects.filter(status=1)


def get_disability_type_by_id(id_):
    return DisabilityType.objects.get(pk=id_)


def get_disability_type_by_name(name):
    return DisabilityType.objects.filter(name=name).first()


def create_disability_type(data):
    disability_type = DisabilityType()
    disability_type.name = data['name']
    disability_type.status = 1
    disability_type.save()
    return disability_type


# Disaster Name
def get_all_disaster_names():
    return Disaster.objects.filter(status=1)


def get_disaster_name_by_id(id_):
    return Disaster.objects.get(pk=id_)


def get_disaster_name_by_name(name):
    return Disaster.objects.filter(name=name).first()


def create_disaster_name(data):
    disaster_name = Disaster()
    disaster_name.name = data['name']
    disaster_name.status = 1
    disaster_name.save()
    return disaster_name


# House Damage Status
def get_all_house_damage_statuses():
    return HouseDamageStatus.objects.filter(status=1)


def get_house_damage_status_by_id(id_):
    return HouseDamageStatus.objects.get(pk=id_)


def get_house_damage_status_by_name(name):
    return HouseDamageStatus.objects.filter(name=name).first()


def create_house_damage_status(data):
    house_damage_status = HouseDamageStatus()
    house_damage_status.name = data['name']
    house_damage_status.status = 1
    house_damage_status.save()
    return house_damage_status


# Education Level
def get_all_education_levels():
    return EducationLevel.objects.filter(status=1)


def get_education_level_by_id(id_):
    return EducationLevel.objects.get(pk=id_)


def get_education_level_by_name(name):
    return EducationLevel.objects.filter(name=name).first()


def create_education_level(data):
    education_level = EducationLevel()
    education_level.name = data['name']
    education_level.status = 1
    education_level.save()
    return education_level


# Education Status
def get_all_education_statuses():
    return EducationStatus.objects.filter(status=1)


def get_education_status_by_id(id_):
    return EducationStatus.objects.get(pk=id_)


def get_education_status_by_name(name):
    return EducationStatus.objects.filter(name=name).first()


def create_education_status(data):
    education_status = EducationStatus()
    education_status.name = data['name']
    education_status.status = 1
    education_status.save()
    return education_status


# Facility
def get_all_facilities():
    return Facility.objects.filter(status=1)


def get_facility_by_id(id_):
    return Facility.objects.get(pk=id_)


def get_facility_by_name(name):
    return Facility.objects.filter(name=name).first()


def create_facility(data):
    facility = Facility()
    facility.name = data['name']
    facility.status = 1
    facility.save()
    return facility


# Festival
def get_all_festivals():
    return Festival.objects.filter(status=1)


def get_festival_by_id(id_):
    return Festival.objects.get(pk=id_)


def get_festival_by_name(name):
    return Festival.objects.filter(name=name).first()


def create_festival(data):
    festival = Festival()
    festival.name = data['name']
    festival.status = 1
    festival.save()
    return festival


# Foreign Reason
def get_all_foreign_reasons():
    return ForeignReason.objects.filter(status=1)


def get_foreign_reason_by_id(id_):
    return ForeignReason.objects.get(pk=id_)


def get_foreign_reason_by_name(name):
    return ForeignReason.objects.filter(name=name).first()


def create_foreign_reason(data):
    foreign_reason = ForeignReason()
    foreign_reason.name = data['name']
    foreign_reason.status = 1
    foreign_reason.save()
    return foreign_reason


# Garbage Management
def get_all_garbage_managements():
    return GarbageManagement.objects.filter(status=1)


def get_garbage_management_by_id(id_):
    return GarbageManagement.objects.get(pk=id_)


def get_garbage_management_by_name(name):
    return GarbageManagement.objects.filter(name=name).first()


def create_garbage_management(data):
    garbage_management = GarbageManagement()
    garbage_management.name = data['name']
    garbage_management.status = 1
    garbage_management.save()
    return garbage_management


# House Type
def get_all_house_types():
    return HouseType.objects.filter(status=1)


def get_house_type_by_id(id_):
    return HouseType.objects.get(pk=id_)


def get_house_type_by_name(name):
    return HouseType.objects.filter(name=name).first()


def create_house_type(data):
    house_type = HouseType()
    house_type.name = data['name']
    house_type.status = 1
    house_type.save()
    return house_type


# Income Source
def get_all_income_sources():
    return IncomeSource.objects.filter(status=1)


def get_income_source_by_id(id_):
    return IncomeSource.objects.get(pk=id_)


def get_income_source_by_name(name):
    return IncomeSource.objects.filter(name=name).first()


def create_income_source(data):
    income_source = IncomeSource()
    income_source.name = data['name']
    income_source.status = 1
    income_source.save()
    return income_source


# Jaati
def get_all_jaatis():
    return Jaati.objects.filter(status=1)


def get_jaati_by_id(id_):
    return Jaati.objects.get(pk=id_)


def get_jaati_by_name(name):
    return Jaati.objects.filter(name=name).first()


def create_jaati(data):
    jaati = Jaati()
    jaati.name = data['name']
    jaati.status = 1
    jaati.save()
    return jaati


# Land Type
def get_all_land_types():
    return LandType.objects.filter(status=1)


def get_land_type_by_id(id_):
    return LandType.objects.get(pk=id_)


def get_land_type_by_name(name):
    return LandType.objects.filter(name=name).first()


def create_land_type(data):
    land_type = LandType()
    land_type.name = data['name']
    land_type.status = 1
    land_type.save()
    return land_type


# Light Fuel
def get_all_light_fuels():
    return LightFuel.objects.filter(status=1)


def get_light_fuel_by_id(id_):
    return LightFuel.objects.get(pk=id_)


def get_light_fuel_by_name(name):
    return LightFuel.objects.filter(name=name).first()


def create_light_fuel(data):
    light_fuel = LightFuel()
    light_fuel.name = data['name']
    light_fuel.status = 1
    light_fuel.save()
    return light_fuel


# Main Occupation
def get_all_main_occupations():
    return MainOccupation.objects.filter(status=1)


def get_main_occupation_by_id(id_):
    return MainOccupation.objects.get(pk=id_)


def get_main_occupation_by_name(name):
    return MainOccupation.objects.filter(name=name).first()


def create_main_occupation(data):
    main_occupation = MainOccupation()
    main_occupation.name = data['name']
    main_occupation.status = 1
    main_occupation.save()
    return main_occupation


# Marga
def get_all_margas():
    return Marga.objects.filter(status=1)


def get_marga_by_id(id_):
    return Marga.objects.get(pk=id_)


def get_marga_by_name(name):
    return Marga.objects.filter(name=name).first()


def create_marga(data):
    marga = Marga()
    marga.name = data['name']
    marga.status = 1
    marga.save()
    return marga


# Marital Status
def get_all_marital_statuses():
    return MaritalStatus.objects.filter(status=1)


def get_marital_status_by_id(id_):
    return MaritalStatus.objects.get(pk=id_)


def get_marital_status_by_name(name):
    return MaritalStatus.objects.filter(name=name).first()


def create_marital_status(data):
    marital_status = MaritalStatus()
    marital_status.name = data['name']
    marital_status.status = 1
    marital_status.save()
    return marital_status

# Mother Tongue
def get_all_mother_tongues():
    return MotherTongue.objects.filter(status=1)


def get_mother_tongue_by_id(id_):
    return MotherTongue.objects.get(pk=id_)


def get_mother_tongue_by_name(name):
    return MotherTongue.objects.filter(name=name).first()


def create_mother_tongue(data):
    mother_tongue = MotherTongue()
    mother_tongue.name = data['name']
    mother_tongue.status = 1
    mother_tongue.save()
    return mother_tongue


# Relation With HouseHead
def get_all_relation_with_hohs():
    return RelationWithHoh.objects.filter(status=1)


def get_relation_with_hoh_by_id(id_):
    return RelationWithHoh.objects.get(pk=id_)


def get_relation_with_hoh_by_name(name):
    return RelationWithHoh.objects.filter(name=name).first()


def create_relation_with_hoh(data):
    relation_with_hoh = RelationWithHoh()
    relation_with_hoh.name = data['name']
    relation_with_hoh.status = 1
    relation_with_hoh.save()
    return relation_with_hoh


# Religion
def get_all_religions():
    return Religion.objects.filter(status=1)


def get_religion_by_id(id_):
    return Religion.objects.get(pk=id_)


def get_religion_by_name(name):
    return Religion.objects.filter(name=name).first()


def create_religion(data):
    religion = Religion()
    religion.name = data['name']
    religion.status = 1
    religion.save()
    return religion


# Roof Type
def get_all_roof_types():
    return RoofType.objects.filter(status=1)


def get_roof_type_by_id(id_):
    return RoofType.objects.get(pk=id_)


def get_roof_type_by_name(name):
    return RoofType.objects.filter(name=name).first()


def create_roof_type(data):
    roof_type = RoofType()
    roof_type.name = data['name']
    roof_type.status = 1
    roof_type.save()
    return roof_type


# Roof Type
def get_all_sewage_types():
    return SewageType.objects.filter(status=1)


def get_sewage_type_by_id(id_):
    return SewageType.objects.get(pk=id_)


def get_sewage_type_by_name(name):
    return SewageType.objects.filter(name=name).first()


def create_sewage_type(data):
    sewage_type = SewageType()
    sewage_type.name = data['name']
    sewage_type.status = 1
    sewage_type.save()
    return sewage_type


# Technical Skill
def get_all_technical_skills():
    return TechnicalSkill.objects.filter(status=1)


def get_technical_skill_by_id(id_):
    return TechnicalSkill.objects.get(pk=id_)


def get_technical_skill_by_name(name):
    return TechnicalSkill.objects.filter(name=name).first()


def create_technical_skill(data):
    technical_skill = TechnicalSkill()
    technical_skill.name = data['name']
    technical_skill.status = 1
    technical_skill.save()
    return technical_skill


# Toilet Type
def get_all_toilet_types():
    return ToiletType.objects.filter(status=1)


def get_toilet_type_by_id(id_):
    return ToiletType.objects.get(pk=id_)


def get_toilet_type_by_name(name):
    return ToiletType.objects.filter(name=name).first()


def create_toilet_type(data):
    toilet_type = ToiletType()
    toilet_type.name = data['name']
    toilet_type.status = 1
    toilet_type.save()
    return toilet_type


# Vaccine Name
def get_all_vaccine_names():
    return VaccineName.objects.filter(status=1)


def get_vaccine_name_by_id(id_):
    return VaccineName.objects.get(pk=id_)


def get_vaccine_name_by_name(name):
    return VaccineName.objects.filter(name=name).first()


def create_vaccine_name(data):
    vaccine_name = VaccineName()
    vaccine_name.name = data['name']
    vaccine_name.status = 1
    vaccine_name.save()
    return vaccine_name


# Vehicle Type
def get_all_vehicle_types():
    return VehicleType.objects.filter(status=1)


def get_vehicle_type_by_id(id_):
    return VehicleType.objects.get(pk=id_)


def get_vehicle_type_by_name(name):
    return VehicleType.objects.filter(name=name).first()


def create_vehicle_type(data):
    vehicle_type = VehicleType()
    vehicle_type.name = data['name']
    vehicle_type.status = 1
    vehicle_type.save()
    return vehicle_type


# Ward
def get_all_wards():
    return Ward.objects.filter(status=1)


def get_ward_by_id(id_):
    return Ward.objects.get(pk=id_)


def get_ward_by_name(name):
    return Ward.objects.filter(name=name).first()


def create_ward(data):
    ward = Ward()
    ward.name = data['name']
    ward.status = 1
    ward.save()
    return ward


def create_collector(data):
    collector = Collector()
    collector.name = data['name']
    collector.phone = data['phone']
    collector.password = data['password'] if 'password' in data['password'] and data['password'] else data['phone']
    collector.status = 1
    collector.save()
    return collector


def get_all_collectors():
    return Collector.objects.filter(status=1)


def get_collector_by_id(id_):
    return Collector.objects.get(pk=id_)


def get_collector_by_name(name):
    return Collector.objects.filter(name=name).first()


# Ward
def get_all_water_sources():
    return WaterSource.objects.filter(status=1)


def get_water_source_by_id(id_):
    return WaterSource.objects.get(pk=id_)


def get_water_source_by_name(name):
    return WaterSource.objects.filter(name=name).first()


def create_water_source(data):
    water_source = WaterSource()
    water_source.name = data['name']
    water_source.status = 1
    water_source.save()
    return water_source


def get_all_disability_cards():
    return DisabilityCard.objects.all()


def get_all_genders():
    return Gender.objects.all()