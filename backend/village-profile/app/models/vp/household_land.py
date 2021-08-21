from django.contrib.auth.models import User
from django.db import models


class HouseholdLand(models.Model):

    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, null=True, related_name='land')
    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=True, related_name='member_land')
    land_type = models.ForeignKey('LandType', on_delete=models.CASCADE, null=True)  # Khet | Bari

    area1 = models.IntegerField(null=True)  # Ropani
    area2 = models.IntegerField(null=True)  # Aana
    area3 = models.IntegerField(null=True)  # Paisa
    area4 = models.IntegerField(null=True)  # Daam
    kitta_no = models.IntegerField(null=True)  # Management | Science | Music
    garden = models.IntegerField(null=True)  #
    irrigation = models.BooleanField(null=True)  # 1 = Yes | 0 = No

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.land_type
