from django.contrib import admin
from .models import TouristDetails

# Register your models here.


class TouristAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "nationality", "occupation")


admin.site.register(TouristDetails, TouristAdmin)
