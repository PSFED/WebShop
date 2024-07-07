from goods.views import catalog, product
from django.urls import path

app_name = "goods"

urlpatterns = [
    path("<slug:category_slug>/", catalog, name="index"),
    path("product/<slug:product_slug>/", product, name="product"),
]
# <slug:slug>
