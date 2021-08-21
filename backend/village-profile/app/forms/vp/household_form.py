from django import forms


class HouseholdHouseholdForm1111(forms.Form):
    hoh_name = forms.CharField(required=True, error_messages={'required': 'Head Of House is required'})
    hoh = forms.IntegerField(required=False)
    hh_no = forms.IntegerField(required=True, error_messages={'required': 'Household No is required'})
    no_of_m = forms.IntegerField(required=True, error_messages={'required': 'No of Member is required'})
    contact = forms.CharField(required=True, error_messages={'required': 'Contact is required'})
    basti = forms.CharField(required=True, error_messages={'required': 'Basti is required'})
    ward = forms.CharField(required=True, error_messages={'required': 'ward is required'})
    street = forms.CharField(required=True, error_messages={'required': 'street is required'})
    local_level = forms.IntegerField(required=True, error_messages={'required': 'local level is required'})

    key = forms.CharField(required=False)

    def clean_local_level(self):
        data = self.cleaned_data['local_level']
        if not data:
            forms.ValidationError("Local Level Required")
        return data


class HouseholdDetailForm1111(forms.Form):
    ethnicity = forms.CharField(required=True, error_messages={'required': 'Ethnicity is required'})
    mother_tongue = forms.CharField(required=True, error_messages={'required': 'mother tongue is required'})
    type_of_residence = forms.CharField(required=True, error_messages={'required': 'type of residence is required'})
    bank_account = forms.IntegerField(required=False)
    occupation1 = forms.CharField(required=False)
    occupation2 = forms.CharField(required=False)
    is_migrated = forms.CharField(required=False)
    migration_year = forms.CharField(required=False)
    remarks = forms.CharField(required=False)
    is_married = forms.CharField(required=False)

    def clean_bank_account(self):
        data = self.cleaned_data['bank_account']
        if not data:
            data = 0
        return data

    def clean_is_migrated(self):
        data = self.cleaned_data['is_migrated']
        if not data:
            data = 0
        return data

    def clean_is_married(self):
        data = self.cleaned_data['is_married']
        if not data:
            data = 0
        return data

    def clean_ethnicity(self):
        data = self.cleaned_data['ethnicity']
        if not data:
            data = ''
        return data

    def clean_mother_tongue(self):
        data = self.cleaned_data['mother_tongue']
        if not data:
            data = ''
        return data

    def clean_type_of_residence(self):
        data = self.cleaned_data['type_of_residence']
        if not data:
            data = ''
        return data

    def clean_occupation1(self):
        data = self.cleaned_data['occupation1']
        if not data:
            data = ''
        return data

    def clean_occupation2(self):
        data = self.cleaned_data['occupation2']
        if not data:
            data = ''
        return data

    def clean_remarks(self):
        data = self.cleaned_data['remarks']
        if not data:
            data = ''
        return data


class HouseholdLandForm(forms.Form):
    type = forms.CharField(required=False)
    area = forms.CharField(required=False)
    kitta_no = forms.CharField(required=False)
    garden = forms.IntegerField(required=False)
    irrigation = forms.IntegerField(required=False)
    remarks = forms.CharField(required=False)


class HouseholdAnimalForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': 'Name is required'})
    count = forms.IntegerField(required=True, error_messages={'required': 'Count is required'})
    remarks = forms.CharField(required=False)


class HouseholdInfrastructureForm(forms.Form):
    water = forms.CharField(required=True, error_messages={'required': 'Mention water source or add No'})
    cooking_fuel = forms.CharField(required=True, error_messages={'required': 'Mention cooking fuel source or add No'})
    light_fuel = forms.CharField(required=True, error_messages={'required': 'Mention light fuel source or add No'})  #
    public_transport = forms.CharField(required=True, error_messages={'required': 'Mention public transport or add No'})
    education = forms.CharField(required=True, error_messages={'required': 'Mention education or add No'})
    hospital = forms.CharField(required=True, error_messages={'required': 'Mention hospital or add No'})
    sewage = forms.CharField(required=True, error_messages={'required': 'Mention sewage or add No'})
    toilet = forms.CharField(required=True, error_messages={'required': 'Mention toilet or add No'})
    remarks = forms.CharField(required=False)


class HouseholdEarthquakeStatusForm(forms.Form):
    damage = forms.CharField(required=False)
    rebuild = forms.CharField(required=False)
    donation = forms.CharField(required=False)
    remarks = forms.CharField(required=False)


class HouseholdOtherForm(forms.Form):
    vehicle = forms.CharField(required=False)
    vehicle_count = forms.IntegerField(required=False)
    festival = forms.CharField(required=False)
    facility = forms.CharField(required=False)
    facility_count = forms.IntegerField(required=False)
    festival_remarks = forms.CharField(required=False)
    facility_remarks = forms.CharField(required=False)
    vehicle_remarks = forms.CharField(required=False)


class HouseholdDetailForm(forms.Form):
    ward_no = forms.CharField(required=True)
    marg_name = forms.CharField(required=True)
    place_name = forms.CharField(required=True)
    new_place_name = forms.CharField(required=False)
    religion = forms.CharField(required=True)
    caste = forms.CharField(required=True)
    mother_tongue = forms.CharField(required=True)
    main_occupation = forms.CharField(required=True)
    bank_ac = forms.CharField(required=True)
    co_ac = forms.CharField(required=True)
    garden = forms.CharField(required=True)
    life_insurance = forms.IntegerField(required=True)
    health_insurance = forms.IntegerField(required=True)
    responder_name = forms.CharField(required=True)
    house_no = forms.IntegerField(required=True)
    member_no = forms.IntegerField(required=True)
    migration_status = forms.CharField(required=True)
    mobile_no = forms.IntegerField(required=True)
    lat = forms.IntegerField(required=False)
    long = forms.IntegerField(required=False)
    responder_photo = forms.CharField(required=False)

    # def clean_place_name(self):
    #     data = self.cleaned_data['place_name']
    #     new_place_name = self.cleaned_data['new_place_name']
    #     if not data:
    #         data = ''
    #     return data


class HouseholdDeceasedForm(forms.Form):
    expire_mm_name = forms.CharField(required=True)
    expire_mm_age = forms.IntegerField(required=True)
    expire_mm_gender = forms.CharField(required=True)
    expire_mm_month = forms.CharField(required=False)
    expire_mm_gender = forms.IntegerField(required=False)
    expire_reason = forms.CharField(required=False)
    expire_remarks = forms.CharField(required=False)
    other_expire_reason = forms.CharField(required=False)


class HouseheadDisabilityForm(forms.Form):
    owner_disability_type = forms.CharField(required=True)
    owner_disability_card_type = forms.IntegerField(required=True)
    owner_disability_card = forms.CharField(required=True)


class HouseholdOwnerForm(forms.Form):
    owner_name = forms.CharField(required=True)
    owner_gender = forms.IntegerField(required=True)
    owner_dob = forms.DateField(required=True)
    owner_citizen = forms.CharField(required=False)
    owner_contact = forms.IntegerField(required=False)
    owner_edu_status = forms.CharField(required=False)
    owner_edu_level = forms.CharField(required=False)
    owner_profession = forms.CharField(required=False)
    owner_monthly_salary = forms.IntegerField(required=False)
    owner_marital_status = forms.CharField(required=False)


class MemberForm(forms.Form):
    mem_name = forms.CharField(required=True)
    mem_gender = forms.IntegerField(required=True)
    mem_dob = forms.DateField(required=True)
    mem_citizen = forms.CharField(required=False)
    mem_contact = forms.IntegerField(required=False)
    mem_edu_status = forms.CharField(required=False)
    mem_edu_level = forms.CharField(required=False)
    mem_profession = forms.CharField(required=False)
    mem_monthly_salary = forms.IntegerField(required=False)
    mem_marital_status = forms.CharField(required=False)
    relation_with_owner = forms.CharField(required=False)


class HouseDetailForm(forms.Form):
    house_no = forms.IntegerField(required=True)
    home_type = forms.CharField(required=True)
    roof_type = forms.CharField(required=True)
    construct_year = forms.DateField(required=True)
    home_design = forms.IntegerField(required=False)
    home_design_date = forms.DateField(required=True)
    home_owner = forms.CharField(required=False)
    home_image = forms.ImageField(required=False)


class RentMemberForm(forms.Form):
    rent_member_owner_name = forms.CharField(required=True)
    rent_member_from_place = forms.CharField(required=True)
    rent_member_count = forms.IntegerField(required=False)
    rent_member_room_count = forms.IntegerField(required=False)
    rent_member_reason = forms.CharField(required=False)


class LandDetailsForm(forms.Form):
    land_type = forms.CharField(required=True)
    land_area1 = forms.IntegerField(required=True)
    land_area2 = forms.IntegerField(required=True)
    land_area3 = forms.IntegerField(required=False)
    land_area4 = forms.IntegerField(required=True)
    irrigation_facility = forms.BooleanField(required=False)
    kitta_no = forms.IntegerField(required=True)
    land_remarks = forms.CharField(required=False)


class AnimalDetailsForm(forms.Form):
    animal_count = forms.IntegerField(required=True)
    animal_type = forms.CharField(required=True)
    animal_remarks = forms.CharField(required=False)


class BusinessDetailsForm(forms.Form):
    business_type = forms.CharField(required=True)
    reg_status = forms.BooleanField(required=True)
    money_spend = forms.IntegerField(required=True)
    business_location = forms.CharField(required=False)
    business_remarks = forms.CharField(required=False)


class FestivalForm(forms.Form):
    festival_name = forms.CharField(required=False)
    festival_remarks = forms.CharField(required=False)


class HelperForm(forms.Form):
    helper_name = forms.CharField(required=False)
    helper_status = forms.BooleanField(required=False)
    helper_fromdate = forms.DateField(required=False)
    helper_remarks = forms.CharField(required=False)
    helper_gender = forms.CharField(required=False)
    helper_age = forms.IntegerField(required=False)


class FamilyIncomeForm(forms.Form):
    earning_source = forms.CharField(required=False)
    earning_amount = forms.IntegerField(required=False)
    earning_from = forms.DateField(required=False)
    earning_remarks = forms.CharField(required=False)


class FamilyExpensesForm(forms.Form):
    expense_food = forms.IntegerField(required=False)
    expense_health = forms.IntegerField(required=False)
    expense_education = forms.IntegerField(required=False)
    expense_other = forms.IntegerField(required=False)
    expense_remarks = forms.CharField(required=False)


class VehicleDetailForm(forms.Form):
    vehicles_type = forms.CharField(required=True)
    vehicles_availability = forms.BooleanField(required=True)
    vehicles_count = forms.IntegerField(required=False)
    vehicles_remarks = forms.CharField(required=False)


class OtherFacilityForm(forms.Form):
    facility_name = forms.CharField(required=False)
    facility_availability = forms.BooleanField(required=False)
    facility_count = forms.IntegerField(required=False)
    facility_remarks = forms.CharField(required=False)


class HouseholdInfrastructureForm(forms.Form):
    water_source = forms.CharField(required=False)
    tap_type = forms.BooleanField(required=False)
    water_distance = forms.IntegerField(required=False)
    water_distance_unit = forms.CharField(required=False)
    water_time = forms.IntegerField(required=False)
    fuel_light = forms.CharField(required=False)
    fuel_cooking = forms.CharField(required=False)
    fuel_garbage = forms.CharField(required=False)
    trans_distance = forms.IntegerField(required=False)
    trans_possi_distance = forms.IntegerField(required=False)
    road_width = forms.IntegerField(required=False)
    edu_prim_distance = forms.IntegerField(required=False)
    edu_sec_distance = forms.IntegerField(required=False)
    edu_higsec_distance = forms.IntegerField(required=False)
    health_distance = forms.IntegerField(required=False)
    health_time = forms.IntegerField(required=False)
    toilet_type = forms.CharField(required=False)
    sewage_type = forms.CharField(required=False)
    disaster = forms.CharField(required=False)
    current_state = forms.CharField(required=False)



