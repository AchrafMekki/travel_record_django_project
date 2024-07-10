from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class TravelInfo(models.Model):
    CURRENCY_CHOICE = {
        
      'EUR' : 'EUR',
      'USD' : 'USD',
      'CHF' : 'CHF',
      'GBP' : 'GBP',
      'other' : 'other',
    }

    TRIP_CHOICE = {
        'Vacation' : 'Vacation',
        'Business' : 'Business',
        'Personal' : 'Personal',
        'other' : 'other'
    }

    travel_id = models.AutoField(primary_key=True)
    tourist = models.ForeignKey('tourist_detail.TouristDetails', on_delete=models.CASCADE)
    country = models.ForeignKey('country.Country', on_delete=models.CASCADE)
    date = models.DateField()
    hotel = models.CharField(max_length=30, null=True, blank=True)
    transportation = ArrayField(models.CharField(max_length=40), null=True, blank=True)
    total_duration = models.DurationField()
    total_cost = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICE, default='EUR')
    trip_type = models.CharField(max_length=15, choices=TRIP_CHOICE, default='Vacation')
    preferred_language = models.CharField(max_length=30, null=True, blank=True)
    rating = models.ForeignKey('rating.Rating', on_delete=models.CASCADE)
    satisfaction_level = models.ForeignKey('satisfaction_level.SatisfactionLevel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Travel {self.travel_id} by {self.tourist}"