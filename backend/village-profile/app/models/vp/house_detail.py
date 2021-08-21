from django.contrib.auth.models import User
from django.db import models


class HouseDetail(models.Model):
    id_string = models.TextField(max_length=500, null=True)

    hh = models.ForeignKey('Household', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='member', null=True)
    house_type = models.ForeignKey('HouseType', on_delete=models.CASCADE, null=True)
    roof_type = models.ForeignKey('RoofType', on_delete=models.CASCADE, null=True)

    house_num = models.IntegerField(null=True)
    map_pass = models.NullBooleanField(default=0)  # 0 = Yes, 1 = No
    map_pass_date_ad = models.DateField(null=True)
    map_pass_date_bs = models.CharField(max_length=100, null=True)

    build_year_ad = models.DateField(null=True)
    build_year_bs = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.house_type

