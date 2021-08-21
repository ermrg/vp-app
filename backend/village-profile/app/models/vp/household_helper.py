from django.contrib.auth.models import User
from django.db import models

from app.models import Gender


class HouseholdHelper(models.Model):
    id_string = models.TextField(max_length=500, null=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='household_helper', null=True)

    child_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, null=True)
    start_date_ad = models.DateField(null=True)
    start_date_bs = models.CharField(max_length=100, null=True)
    child_labor_status = models.BooleanField(default=0)  # True = self kept | False = send to others

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.child_name


