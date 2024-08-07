import uuid
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.db.models import Sum
from products.models import Product
from profiles.models import UserProfile

# Create your models here.
STATUS = (
    ("in_progress", "In Progress"),
    ("finished", "Finished"),
    ("cancelled", "Cancelled"),
)


class Order(models.Model):
    """
    Define the data fields for an order
    """
    order_number = models.CharField(max_length=40, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    town_or_city = models.CharField(max_length=30, null=False, blank=False)
    street_address1 = models.CharField(max_length=60, null=False, blank=False)
    street_address2 = models.CharField(max_length=60, null=True, blank=True)
    county = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    def _generate_order_number(self):
        """
        Generate a random unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update the total every time an item is added"""
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Define the data fields for an order line item
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """Set the line item total"""
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU{self.product.sku} on order {self.order.order_number}"


class OrderStatus(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, null=True, blank=True, choices=STATUS,
        default=STATUS[0][0]
    )

    def __str__(self):
        return f"{self.order.order_number} - {self.status}"
