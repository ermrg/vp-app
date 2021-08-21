from django.contrib.auth.models import User
from django.db import models


class RentMember(models.Model):

    id_string = models.TextField(max_length=500, null=True)
    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)

    rent_member_head = models.CharField(max_length=100, null=True)
    room_no = models.IntegerField(null=True)
    migrated_from = models.BooleanField(default=0)  # 0 = inside city, 1 = outside city
    no_of_member = models.IntegerField(null=True)
    reason_for_migration = models.TextField(max_length=500, null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.rent_member_head

