from django.urls import path
from .views import ContactView, SuccessView

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]