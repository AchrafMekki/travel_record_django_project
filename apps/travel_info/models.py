from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

# class TravelInfoManager(models.Manager):
#     # self = Book.objects
#     def get_travel_info_by_ratings(self, *ratings):
#         return self.filter(ratings__name__in=ratings)


class SatisfactionLevel(models.Model):
    SATISFACTION_CHOICE = {
        "Very Unsatisfied": "Very Unsatisfied",
        "Unsatisfied": "Unsatified",
        "Neutral": "Neutral",
        "Satisfied": "Satisfied",
        "Very Satisfied": "Very Satisfied",
    }
    satisfaction_id = models.AutoField(primary_key=True)
    satisfaction_value = models.CharField(
        max_length=20, choices=SATISFACTION_CHOICE, default="Neutral", null=False
    )

    def __str__(self):
        return self.satisfaction_value


# class Rating(models.Model):
#     RATING_CHOICES = {
#         "1 Star": "1 Star",
#         "2 Stars": "2 Stars",
#         "3 Stars": "3 Stars",
#         "4 Stars": "4 Stars",
#         "5 Stars": "5 Stars",
#     }

#     rating_id = models.AutoField(primary_key=True)
#     rating_value = models.CharField(max_length=50, choices=RATING_CHOICES, null=True, blank=True)

#     def __str__(self) -> str:
#         return self.rating_value


class TravelInfo(models.Model):
    CURRENCY_CHOICE = {
      'EUR': 'EUR',
      'USD': 'USD',
      'CHF': 'CHF',
      'GBP': 'GBP',
      'other': 'other',
    }

    TRIP_CHOICE = {
        'Vacation': 'Vacation',
        'Business': 'Business',
        'Personal': 'Personal',
        'other': 'other'
    }

    RATING_CHOICES = {
        "1 Star": "1 Star",
        "2 Stars": "2 Stars",
        "3 Stars": "3 Stars",
        "4 Stars": "4 Stars",
        "5 Stars": "5 Stars",
    }
    DURATION_CHOICES = {
        "1-3 days": "1-3 days",
        "4-7 days": "4-7 days",
        "1-2 weeks": "1-2 weeks",
        "2-4 weeks": "2-4 weeks",
        "1-3 months": "1-3 months",
        "3-6 months": "3-6 months",
        "6-12 months": "6-12 months",
        "more than a year": "More than a year",
    }
    ACCOMMODATION_CHOICES = [
        ('Hotel', 'Hotel'),
        ('Airbnb', 'Airbnb'),
        ('Hostel', 'Hostel'),
        ('Guesthouse', 'Guesthouse'),
        ('Other', 'Other'),
    ]
    travel_id = models.AutoField(primary_key=True)
    first_name = models.ForeignKey(
        "tourist_detail.TouristDetails",
        on_delete=models.CASCADE,
        related_name="travel_infos",
    )
    country = models.ForeignKey(
        "country.Country", on_delete=models.CASCADE, related_name="travel_infos"
    )
    city = models.ForeignKey(
        "city.City", on_delete=models.CASCADE, default="1", related_name="travel_infos"
    )
    date = models.DateField()
    accommodation_name = models.CharField(
        max_length=30, null=True, blank=True
    )
    accommodation_type = models.CharField(
        max_length=15, choices=ACCOMMODATION_CHOICES, default="Hotel"
    )
    transportation = ArrayField(models.CharField(max_length=40), null=True, blank=True)
    total_duration = models.CharField(
        max_length=20, choices=DURATION_CHOICES, default="1-3 days"
    )
    total_cost = models.IntegerField()
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICE, default='EUR')
    trip_type = models.CharField(max_length=15, choices=TRIP_CHOICE, default='Vacation')
    preferred_language = models.CharField(max_length=30, null=True, blank=True)
    rating = models.CharField(max_length=50, choices=RATING_CHOICES, default='1')
    satisfaction_level = models.ManyToManyField('travel_info.SatisfactionLevel')

    # Override objects with new Manager
    # objects = TravelInfoManager()

    def __str__(self):
        return f" {self.travel_id} "

    class Meta:
        ordering = ("first_name",)
        # <app>_<model>
        default_related_name = "%(app_label)s_%(model_name)s"
        verbose_name = "Travel Info"
        verbose_name_plural = "Travel Infos"
