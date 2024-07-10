from carts.views import cart_add, cart_change, cart_remove
from django.urls import path

app_name = "carts"

urlpatterns = [
    path("cart_add/<int:product_id>/", cart_add, name="cart_add"),
    path("cart_change/<int:product_id>/", cart_change, name="cart_change"),
    path("cart_remove/<int:product_id>/", cart_remove, name="cart_remove"),
]
