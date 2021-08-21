from django.contrib.auth.models import User
from django.db import models


class HouseholdAnimal(models.Model):
    id_string = models.TextField(max_length=500, null=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE, null=True, related_name='household_animal')
    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=True, related_name='member_animal')
    animal_type = models.ForeignKey('AnimalType', on_delete=models.CASCADE,
                                    null=True)  # cow | Chicken | Goat | Yak | Pig | Horse
    count = models.IntegerField(null=True)

    status = models.IntegerField(null=True)
    remarks = models.TextField(null=True)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.animal_type
