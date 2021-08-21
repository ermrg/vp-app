from django.contrib.auth.models import User
from django.db import models


class HouseholdInfrastructure(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='infrastructure', null=True)
    household_education = models.ForeignKey('HouseholdEducation', on_delete=models.CASCADE,
                                            related_name='infrastructure_education', null=True)
    household_fuel = models.ForeignKey('HouseholdFuel', on_delete=models.CASCADE,
                                       related_name='infrastructure_fuel', null=True)
    household_healthpost = models.ForeignKey('HouseholdHealthPost', on_delete=models.CASCADE,
                                             related_name='infrastructure_healthpost', null=True)
    household_public_transport = models.ForeignKey('HouseholdPublicTransport', on_delete=models.CASCADE,
                                                   related_name='infrastructure_public_transport', null=True)
    household_sewage = models.ForeignKey('HouseholdSewage', on_delete=models.CASCADE,
                                         related_name='infrastructure_sewage', null=True)
    household_watersource = models.ForeignKey('HouseholdWaterSource', on_delete=models.CASCADE,
                                              related_name='infrastructure_water_source', null=True)
    household_natural_disaster = models.ForeignKey('HouseholdNaturalDisaster', on_delete=models.CASCADE,
                                                   related_name='infrastructure_natural_disaster', null=True)
    light_fuel = models.ForeignKey('LightFuel', on_delete=models.CASCADE,
                                   null=True)  # Solar| LocalLine| Kerosene| NationalLine
    cooking_fuel = models.ForeignKey('CookingFuel', on_delete=models.CASCADE,
                                     null=True)  # Wood| LP Gas| Electricity| Kerosene
    garbage_management = models.ForeignKey('GarbageManagement', on_delete=models.CASCADE,
                                           null=True)  # ManagedInHome| River| DisposalPalace|
    water_source = models.ForeignKey('WaterSource', on_delete=models.CASCADE, null=True)  # Well| NaturalSource| River| Pond
    toilet_type = models.ForeignKey('ToiletType', on_delete=models.CASCADE, null=True)
    sewage_type = models.ForeignKey('SewageType', on_delete=models.CASCADE, null=True)
    disaster = models.ForeignKey('Disaster', on_delete=models.CASCADE, null=True)
    house_damage_status = models.ForeignKey('HouseDamageStatus', on_delete=models.CASCADE, null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # def __str__(self):
    #     return self.household_watersource
