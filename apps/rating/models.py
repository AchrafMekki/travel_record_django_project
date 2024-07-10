from typing import Any
from django.db import models

# Create your models here.

class Rating(models.Model):
    RATING_CHOICES = {
        '1 Star': '1 Star',
        '2 Stars': '2 Stars',
        '3 Stars': '3 Stars',
        '4 Stars': '4 Stars',
        '5 Stars': '5 Stars',
    }

    rating_id = models.AutoField(primary_key=True)
    rating_value = models.CharField(max_length=50, null=True, blank=True, choices=RATING_CHOICES, default='Neutral')

    def __str__(self) -> str:
        return self.rating_value
