from django.contrib.auth.models import User
from django.db import models


class Household(models.Model):

    RESIDENT_CHOICES = (
        ('जन्मसिद्ध', 'from_birth'),
        ('बसाईसराई', 'migrated'),
    )

    id_string = models.TextField(max_length=500, null=True)

    hoh_name = models.CharField(max_length=50, null=True)
    hoh = models.ForeignKey('Member', on_delete=models.DO_NOTHING, related_name='dead', null=True)
    province = models.ForeignKey('Province', on_delete=models.DO_NOTHING, null=True)
    district = models.ForeignKey('District', on_delete=models.DO_NOTHING, null=True)
    local_level = models.ForeignKey('LocalLevel', on_delete=models.DO_NOTHING, null=True)
    ward = models.ForeignKey('Ward', on_delete=models.DO_NOTHING, null=True)
    basti = models.ForeignKey('Basti', on_delete=models.DO_NOTHING, null=True)
    marga = models.ForeignKey('Marga', on_delete=models.DO_NOTHING, null=True)
    religion = models.ForeignKey('Religion', on_delete=models.DO_NOTHING, null=True)
    jaati = models.ForeignKey('Jaati', on_delete=models.DO_NOTHING, null=True)
    mother_tongue = models.ForeignKey('MotherTongue', on_delete=models.DO_NOTHING, null=True)
    main_occupation = models.ForeignKey('MainOccupation', on_delete=models.DO_NOTHING, null=True)

    has_bank_acc = models.IntegerField(default=0)
    has_cooperative_acc = models.IntegerField(default=0)
    has_garden = models.IntegerField(default=0)
    member_with_life_insurance = models.IntegerField(null=True)
    member_with_health_insurance = models.IntegerField(null=True)
    responder_name = models.CharField(max_length=200, null=True)
    house_num = models.IntegerField(null=True)
    num_of_member = models.IntegerField(null=True)
    resident_type = models.CharField(max_length=14, choices=RESIDENT_CHOICES, default='जन्मसिद्ध')
    phone_num = models.BigIntegerField(null=True)
    mobile_num = models.BigIntegerField(null=True)
    longitude = models.DecimalField(decimal_places=5, max_digits=12, null=True)
    latitude = models.DecimalField(decimal_places=5, max_digits=12, null=True)
    geo_location = models.CharField(max_length=500, null=True)
    altitude = models.DecimalField(decimal_places=5, max_digits=12, null=True)
    accuracy = models.DecimalField(decimal_places=5, max_digits=12, null=True)
    responder_image = models.ImageField(upload_to='image', null=True)

    step = models.IntegerField(default=1)
    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.hoh_name
