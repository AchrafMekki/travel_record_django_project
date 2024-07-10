from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class TouristDetails(models.Model):
    GENDER_CHOICES = {
        'Male': 'Male',
        'Female': 'Female',
        'Other': 'Other'
    }
    tourist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    language = ArrayField(models.CharField(max_length=20), blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
