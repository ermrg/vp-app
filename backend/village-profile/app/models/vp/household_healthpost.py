from django.contrib.auth.models import User
from django.db import models


class HouseholdHealthPost(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    household = models.ForeignKey('Household', on_delete=models.CASCADE, related_name='health_post', null=True)

    time = models.IntegerField(null=True)   # in minutes
    distance = models.IntegerField(null=True)
    is_available = models.BooleanField(default=0)  # 0 = Yes | 1 = No

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


