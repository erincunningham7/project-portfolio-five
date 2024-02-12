from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Brand

# Create your views here.
def all_products(request):
    '''
    Render all products on the products page
    '''
    products = Product.objects.all().order_by('-created_on')
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything yet!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)