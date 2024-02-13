from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    """
    Handles the shopping bag contents
    """

    bag_content = []
    total = 0
    product_count = 0
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'bag_content': bag_content,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context