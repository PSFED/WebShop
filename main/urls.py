from main.views import AboutView, IndexView
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
]
