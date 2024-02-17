from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag!")
        return redirect(reverse('products'))

    order_form  = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OkqHnJahViFrfWPb64e2Uwm6UQbLBfyAmx6UYy2A9odfSMs9ykJkdvUBq407UPoNxZBbzdUnHvhSVwvpc2Xhqnl00SbyeLuRk',
        'client_secret': 'test',
    }
    return render(request, template, context)