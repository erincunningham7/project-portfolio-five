from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.

class UserReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return f'{self.product.title}, {self.user}'
