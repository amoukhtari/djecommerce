from django.shortcuts import render

from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def products_all(request):
    products = Product.objects.all()
    return render(request, 'catalogue/home.html', {'products': products})
