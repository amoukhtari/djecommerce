from django.shortcuts import render

from .models import Category, Product

def products_all(request):
    products = Product.objects.all()
    return render(request, 'catalogue/home.html', {'products': products})