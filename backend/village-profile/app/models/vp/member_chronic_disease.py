from django.contrib.auth.models import User
from django.db import models


class MemberChronicDisease(models.Model):

    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='ill_member', null=True)
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)

    disease_name = models.CharField(max_length=100, null=True)  # Create disease table
    treatment_status = models.IntegerField(default=0)  # 0=worsen, 1= improvement, 2= cured
    present_status = models.IntegerField(default=0)  # 0=taking medicine, 1=left medicine
    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

