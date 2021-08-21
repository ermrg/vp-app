from django.contrib.auth.models import User
from django.db import models


class HouseholdNaturalDisaster(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)

    disaster = models.ForeignKey('Disaster', on_delete=models.CASCADE, null=True)
    house_damage_status = models.ForeignKey('HouseDamageStatus', on_delete=models.CASCADE, null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.disaster


