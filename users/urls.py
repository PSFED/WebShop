from users.views import (
    UpdateView,
    UserRegistrationView,
    UserLoginView,
    logout,
    UserCartView,
)
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("profile/", UpdateView.as_view, name="profile"),
    path("users-cart/", UserCartView.as_view(), name="users_cart"),
    path("logout/", logout, name="logout"),
]
