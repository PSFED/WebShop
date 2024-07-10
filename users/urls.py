from users.views import profile, registration, login, logout, users_cart
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("users-cart/", users_cart, name="users_cart"),
    path("logout/", logout, name="logout"),
]
