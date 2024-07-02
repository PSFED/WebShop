from main.views import index, about
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
]
