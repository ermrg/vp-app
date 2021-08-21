from django.contrib.auth.models import User
from django.db import models


class HouseholdWaterSource(models.Model):
    id_string = models.TextField(max_length=500, null=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='water_source', null=True)
    water_source = models.ForeignKey('WaterSource', on_delete=models.CASCADE, null=True)  # Well| NaturalSource| River| Pond

    distance = models.IntegerField(null=True)
    unit = models.IntegerField(null=True)  # 0 = KMeter | 1 = Meter | 2 = Mile
    time = models.IntegerField(null=True)  # in minutes
    has_private_tap = models.BooleanField(default=0)  # True = Yes | False = No

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.water_source


