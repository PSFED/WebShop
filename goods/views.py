from django.shortcuts import render


def catalog(request):
    content = {}
    return render(request, "goods/catalog", content)


def product(request):
    content = {}
    return render(request, "goods/product", content)
