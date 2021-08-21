from django.contrib.auth.models import User
from django.db import models


class HouseholdSewage(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)
    toilet_type = models.ForeignKey('ToiletType', on_delete=models.CASCADE, null=True)
    sewage_type = models.ForeignKey('SewageType', on_delete=models.CASCADE, null=True)

    is_available = models.BooleanField(default=0)  # 0 = Yes | 1 = No

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.toilet_type


