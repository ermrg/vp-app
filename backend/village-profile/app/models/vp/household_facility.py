from django.contrib.auth.models import User
from django.db import models


class HouseholdFacility(models.Model):
    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='facility', null=True)
    name = models.ForeignKey('Facility', on_delete=models.CASCADE, null=True)  # Internet| MobilePhone| Electricity| DrinkingWater

    count = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)  # True = Yes | False = No

    status = models.IntegerField(null=True)
    remarks = models.CharField(max_length=200, null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


