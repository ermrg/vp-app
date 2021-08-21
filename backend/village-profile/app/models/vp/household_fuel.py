from django.contrib.auth.models import User
from django.db import models


class HouseholdFuel(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='fuel', null=True)
    light_fuel = models.ForeignKey('LightFuel', on_delete=models.CASCADE ,null=True)  # Solar| LocalLine| Kerosene| NationalLine
    cooking_fuel = models.ForeignKey('CookingFuel', on_delete=models.CASCADE, null=True)  # Wood| LP Gas| Electricity| Kerosene
    garbage_management = models.ForeignKey('GarbageManagement', on_delete=models.CASCADE, null=True)  # ManagedInHome| River| DisposalPalace|

    is_available = models.BooleanField(default=0)  # 0 = Yes | 1 = No

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.light_fuel


