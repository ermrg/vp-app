from django.contrib.auth.models import User
from django.db import models


class MemberTechnicalSkill(models.Model):

    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=True, related_name='skilled_member')
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)
    skill = models.ForeignKey('TechnicalSkill', on_delete=models.CASCADE, null=True)

    skill_source = models.IntegerField(default=0)  # 0 = self, 1 = from Institute

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

