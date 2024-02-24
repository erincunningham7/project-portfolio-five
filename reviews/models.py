from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.
RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


class UserReview(models.Model):
    """
    Define the data fields for a review
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default="", null=True)
    created = models.DateTimeField(auto_now_add=True)
    review = models.TextField()

    def __str__(self):
        return f"{self.product.title}, {self.user}"

    @property
    def get_rating_range(self):
        """Return range of the review rating"""
        return range(self.rating or 1)
