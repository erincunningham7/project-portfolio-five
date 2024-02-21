from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<str:pk>', views.add_review, name='add_review'),
    path('update_review/<str:pk>', views.update_review, name='update_review'),
    path('delete_review/<str:pk>', views.delete_review, name='delete_review'),
]