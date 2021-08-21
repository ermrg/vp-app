from django.contrib.auth.models import User
from django.db import models


class HouseholdVehicle(models.Model):
    household = models.ForeignKey('Household', on_delete=models.CASCADE, null=True, related_name='vehicle')
    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=True)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE, null=True)

    is_available = models.BooleanField(default=0)  # True = Yes | False = No
    count = models.IntegerField(null=True)

    status = models.IntegerField(null=True)
    remarks = models.CharField(null=True, max_length=200)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.remarks


