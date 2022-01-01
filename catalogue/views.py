from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def products_all(request):
    products = Product.objects.all()
    return render(request, 'catalogue/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'catalogue/products/detail.html', {'product': product})
