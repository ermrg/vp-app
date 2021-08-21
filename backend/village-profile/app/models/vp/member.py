from django.contrib.auth.models import User
from django.db import models

from app.models import DisabilityCard, Gender, DisabilityType, Country, TechnicalSkill, ForeignReason
from app.models.settings.vaccine_name import VaccineName


class Member (models.Model):
    id_string = models.CharField(max_length=500, null=True)
    name_eng = models.CharField(max_length=100, null=True)
    name_nep = models.CharField(max_length=100, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.DO_NOTHING, default=1)
    dob_ad = models.DateTimeField(null=True)
    dob_bs = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True, blank=True)

    hh = models.ForeignKey('Household', on_delete=models.DO_NOTHING, related_name='house', null=True)
    education_status = models.ForeignKey('EducationStatus', on_delete=models.DO_NOTHING, null=True)
    main_occupation = models.ForeignKey('MainOccupation', on_delete=models.DO_NOTHING, null=True)
    citizenship_num = models.CharField(max_length=200, null=True, blank=True)
    relation_with_hoh = models.ForeignKey('RelationWithHoh', on_delete=models.DO_NOTHING, null=True)
    phone_num = models.IntegerField(null=True, blank=True)
    mobile_num = models.CharField(max_length=100, null=True, blank=True)
    is_married = models.IntegerField(null=True)  # 0 = Yes, 1 = No
    monthly_income = models.IntegerField(null=True, blank=True)
    education_level = models.ForeignKey('EducationLevel', on_delete=models.DO_NOTHING, null=True, blank=True)
    marital_status = models.ForeignKey('MaritalStatus', on_delete=models.DO_NOTHING, null=True, blank=True)
    spouse = models.ForeignKey('Member', on_delete=models.DO_NOTHING, related_name='my_spouse', null=True, blank=True)
    guardian = models.ForeignKey('Member', on_delete=models.DO_NOTHING, related_name='my_guardian', null=True, blank=True)
    has_disability = models.IntegerField(default=0, null=True)
    has_chronic_disease = models.IntegerField(default=0, null=True)
    has_technical_training = models.IntegerField(default=0, null=True)
    foreign_stay = models.IntegerField(default=0, null=True)  # 1 = yes, 0 = no
    is_child_marriage = models.IntegerField(default=0, null=True)
    is_vaccinated = models.IntegerField(default=0, null=True)
    is_hoh = models.BooleanField(default=True)
    bank_account = models.IntegerField(null=True)
    disability_card = models.ForeignKey('DisabilityCard', on_delete=models.DO_NOTHING, null=True, blank=True)
    disability_type = models.ForeignKey('DisabilityType', on_delete=models.DO_NOTHING, null=True, blank=True)
    country_visited = models.ForeignKey('Country', on_delete=models.DO_NOTHING, null=True, blank=True)
    technical_skill = models.ForeignKey('TechnicalSkill', on_delete=models.DO_NOTHING, null=True, blank=True)
    vaccine_name = models.ForeignKey('VaccineName', on_delete=models.DO_NOTHING, null=True, blank=True)
    foreign_reason = models.ForeignKey('ForeignReason', on_delete=models.DO_NOTHING, null=True, blank=True)
    disease_name = models.CharField(max_length=200, null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name_nep


