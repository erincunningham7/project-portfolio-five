from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('date','order_number', 'order_total', 'delivery_cost', 'grand_total',)

    field = ('date', 'order_number', 'full_name', 'phone_number', 'email', 'street_address1', 'street_address2', 'town_or_city', 'county', 'country', 'postcode', 'town_or_city', 'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('date', 'order_number','full_name', 'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('date',)

admin.site.register(Order, OrderAdmin)