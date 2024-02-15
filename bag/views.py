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

def update_bag(request, item_id):
    """Change the quantity of bag items"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
        else:
            del bag[item_id]
            if not bag[item_id]:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove an item from the bag"""

    if quantity === 0:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        messages.success(request, f'{product.title} removed from your cart')