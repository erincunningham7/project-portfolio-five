from django import forms
from .models import Order, OrderStatus


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "phone_number",
            "email",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = ("status",)
