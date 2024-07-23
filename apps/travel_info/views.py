from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def travel_info(request):
    return render(request, "info.html")


# class TravelView(TemplateView):
#     template_name = "tourist_detail/details_html"
