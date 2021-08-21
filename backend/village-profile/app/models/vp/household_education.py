from django.contrib.auth.models import User
from django.db import models


class HouseholdEducation(models.Model):
    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='household_education', null=True)

    primary_distance = models.IntegerField(null=True)  # distance taken from home to primary level school
    secondary_distance = models.IntegerField(null=True)  # distance taken from home to secondary level school
    higher_secondary_distance = models.IntegerField(null=True)  # distance taken from home to higher sec. level school

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.primary_distance


