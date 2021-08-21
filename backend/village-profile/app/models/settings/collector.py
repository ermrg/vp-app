from django.contrib.auth.models import User
from django.db import models


class Collector (models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=10, null=True)
    status = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
