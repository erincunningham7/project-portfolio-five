from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Brand
from .forms import ProductForm

# Create your views here.
def all_products(request):
    '''
    Render all products on the products page
    '''
    products = Product.objects.all().order_by('-created_on')
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # print(categories)
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)

# def add_product(request):
#     """ Add a product to the store """
#     form = ProductForm()
#     template = 'products/add_product.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)

def add_product(request):
    '''A view to add products '''
    if not request.user.is_superuser:
        messages.error(request, 'You need admin rights to access this page')
        return redirect('home')

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('product', product.id)
        else:
            messages.error(request, 'Invalid form. Try again')
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)