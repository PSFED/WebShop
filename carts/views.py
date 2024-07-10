from django.shortcuts import render


def cart_add(request, product_id):
    context = {}
    return render(request, ".html", context)


def cart_change(request, product_id):
    context = {}
    return render(request, ".html", context)


def cart_remove(request, product_id):
    context = {}
    return render(request, ".html", context)
