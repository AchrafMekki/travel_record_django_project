from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def travel_info(request):
    return render(request, "info.html")


class OurStory(TemplateView):
     template_name = "about_us.html"
