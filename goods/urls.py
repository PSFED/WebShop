from goods.views import ProductView, CatalogView
from django.urls import path

app_name = "goods"

urlpatterns = [
    path("search/", CatalogView.as_view(), name="search"),
    path("<slug:category_slug>/", CatalogView.as_view(), name="index"),
    path("product/<slug:product_slug>/", ProductView.as_view(), name="product"),
]
