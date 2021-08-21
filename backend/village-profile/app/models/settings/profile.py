from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, null=True)
    local_level = models.ForeignKey('LocalLevel', on_delete=models.CASCADE, null=True)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE, null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)

    status = models.IntegerField(null=True)
    created_by = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


#  ALTER TABLE app_advertisement CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
#  python manage.py dumpdata  app.FiscalYear --exclude contenttypes --indent 2 > fiscal_year.json
