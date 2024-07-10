from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)  # SERIAL PRIMARY KEY
    country_name = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.country_name
