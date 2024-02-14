from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def shopping_bag(request):
    """ A view that renders the shopping bag page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """
    A view that handles adding items to cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'{product.title} added to your cart')
        # print(messages.success)
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.title} added to your cart')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)
