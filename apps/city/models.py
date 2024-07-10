from django.db import models

# Create your models here.


class City(models.Model):
    city_id = models.AutoField(primary_key=True)  # SERIAL PRIMARY KEY
    country_id = models.ForeignKey('country.Country', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name
