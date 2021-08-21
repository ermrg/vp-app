from django.contrib.auth.models import User
from django.db import models


class FiscalYear(models.Model):
    year = models.CharField(max_length=50)
    code = models.CharField(max_length=10, null=True)

    start_date_ad = models.DateTimeField(null=True)
    end_date_ad = models.DateTimeField(null=True)

    start_date_bs = models.CharField(null=True, max_length=20)
    end_date_bs = models.CharField(null=True, max_length=20)

    status = models.IntegerField(null=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.code
