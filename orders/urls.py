from orders.views import create_order
from django.urls import path

app_name = "orders"

urlpatterns = [
    path("create-order/", create_order, name="create_order"),
]
