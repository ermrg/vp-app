from app.models.vp.household import Household
from app.models.vp.member import Member
from app.models.vp.member_deceased import MemberDeceased


def get_all_population():
    populations = Member.objects.all().count()
    return populations


                                                # Population by Genders
def get_all_male_genders():
    male_genders = Member.objects.filter(gender=1).count()
    return male_genders


def get_all_female_genders():
    female_genders = Member.objects.filter(gender=2).count()
    return female_genders


def get_all_other_genders():
    other_genders = Member.objects.filter(gender=3).count()
    return other_genders


                                                # Household by Religion
def get_all_hindus():
    hindus = Household.objects.filter(religion=1).count()
    return hindus


def get_all_buddhists():
    buddhists = Household.objects.filter(religion=2).count()
    return buddhists


def get_all_muslims():
    muslims = Household.objects.filter(religion=3).count()
    return muslims


def get_all_christians():
    christians = Household.objects.filter(religion=4).count()
    return christians


def get_all_kirats():
    kirats = Household.objects.filter(religion=5).count()
    return kirats


                                                    # Household by Ethnics/ Jaati
def get_all_chhetries():
    chhetries = Household.objects.filter(jaati=1).count
    return chhetries


def get_all_bhramins():
    bhramins = Household.objects.filter(jaati=2).count
    return bhramins


def get_all_magars():
    magars = Household.objects.filter(jaati=3).count
    return magars


def get_all_tharus():
    tharus = Household.objects.filter(jaati=4).count
    return tharus


def get_all_tamangs():
    tamangs = Household.objects.filter(jaati=5).count
    return tamangs


def get_all_newars():
    newars = Household.objects.filter(jaati=6).count
    return newars


def get_all_kamis():
    kamis = Household.objects.filter(jaati=7).count
    return kamis


def get_all_musalmans():
    musalmans = Household.objects.filter(jaati=8).count
    return musalmans


def get_all_yadavs():
    yadavs = Household.objects.filter(jaati=9).count
    return yadavs


def get_all_rais():
    rais = Household.objects.filter(jaati=10).count
    return rais


def get_all_gurungs():
    gurungs = Household.objects.filter(jaati=11).count
    return gurungs


def get_all_damais():
    damais = Household.objects.filter(jaati=12).count
    return damais


def get_all_thakuris():
    thakuris = Household.objects.filter(jaati=13).count
    return thakuris


def get_all_limbus():
    limbus = Household.objects.filter(jaati=14).count
    return limbus


def get_all_sarkis():
    sarkis = Household.objects.filter(jaati=15).count
    return sarkis


def get_all_telis():
    telis = Household.objects.filter(jaati=16).count
    return telis


def get_all_musahars():
    musahars = Household.objects.filter(jaati=17).count
    return musahars


def get_all_rautes():
    rautes = Household.objects.filter(jaati=18).count
    return rautes


def get_all_pasies():
    pasies = Household.objects.filter(jaati=19).count
    return pasies


                                                        # Household on Mother Tongue
def get_all_lan_nepali():
    nepali = Household.objects.filter(mother_tongue=1).count
    return nepali


def get_all_lan_maithali():
    maithali = Household.objects.filter(mother_tongue=2).count
    return maithali


def get_all_lan_tharu():
    tharu = Household.objects.filter(mother_tongue=3).count
    return tharu


def get_all_lan_tamang():
    tamang = Household.objects.filter(mother_tongue=4).count
    return tamang


def get_all_lan_nepal_bhasa():
    nepal_bhasa = Household.objects.filter(mother_tongue=5).count
    return nepal_bhasa


def get_all_lan_bajjika():
    bajjika = Household.objects.filter(mother_tongue=6).count
    return bajjika


def get_all_lan_magar():
    magar = Household.objects.filter(mother_tongue=7).count
    return magar


def get_all_lan_doteli():
    doteli = Household.objects.filter(mother_tongue=8).count
    return doteli


def get_all_lan_urdu():
    urdu = Household.objects.filter(mother_tongue=9).count
    return urdu


def get_all_lan_awadhi():
    awadhi = Household.objects.filter(mother_tongue=10).count
    return awadhi


def get_all_lan_limbu():
    limbu = Household.objects.filter(mother_tongue=11).count
    return limbu


def get_all_lan_gurung():
    gurung = Household.objects.filter(mother_tongue=12).count
    return gurung


def get_all_lan_baitadeli():
    baitadeli = Household.objects.filter(mother_tongue=13).count
    return baitadeli


def get_all_lan_rai():
    rai = Household.objects.filter(mother_tongue=14).count
    return rai


def get_all_lan_achhami():
    achhami = Household.objects.filter(mother_tongue=15).count
    return achhami


def get_all_lan_bantawa():
    bantawa = Household.objects.filter(mother_tongue=16).count
    return bantawa


def get_all_lan_rajbansi():
    rajbansi = Household.objects.filter(mother_tongue=17).count
    return rajbansi


def get_all_lan_sherpa():
    sherpa = Household.objects.filter(mother_tongue=18).count
    return sherpa


def get_all_lan_bhojpuri():
    bhojpuri = Household.objects.filter(mother_tongue=19).count
    return bhojpuri


                                                                # disability
def get_all_blind():
    blind = Member.objects.filter(disability_type=1).count()
    return blind


def get_all_semi_blind():
    semi_blind = Member.objects.filter(disability_type=2).count()
    return semi_blind


def get_all_deaf():
    deaf = Member.objects.filter(disability_type=3).count()
    return deaf


def get_all_dumb():
    dumb = Member.objects.filter(disability_type=4).count()
    return dumb


def get_all_slow_minded():
    slow_minded = Member.objects.filter(disability_type=5).count()
    return slow_minded


def get_all_semi_deaf():
    semi_deaf = Member.objects.filter(disability_type=6).count()
    return semi_deaf


def get_all_paralyzed():
    paralyzed = Member.objects.filter(disability_type=7).count()
    return paralyzed


def get_all_non_disabled():
    is_not_disable = Member.objects.filter(has_disability=0).count()
    return is_not_disable


                         # Disability Card Type
def get_all_red_card():
    red_card = Member.objects.filter(disability_card=1).count()
    return red_card


def get_all_blue_card():
    blue_card = Member.objects.filter(disability_card=2).count()
    return blue_card


def get_all_white_card():
    white_card = Member.objects.filter(disability_card=3).count()
    return white_card


def get_all_no_card():
    no_card = Member.objects.filter(disability_card=4).count()
    return no_card


                                    # Household Main Occupation
def get_all_occupation_agriculture():
    occ_agriculture = Household.objects.filter(main_occupation=1).count()
    return occ_agriculture


def get_all_occupation_business():
    occ_business = Household.objects.filter(main_occupation=2).count()
    return occ_business


def get_all_occupation_gov_job():
    occ_gov_job = Household.objects.filter(main_occupation=4).count()
    return occ_gov_job


def get_all_occupation_entrepreneur():
    occ_entrepreneur = Household.objects.filter(main_occupation=10).count()
    return occ_entrepreneur


def get_all_occupation_self_employed():
    occ_self_employed = Household.objects.filter(main_occupation=11).count()
    return occ_self_employed


def get_all_occupation_others():
    occ_others = Household.objects.filter(main_occupation=12).count()
    return occ_others


                        # Member Death Reasons
def get_all_death_age():
    death_age = MemberDeceased.objects.filter(reason_of_death=1).count()
    return death_age


def get_all_accident():
    accident = MemberDeceased.objects.filter(reason_of_death=2).count()
    return accident


def get_all_suicide():
    suicide = MemberDeceased.objects.filter(reason_of_death=3).count()
    return suicide


def get_all_murdered():
    murdered = MemberDeceased.objects.filter(reason_of_death=4).count()
    return murdered


def get_all_disease():
    disease = MemberDeceased.objects.filter(reason_of_death=5).count()
    return disease


def get_all_not_known():
    not_known = MemberDeceased.objects.filter(reason_of_death=6).count()
    return not_known


                # Member Abroad Reasons
def get_all_abroad_for_employment():
    employement = Member.objects.filter(foreign_reason=1).count()
    return employement


def get_all_abroad_for_business():
    business = Member.objects.filter(foreign_reason=2).count()
    return business


def get_all_abroad_for_study():
    study = Member.objects.filter(foreign_reason=3).count()
    return study


def get_all_abroad_for_migration():
    migration = Member.objects.filter(foreign_reason=4).count()
    return migration


                                            # Househead Gender
def get_all_male_househead():
    househead_male = Member.objects.filter(is_hoh=1, gender=1).count()
    return househead_male


def get_all_female_househead():
    househead_female = Member.objects.filter(is_hoh=1, gender=2).count()
    return househead_female


def get_all_other_househead():
    househead_other = Member.objects.filter(is_hoh=1, gender=3).count()
    return househead_other
