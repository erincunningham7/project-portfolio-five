from django.urls import path
from . import views

urlpatterns = [
    path('reviews_list', views.reviews_list, name="reviews_list"),
    path('add_review/<product_id>', views.add_review, name='add_review'),
    path('update_review/<product_id>', views.update_review, name='update_review'),
    path('delete_review/<product_id>', views.delete_review, name='delete_review'),
]