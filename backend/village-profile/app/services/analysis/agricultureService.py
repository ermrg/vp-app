from app.models.vp.household import Household
from app.models.vp.household_animal import HouseholdAnimal
from app.models.vp.household_land import HouseholdLand


                                # Land Type
def get_all_khet_aayam():
    khet_aayam = HouseholdLand.objects.filter(land_type=1).count()
    return khet_aayam


def get_all_khet_doyam():
    khet_doyam = HouseholdLand.objects.filter(land_type=2).count()
    return khet_doyam


def get_all_bari():
    bari = HouseholdLand.objects.filter(land_type=3).count()
    return bari


def get_all_ghaderi():
    ghaderi = HouseholdLand.objects.filter(land_type=4).count()
    return ghaderi


def get_all_pakha_bari():
    pakha_bari = HouseholdLand.objects.filter(land_type=5).count()
    return pakha_bari


def get_all_khet_sima():
    khet_sima = HouseholdLand.objects.filter(land_type=6).count()
    return khet_sima


                                        # Animal Type
def get_all_cow_category():
    cow_category = HouseholdAnimal.objects.filter(animal_type=1).count()
    return cow_category


def get_all_buffalo_category():
    buffalo_category = HouseholdAnimal.objects.filter(animal_type=2).count()
    return buffalo_category


def get_all_yak_chauri():
    yak_chauri = HouseholdAnimal.objects.filter(animal_type=3).count()
    return yak_chauri


def get_all_goat_category():
    goat_category = HouseholdAnimal.objects.filter(animal_type=4).count()
    return goat_category


def get_all_pigs():
    pigs = HouseholdAnimal.objects.filter(animal_type=5).count()
    return pigs


def get_all_chicken_category():
    chicken_category = HouseholdAnimal.objects.filter(animal_type=6).count()
    return chicken_category


def get_all_ostrich():
    ostrich = HouseholdAnimal.objects.filter(animal_type=7).count()
    return ostrich


def get_all_pets_category():
    pets_category = HouseholdAnimal.objects.filter(animal_type=8).count()
    return pets_category


                                    # Household Garden
def get_all_house_with_garden():
    house_with_garden = Household.objects.filter(has_garden=0).count()
    return house_with_garden


def get_all_house_without_garden():
    house_without_garden = Household.objects.filter(has_garden=1).count()
    return house_without_garden


