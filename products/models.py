from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, default='images/noimage.png')
    created_on = models.DateTimeField(auto_now_add=True)
    # in_stock = models.BooleanField(default=True)
    # stock_amount = models.IntegerField(default=1)
    # on_sale = models.BooleanField(default=False)
    # discount = models.IntegerField(null=True, blank=True)
    # sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title