from django.urls import path
from . import views

app_name = "tourist_detail"

urlpatterns = [
    #path("", home_page, name="home_page"),
    path("touristdetails/", views.tourist_details_view, name="details"),
]
