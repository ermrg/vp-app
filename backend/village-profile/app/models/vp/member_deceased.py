from django.contrib.auth.models import User
from django.db import models

from app.models import Gender


class MemberDeceased (models.Model):

    id_string = models.TextField(max_length=500, null=True)
    hh_id_string = models.TextField(max_length=500, null=True)

    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='deceased_member', null=True)
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)
    reason_of_death = models.ForeignKey('DeathReason', on_delete=models.CASCADE, null=True)

    year_of_death_ad = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, default=1)
    year_of_death_bs = models.CharField(max_length=100)
    month_of_death = models.IntegerField(default=0)
    age_on_death = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

