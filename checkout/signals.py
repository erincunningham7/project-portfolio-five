from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order, OrderLineItem, OrderStatus

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update 
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()

@receiver(post_save, sender=Order)
def create_order_status(sender, instance, created, **kwargs):
    ''' Create OrderStatus when Order is created'''
    if created:
        OrderStatus.objects.create(order=instance)