from django.urls import path, include
from . import views


app_name = "travel_info"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("travelinfo/", views.travel_info, name="info")
    # path("tourist/", TravelView.as_view(), name="tourist"),
]
