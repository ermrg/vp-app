from django.contrib.auth.models import User
from django.db import models


class HouseholdIncome(models.Model):

    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='household_income', null=True)
    source = models.ForeignKey('IncomeSource', on_delete=models.CASCADE, null=True)

    start_date_ad = models.DateTimeField(null=True)
    start_date_bs = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(null=True)  

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.source


