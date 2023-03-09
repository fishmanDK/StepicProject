from django.shortcuts import render
from products.models import *

def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        "title": "Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)