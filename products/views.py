from django.shortcuts import render
from .models import Product, Category, Brand

# Create your views here.
def all_products(request):
    '''
    Render all products on the products page
    '''
    products = Product.objects.all().order_by('-created_on')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)