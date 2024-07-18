from django.db import models
from users.models import User

class Pet(models.Model):
    PET_TYPE_CHOICES = [
        ('dog', '강아지'),
        ('cat', '고양이'),
    ]

    user = models.ForeignKey(User, related_name='pets', on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    pet_name = models.CharField(max_length=20)
    pet_age = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.pet_name} ({self.pet_type})"



