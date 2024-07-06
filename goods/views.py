from django.shortcuts import render

from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    content = {
        "title": "Home - каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", content)


def product(request):
    content = {}
    return render(request, "goods/product.html", content)
