from django.contrib.auth.models import User
from django.db import models


class MemberChildMarriage(models.Model):

    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='early_married_member', null=True)
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)

    married_year_ad = models.DateTimeField(auto_now=True, null=True)
    married_year_bs = models.CharField(max_length=100)
    age_on_married = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

