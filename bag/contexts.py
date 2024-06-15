from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Handles the shopping bag contents
    """

    bag_content = []
    total = 0
    product_count = 0
    delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery_cost + total
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_content.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
            }
        )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery_cost = 0
        free_delivery_delta = 0

    grand_total = delivery_cost + total

    context = {
        "bag_content": bag_content,
        "total": total,
        "product_count": product_count,
        "delivery_cost": delivery_cost,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
