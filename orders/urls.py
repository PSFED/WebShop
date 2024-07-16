from orders.views import CreateOrderView
from django.urls import path

app_name = "orders"

urlpatterns = [
    path("create-order/", CreateOrderView.as_view(), name="create_order"),
]
