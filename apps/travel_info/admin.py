from django.contrib import admin
from .models import TravelInfo, SatisfactionLevel

# Register your models here.


class TravelInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "country", "date")


admin.site.register(TravelInfo, TravelInfoAdmin)
# admin.site.register(Rating)
admin.site.register(SatisfactionLevel)
