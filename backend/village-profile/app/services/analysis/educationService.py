from app.models.vp.member import Member


# Education Status Male
def get_all_male_studying():
    male_studying = Member.objects.filter(education_status=1, gender=1).count()
    return male_studying


def get_all_male_left_study():
    male_left_study = Member.objects.filter(education_status=2, gender=1).count()
    return male_left_study


def get_all_male_study_completed():
    male_study_completed = Member.objects.filter(education_status=3, gender=1).count()
    return male_study_completed


def get_all_male_no_study():
    male_no_study = Member.objects.filter(education_status=4, gender=1).count()
    return male_no_study


# Education Status female
def get_all_female_studying():
    female_studying = Member.objects.filter(education_status=1, gender=2).count()
    return female_studying


def get_all_female_left_study():
    female_left_study = Member.objects.filter(education_status=2, gender=2).count()
    return female_left_study


def get_all_female_study_completed():
    female_study_completed = Member.objects.filter(education_status=3, gender=2).count()
    return female_study_completed


def get_all_female_no_study():
    female_no_study = Member.objects.filter(education_status=4, gender=2).count()
    return female_no_study


# Education Status
def get_all_studying():
    studying = Member.objects.filter(education_status=1).count()
    return studying


def get_all_left_study():
    left_study = Member.objects.filter(education_status=2).count()
    return left_study


def get_all_study_completed():
    study_completed = Member.objects.filter(education_status=3).count()
    return study_completed


def get_all_no_study():
    no_study = Member.objects.filter(education_status=4).count()
    return no_study


#  Education Level
def get_all_primary_level():
    primary_level = Member.objects.filter(education_status=1).count()
    return primary_level


def get_all_pre_primary_level():
    pre_primary_level = Member.objects.filter(education_status=2).count()
    return pre_primary_level


def get_all_secondary_level():
    secondary_level = Member.objects.filter(education_status=3).count()
    return secondary_level


def get_all_bachelor_level():
    bachelor_level = Member.objects.filter(education_status=4).count()
    return bachelor_level


def get_all_degree_level():
    degree_level = Member.objects.filter(education_status=5).count()
    return degree_level


def get_all_master_phd_level():
    master_phd_level = Member.objects.filter(education_status=6).count()
    return master_phd_level


def get_all_high_school_level():
    high_school_level = Member.objects.filter(education_status=7).count()
    return high_school_level


def get_all_normal_read_write():
    normal_read_write = Member.objects.filter(education_status=8).count()
    return normal_read_write


def get_all_illiterate():
    illiterate = Member.objects.filter(education_status=9).count()
    return illiterate


                        # Technical Training skill
def get_all_electrician():
    electrician = Member.objects.filter(technical_skill=1).count()
    return electrician


def get_all_mason():  # mason = डकर्मी
    mason = Member.objects.filter(technical_skill=2).count()
    return mason


def get_all_painter():
    painter = Member.objects.filter(technical_skill=3).count()
    return painter


def get_all_plumber():
    plumber = Member.objects.filter(technical_skill=4).count()
    return plumber


def get_all_carpenter():  # सिकर्मी
    carpenter = Member.objects.filter(technical_skill=5).count()
    return carpenter


def get_all_tech_and_information():
    tech_and_information = Member.objects.filter(technical_skill=6).count()
    return tech_and_information


def get_all_knitting_stitch():   # सिलाई बुनााई
    knitting_stitch = Member.objects.filter(technical_skill=7).count()
    return knitting_stitch


def get_all_other_skills():
    other_skills = Member.objects.filter(technical_skill=8).count()
    return other_skills
