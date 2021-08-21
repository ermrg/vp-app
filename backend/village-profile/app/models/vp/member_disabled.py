from django.contrib.auth.models import User
from django.db import models

from app.models import DisabilityCard


class MemberDisability(models.Model):

    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='disabled_member', null=True)
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)
    disability_type = models.ForeignKey('DisabilityType', on_delete=models.CASCADE, null=True)

    has_card = models.BooleanField(default=0)
    card_type = models.ForeignKey(DisabilityCard, on_delete=models.DO_NOTHING, default=1)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

