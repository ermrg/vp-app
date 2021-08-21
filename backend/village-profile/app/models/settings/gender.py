
from django.db import models


class Gender (models.Model):

    name = models.CharField(max_length=200, null=True)

    remarks = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)