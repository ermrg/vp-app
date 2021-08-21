from django.contrib.auth.models import User
from app.models.settings.province import Province
from app.models.settings.district import District
from app.models.settings.local_level import LocalLevel
from app.models.settings.ward import Ward
from django.db import models


class Basti (models.Model):
    name = models.CharField(max_length=100, null=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING, null=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, null=True)
    local_level = models.ForeignKey(LocalLevel, on_delete=models.DO_NOTHING, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.DO_NOTHING, null=True)

    status = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
