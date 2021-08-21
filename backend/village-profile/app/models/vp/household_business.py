from django.contrib.auth.models import User
from django.db import models


class HouseholdBusiness(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='household_business', null=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='member_business', null=True)
    business_type = models.ForeignKey('BusinessType', on_delete=models.CASCADE, null=True)  # Agriculture | Meat Shop | Fancy Shop

    business_place = models.CharField(max_length=150, null=True)
    is_registered = models.BooleanField(default=0)  # True = Yes | False = No
    money_invested = models.IntegerField(null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.business_type


