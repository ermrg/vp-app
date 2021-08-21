from app.models.vp.house_detail import HouseDetail
from app.models.vp.household import Household


                        # Household By Ward
from app.models.vp.household_facility import HouseholdFacility
from app.models.vp.household_infrastructure import HouseholdInfrastructure


def get_all_ward_1():
    ward_1 = Household.objects.filter(ward=1).count()
    return ward_1


def get_all_ward_2():
    ward_2 = Household.objects.filter(ward=2).count()
    return ward_2


def get_all_ward_3():
    ward_3 = Household.objects.filter(ward=3).count()
    return ward_3


def get_all_ward_4():
    ward_4 = Household.objects.filter(ward=4).count()
    return ward_4


def get_all_ward_5():
    ward_5 = Household.objects.filter(ward=5).count()
    return ward_5


def get_all_ward_6():
    ward_6 = Household.objects.filter(ward=6).count()
    return ward_6


def get_all_ward_7():
    ward_7 = Household.objects.filter(ward=7).count()
    return ward_7


def get_all_ward_8():
    ward_8 = Household.objects.filter(ward=8).count()
    return ward_8


def get_all_ward_9():
    ward_9 = Household.objects.filter(ward=9).count()
    return ward_9


                                    # Household Residence
def get_all_household_from_birth():
    from_birth = Household.objects.filter(resident_type='from_birth').count()
    return from_birth


def get_all_household_migrated():
    migrated = Household.objects.filter(resident_type='migrated').count()
    return migrated


                                    # House Type
def get_all_rcc_concrete():
    rcc_concrete = HouseDetail.objects.filter(house_type='1').count()
    return rcc_concrete


def get_all_load_bearing_concrete():
    load_bearing_concrete = HouseDetail.objects.filter(house_type='2').count()
    return load_bearing_concrete


def get_all_not_concrete():
    not_concrete = HouseDetail.objects.filter(house_type='3').count()
    return not_concrete


def get_all_hard_soil():
    hard_soil = HouseDetail.objects.filter(house_type='4').count()
    return hard_soil


def get_all_stone_soil():
    stone_soil = HouseDetail.objects.filter(house_type='5').count()
    return stone_soil


def get_all_cottage():
    cottage = HouseDetail.objects.filter(house_type='6').count()
    return cottage


                        # Roof Types
def get_all_solid_roof():
    solid_roof = HouseDetail.objects.filter(roof_type='1').count()
    return solid_roof


def get_all_zinc_roof():
    zinc_roof = HouseDetail.objects.filter(roof_type='2').count()
    return zinc_roof


def get_all_stone_roof():
    stone_roof = HouseDetail.objects.filter(roof_type='3').count()
    return stone_roof


def get_all_straw_roof():
    straw_roof = HouseDetail.objects.filter(roof_type='4').count()
    return straw_roof


                            # Water Source
def get_all_taps():
    taps = HouseholdInfrastructure.objects.filter(water_source='1').count()
    return taps


def get_all_well():
    well = HouseholdInfrastructure.objects.filter(water_source='2').count()
    return well


def get_all_natural_source():
    natural_source = HouseholdInfrastructure.objects.filter(water_source='3').count()
    return natural_source


def get_all_river():
    river = HouseholdInfrastructure.objects.filter(water_source='4').count()
    return river


                        # Cooking Fuel
def get_all_electricity():
    electricity = HouseholdInfrastructure.objects.filter(cooking_fuel='1').count()
    return electricity


def get_all_lp_gas():
    lp_gas = HouseholdInfrastructure.objects.filter(cooking_fuel='2').count()
    return lp_gas


def get_all_bio_gas():
    bio_gas = HouseholdInfrastructure.objects.filter(cooking_fuel='3').count()
    return bio_gas


def get_all_woods():
    woods = HouseholdInfrastructure.objects.filter(cooking_fuel='4').count()
    return woods


                                # Light Fuel
def get_all_national_electricity():
    national_electricity = HouseholdInfrastructure.objects.filter(light_fuel='1').count()
    return national_electricity


def get_all_local_electricity():
    local_electricity = HouseholdInfrastructure.objects.filter(light_fuel='2').count()
    return local_electricity


def get_all_solar():
    solar = HouseholdInfrastructure.objects.filter(light_fuel='3').count()
    return solar


def get_all_kerosene():
    kerosene = HouseholdInfrastructure.objects.filter(light_fuel='4').count()
    return kerosene


def get_all_other_light_fuels():
    other_light_fuels = HouseholdInfrastructure.objects.filter(light_fuel='5').count()
    return other_light_fuels


                                # Toilet Type
def get_all_solid_latrine():
    solid_latrine = HouseholdInfrastructure.objects.filter(toilet_type=1).count()
    return solid_latrine


def get_all_weak_latrine():
    weak_latrine = HouseholdInfrastructure.objects.filter(toilet_type=2).count()
    return weak_latrine


def get_all_no_latrine():
    no_latrine = HouseholdInfrastructure.objects.filter(toilet_type=3).count()
    return no_latrine


                                # Garbage Management
def get_all_managed_at_home():
    managed_at_home = HouseholdInfrastructure.objects.filter(garbage_management=1).count()
    return managed_at_home


def get_all_dumping_site():
    dumping_site = HouseholdInfrastructure.objects.filter(garbage_management=2).count()
    return dumping_site


def get_all_comes_to_collect():
    comes_to_collect = HouseholdInfrastructure.objects.filter(garbage_management=3).count()
    return comes_to_collect


def get_all_stream():
    stream = HouseholdInfrastructure.objects.filter(garbage_management=4).count()
    return stream


def get_all_lake():
    lake = HouseholdInfrastructure.objects.filter(garbage_management=5).count()
    return lake


                                        # sewage Type

def get_all_public_sewage():
    public_sewage = HouseholdInfrastructure.objects.filter(sewage_type=1).count()
    return public_sewage


def get_all_safety_tank():
    safety_tank = HouseholdInfrastructure.objects.filter(sewage_type=2).count()
    return safety_tank


def get_all_common_sewage():
    common_sewage = HouseholdInfrastructure.objects.filter(sewage_type=3).count()
    return common_sewage


def get_all_open_sewage():
    open_sewage = HouseholdInfrastructure.objects.filter(sewage_type=4).count()
    return open_sewage


                                        # Vehicle Types
def get_all_radios():
    radios = HouseholdFacility.objects.filter(name=1).count()
    return radios


def get_all_televisions():
    televisions = HouseholdFacility.objects.filter(name=2).count()
    return televisions


def get_all_mobiles():
    mobiles = HouseholdFacility.objects.filter(name=3).count()
    return mobiles


def get_all_landline_phones():
    landline_phones = HouseholdFacility.objects.filter(name=4).count()
    return landline_phones


def get_all_internet():
    internet = HouseholdFacility.objects.filter(name=5).count()
    return internet


def get_all_refrigerators():
    refrigerators = HouseholdFacility.objects.filter(name=6).count()
    return refrigerators


def get_all_washing_machines():
    washing_machines = HouseholdFacility.objects.filter(name=7).count()
    return washing_machines


def get_all_ovens():
    ovens = HouseholdFacility.objects.filter(name=8).count()
    return ovens



