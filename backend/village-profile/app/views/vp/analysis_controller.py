from django.db.models import Count, Q
from django.shortcuts import render, redirect

from app.models.vp.member import Member
from app.services.analysis.agricultureService import get_all_khet_sima, get_all_khet_aayam, get_all_khet_doyam, \
    get_all_bari, get_all_ghaderi, get_all_pakha_bari, get_all_cow_category, get_all_buffalo_category, \
    get_all_yak_chauri, get_all_goat_category, get_all_pigs, get_all_chicken_category, get_all_ostrich, \
    get_all_pets_category, get_all_house_with_garden, get_all_house_without_garden
from app.services.analysis.demographyService import get_all_male_genders, get_all_female_genders, get_all_other_genders, \
    get_all_hindus, get_all_buddhists, get_all_christians, get_all_muslims, get_all_kirats, get_all_chhetries, \
    get_all_bhramins, get_all_magars, get_all_tharus, get_all_tamangs, get_all_newars, get_all_kamis, get_all_musalmans, \
    get_all_yadavs, get_all_rais, get_all_gurungs, get_all_damais, get_all_thakuris, get_all_limbus, get_all_sarkis, \
    get_all_telis, get_all_musahars, get_all_rautes, get_all_pasies, get_all_lan_nepali, get_all_lan_maithali, \
    get_all_lan_tharu, get_all_lan_tamang, get_all_lan_nepal_bhasa, get_all_lan_bajjika, get_all_lan_magar, \
    get_all_lan_doteli, get_all_lan_urdu, get_all_lan_awadhi, get_all_lan_limbu, get_all_lan_gurung, \
    get_all_lan_baitadeli, get_all_lan_rai, get_all_lan_achhami, get_all_lan_bantawa, get_all_lan_rajbansi, \
    get_all_lan_sherpa, get_all_lan_bhojpuri, get_all_blind, get_all_semi_blind, get_all_deaf, \
    get_all_dumb, get_all_slow_minded, get_all_semi_deaf, get_all_paralyzed, get_all_red_card, get_all_blue_card, \
    get_all_white_card, get_all_no_card, get_all_non_disabled, get_all_occupation_agriculture, \
    get_all_occupation_business, get_all_occupation_gov_job, get_all_occupation_entrepreneur, \
    get_all_occupation_self_employed, get_all_occupation_others, get_all_death_age, get_all_accident, get_all_suicide, \
    get_all_murdered, get_all_disease, get_all_not_known, get_all_abroad_for_employment, get_all_abroad_for_business, \
    get_all_abroad_for_study, get_all_abroad_for_migration, get_all_male_househead, get_all_female_househead, \
    get_all_other_househead, get_all_population
from app.services.analysis.educationService import get_all_studying, get_all_left_study, get_all_study_completed, \
    get_all_no_study, get_all_male_studying, get_all_male_left_study, get_all_male_study_completed, \
    get_all_male_no_study, get_all_female_studying, get_all_female_left_study, get_all_female_study_completed, \
    get_all_female_no_study, get_all_primary_level, get_all_illiterate, get_all_pre_primary_level, \
    get_all_secondary_level, get_all_bachelor_level, get_all_degree_level, get_all_master_phd_level, \
    get_all_high_school_level, get_all_normal_read_write, get_all_electrician, get_all_mason, get_all_painter, \
    get_all_plumber, get_all_carpenter, get_all_tech_and_information, get_all_knitting_stitch, get_all_other_skills
from app.services.analysis.financeService import get_all_vegetable_agriculture, get_all_animal_husbandry, \
    get_all_chicken_farm, get_all_fish_farm, get_all_indigence_labour, get_all_business, get_all_foreign_employment, \
    get_all_goverment_job, get_all_non_gov_jobs, get_all_house_rent, get_all_land_rent, \
    get_all_employed_in_korea, get_all_employed_in_dubai, get_all_employed_in_germany, get_all_employed_in_india, \
    get_all_employed_in_iraq, get_all_employed_in_israel, get_all_employed_in_japan, get_all_employed_in_kuwait, \
    get_all_employed_in_malaysia, get_all_employed_in_qatar, get_all_employed_in_saudi, get_all_employed_in_america, \
    get_all_employed_in_england, get_all_employed_in_bahrain, get_all_employed_in_australia, get_all_with_bank_ac, \
    get_all_without_bank_ac
from app.services.analysis.healthService import get_all_vaccinated, get_all_non_vaccinated
from app.services.analysis.householdAmenitiesService import get_all_ward_1, get_all_ward_2, get_all_ward_3, \
    get_all_ward_4, get_all_ward_5, get_all_ward_6, get_all_ward_7, get_all_ward_8, get_all_ward_9, \
    get_all_household_from_birth, get_all_household_migrated, get_all_not_concrete, get_all_rcc_concrete, \
    get_all_load_bearing_concrete, get_all_hard_soil, get_all_stone_soil, get_all_cottage, get_all_solid_roof, \
    get_all_zinc_roof, get_all_stone_roof, get_all_straw_roof, get_all_taps, get_all_well, get_all_natural_source, \
    get_all_river, get_all_electricity, get_all_lp_gas, get_all_bio_gas, get_all_woods, get_all_national_electricity, \
    get_all_local_electricity, get_all_solar, get_all_kerosene, get_all_other_light_fuels, get_all_solid_latrine, \
    get_all_weak_latrine, get_all_no_latrine, get_all_managed_at_home, get_all_dumping_site, get_all_comes_to_collect, \
    get_all_stream, get_all_lake, get_all_public_sewage, get_all_safety_tank, get_all_common_sewage, \
    get_all_open_sewage, get_all_radios, get_all_televisions, get_all_mobiles, get_all_landline_phones, \
    get_all_internet, get_all_refrigerators, get_all_washing_machines, get_all_ovens


def demography_page(request):
    population = dict()

    # genders
    population['male'] = get_all_male_genders()
    population['female'] = get_all_female_genders()
    population['other_genders'] = get_all_other_genders()
    population['total_population'] = get_all_population()

    # religions
    population['hindus'] = get_all_hindus()
    population['buddhists'] = get_all_buddhists()
    population['muslims'] = get_all_muslims()
    population['christians'] = get_all_christians()
    population['kirats'] = get_all_kirats()

    # ethnics
    population['chhetris'] = get_all_chhetries()
    population['brahmins'] = get_all_bhramins()
    population['magars'] = get_all_magars()
    population['tharus'] = get_all_tharus()
    population['tamangs'] = get_all_tamangs()
    population['newars'] = get_all_newars()
    population['kamis'] = get_all_kamis()
    population['musalmans'] = get_all_musalmans()
    population['yadavs'] = get_all_yadavs()
    population['rais'] = get_all_rais()
    population['gurungs'] = get_all_gurungs()
    population['damais'] = get_all_damais()
    population['thakuris'] = get_all_thakuris()
    population['limbus'] = get_all_limbus()
    population['sarkis'] = get_all_sarkis()
    population['telis'] = get_all_telis()
    population['musahars'] = get_all_musahars()
    population['rautes'] = get_all_rautes()
    population['pasies'] = get_all_pasies()

    # mother Tongue
    population['nepali'] = get_all_lan_nepali()
    population['maithali'] = get_all_lan_maithali()
    population['tharu'] = get_all_lan_tharu()
    population['tamang'] = get_all_lan_tamang()
    population['nepal_bhasa'] = get_all_lan_nepal_bhasa()
    population['bajjika'] = get_all_lan_bajjika()
    population['magar'] = get_all_lan_magar()
    population['doteli'] = get_all_lan_doteli()
    population['urdu'] = get_all_lan_urdu()
    population['awadhi'] = get_all_lan_awadhi()
    population['limbu'] = get_all_lan_limbu()
    population['gurung'] = get_all_lan_gurung()
    population['baitadeli'] = get_all_lan_baitadeli()
    population['rai'] = get_all_lan_rai()
    population['achhami'] = get_all_lan_achhami()
    population['bantawa'] = get_all_lan_bantawa()
    population['rajbansi'] = get_all_lan_rajbansi()
    population['sherpa'] = get_all_lan_sherpa()
    population['bhojpuri'] = get_all_lan_bhojpuri()

    # disability Type
    population['blind'] = get_all_blind()
    population['semi_blind'] = get_all_semi_blind()
    population['deaf'] = get_all_deaf()
    population['dumb'] = get_all_dumb()
    population['slow_minded'] = get_all_slow_minded()
    population['semi_deaf'] = get_all_semi_deaf()
    population['paralyzed'] = get_all_paralyzed()
    population['is_not_disable'] = get_all_non_disabled()

    # disability Card
    population['red_card'] = get_all_red_card()
    population['blue_card'] = get_all_blue_card()
    population['white_card'] = get_all_white_card()
    population['no_card'] = get_all_no_card()

    # Household Main Occupation
    population['occ_agriculture'] = get_all_occupation_agriculture()
    population['occ_business'] = get_all_occupation_business()
    population['occ_gov_job'] = get_all_occupation_gov_job()
    population['occ_entrepreneur'] = get_all_occupation_entrepreneur()
    population['occ_self_employed'] = get_all_occupation_self_employed()
    population['occ_others'] = get_all_occupation_others()

    # Member Death Reasons
    population['death_age'] = get_all_death_age()
    population['accident'] = get_all_accident()
    population['suicide'] = get_all_suicide()
    population['murdered'] = get_all_murdered()
    population['disease'] = get_all_disease()
    population['not_known'] = get_all_not_known()

    # reason of being in Abroad
    population['employement'] = get_all_abroad_for_employment()
    population['business'] = get_all_abroad_for_business()
    population['study'] = get_all_abroad_for_study()
    population['migration'] = get_all_abroad_for_migration()

    # Househead by Gender
    population['househead_male'] = get_all_male_househead()
    population['househead_female'] = get_all_female_househead()
    population['househead_other'] = get_all_other_househead()

    return render(request, 'app/backend/vp/analysis/demography.html', population)


def education_page(request):
    education = dict()

    # education status
    education['studying'] = get_all_studying()
    education['left_study'] = get_all_left_study()
    education['study_completed'] = get_all_study_completed()
    education['no_study'] = get_all_no_study()
    # education status Male
    education['male_studying'] = get_all_male_studying()
    education['male_left_study'] = get_all_male_left_study()
    education['male_study_completed'] = get_all_male_study_completed()
    education['male_no_study'] = get_all_male_no_study()
    # education status Female
    education['female_studying'] = get_all_female_studying()
    education['female_left_study'] = get_all_female_left_study()
    education['female_study_completed'] = get_all_female_study_completed()
    education['female_no_study'] = get_all_female_no_study()

    # Education Level
    education['primary_level'] = get_all_primary_level()
    education['pre_primary_level'] = get_all_pre_primary_level()
    education['secondary_level'] = get_all_secondary_level()
    education['bachelor_level'] = get_all_bachelor_level()
    education['degree_level'] = get_all_degree_level()
    education['master_phd_level'] = get_all_master_phd_level()
    education['high_school_level'] = get_all_high_school_level()
    education['normal_read_write'] = get_all_normal_read_write()

    # technical skill
    education['electrician'] = get_all_electrician()
    education['mason'] = get_all_mason()
    education['painter'] = get_all_painter()
    education['plumber'] = get_all_plumber()
    education['carpenter'] = get_all_carpenter()
    education['tech_and_information'] = get_all_tech_and_information()
    education['knitting_stitch'] = get_all_knitting_stitch()
    education['other_skills'] = get_all_other_skills()

    return render(request, 'app/backend/vp/analysis/education.html', education)


def household_page(request):
    household = dict()

    # household on Wards
    household['ward_1'] = get_all_ward_1()
    household['ward_2'] = get_all_ward_2()
    household['ward_3'] = get_all_ward_3()
    household['ward_4'] = get_all_ward_4()
    household['ward_5'] = get_all_ward_5()
    household['ward_6'] = get_all_ward_6()
    household['ward_7'] = get_all_ward_7()
    household['ward_8'] = get_all_ward_8()
    household['ward_9'] = get_all_ward_9()

    # Residence Type
    household['from_birth'] = get_all_household_from_birth()
    household['migrated'] = get_all_household_migrated()

    # House Type
    household['rcc_concrete'] = get_all_rcc_concrete()
    household['load_bearing_concrete'] = get_all_load_bearing_concrete()
    household['not_concrete'] = get_all_not_concrete()
    household['hard_soil'] = get_all_hard_soil()
    household['stone_soil'] = get_all_stone_soil()
    household['cottage'] = get_all_cottage()

    # Roof Type
    household['solid_roof'] = get_all_solid_roof()
    household['zinc_roof'] = get_all_zinc_roof()
    household['stone_roof'] = get_all_stone_roof()
    household['straw_roof'] = get_all_straw_roof()

    # Water Source
    household['taps'] = get_all_taps()
    household['well'] = get_all_well()
    household['natural_source'] = get_all_natural_source()
    household['river'] = get_all_river()

    # Cooking Fuel
    household['electricity'] = get_all_electricity()
    household['lp_gas'] = get_all_lp_gas()
    household['bio_gas'] = get_all_bio_gas()
    household['woods'] = get_all_woods()

    # Light Fuel
    household['national_electricity'] = get_all_national_electricity()
    household['local_electricity'] = get_all_local_electricity()
    household['solar'] = get_all_solar()
    household['kerosene'] = get_all_kerosene()
    household['other_light_fuels'] = get_all_other_light_fuels()

    # Toilet Types
    household['solid_latrine'] = get_all_solid_latrine()
    household['weak_latrine'] = get_all_weak_latrine()
    household['no_latrine'] = get_all_no_latrine()

    # Garbage Management
    household['managed_at_home'] = get_all_managed_at_home()
    household['dumping_site'] = get_all_dumping_site()
    household['comes_to_collect'] = get_all_comes_to_collect()
    household['stream'] = get_all_stream()
    household['lake'] = get_all_lake()

    # Sewage Type
    household['public_sewage'] = get_all_public_sewage()
    household['safety_tank'] = get_all_safety_tank()
    household['common_sewage'] = get_all_common_sewage()
    household['open_sewage'] = get_all_open_sewage()

    # Facilities
    household['radios'] = get_all_radios()
    household['televisions'] = get_all_televisions()
    household['mobiles'] = get_all_mobiles()
    household['landline_phones'] = get_all_landline_phones()
    household['internet'] = get_all_internet()
    household['refrigerators'] = get_all_refrigerators()
    household['washing_machines'] = get_all_washing_machines()
    household['ovens'] = get_all_ovens()

    return render(request, 'app/backend/vp/analysis/household_amenities.html', household)


def finance_page(request):
    finance = dict()

    # Bank AC
    finance['with_bank_ac'] = get_all_with_bank_ac
    finance['without_bank_ac'] = get_all_without_bank_ac

    # Earning Source
    finance['vegetable_agriculture'] = get_all_vegetable_agriculture
    finance['animal_husbandry'] = get_all_animal_husbandry
    finance['chicken_farm'] = get_all_chicken_farm
    finance['fish_farm'] = get_all_fish_farm
    finance['indigence_labour'] = get_all_indigence_labour
    finance['business'] = get_all_business
    finance['foreign_employment'] = get_all_foreign_employment
    finance['goverment_job'] = get_all_goverment_job
    finance['non_gov_jobs'] = get_all_non_gov_jobs
    finance['house_rent'] = get_all_house_rent
    finance['land_rent'] = get_all_land_rent

    # Empolyed Countries
    finance['employed_in_australia'] = get_all_employed_in_australia
    finance['employed_in_bahrain'] = get_all_employed_in_bahrain
    finance['employed_in_korea'] = get_all_employed_in_korea
    finance['employed_in_dubai'] = get_all_employed_in_dubai
    finance['employed_in_germany'] = get_all_employed_in_germany
    finance['employed_in_india'] = get_all_employed_in_india
    finance['employed_in_iraq'] = get_all_employed_in_iraq
    finance['employed_in_israel'] = get_all_employed_in_israel
    finance['employed_in_japan'] = get_all_employed_in_japan
    finance['employed_in_kuwait'] = get_all_employed_in_kuwait
    finance['employed_in_malaysia'] = get_all_employed_in_malaysia
    finance['employed_in_qatar'] = get_all_employed_in_qatar
    finance['employed_in_saudi'] = get_all_employed_in_saudi
    finance['employed_in_america'] = get_all_employed_in_america
    finance['employed_in_england'] = get_all_employed_in_england

    return render(request, 'app/backend/vp/analysis/finance.html', finance)


def health_page(request):
    health = dict()

    # Vaccinated or not
    health['vaccinated'] = get_all_vaccinated
    health['non_vaccinated'] = get_all_non_vaccinated

    return render(request, 'app/backend/vp/analysis/health.html', health)


def agriculture_page(request):
    agriculture = dict()

    # land Type
    agriculture['khet_aayam'] = get_all_khet_aayam()
    agriculture['khet_doyam'] = get_all_khet_doyam()
    agriculture['bari'] = get_all_bari()
    agriculture['ghaderi'] = get_all_ghaderi()
    agriculture['pakha_bari'] = get_all_pakha_bari()
    agriculture['khet_sima'] = get_all_khet_sima()

    # Animal Type
    agriculture['cow_category'] = get_all_cow_category()
    agriculture['buffalo_category'] = get_all_buffalo_category()
    agriculture['yak_chauri'] = get_all_yak_chauri()
    agriculture['goat_category'] = get_all_goat_category()
    agriculture['pigs'] = get_all_pigs()
    agriculture['chicken_category'] = get_all_chicken_category()
    agriculture['ostrich'] = get_all_ostrich()
    agriculture['pets_category'] = get_all_pets_category()

    # House with Garden
    agriculture['house_with_garden'] = get_all_house_with_garden()
    agriculture['house_without_garden'] = get_all_house_without_garden()

    return render(request, 'app/backend/vp/analysis/agriculture.html', agriculture)
