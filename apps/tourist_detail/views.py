from django.shortcuts import render
from .models import TouristDetails

# Create your views here.


def tourist_details_view(request):
    tourists = TouristDetails.objects.all()
    return render(request, "tourist_details.html", {"tourists": tourists})
