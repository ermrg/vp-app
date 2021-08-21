from django.contrib.auth.models import User
from django.db import models


class MemberForeign(models.Model):

    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='member_foreign', null=True)
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)

    reason = models.ForeignKey('ForeignReason', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    visited_year_ad = models.DateTimeField(auto_now_add=True, null=True)
    visited_year_bs = models.CharField(max_length=100, null=True)
    return_year_ad = models.DateTimeField(auto_now=True, null=True)
    return_year_bs = models.CharField(max_length=100, null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

