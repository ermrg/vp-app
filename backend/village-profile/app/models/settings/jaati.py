from django.contrib.auth.models import User
from django.db import models
from app.models.settings.religion import Religion


class Jaati (models.Model):
    name = models.CharField(max_length=100, null=True)
    status = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name