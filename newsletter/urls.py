from django.urls import path
from .views import NewsletterView, SubscribedView

urlpatterns = [
    path("", NewsletterView.as_view(), name="newsletter"),
    path("subscribed/", SubscribedView.as_view(), name="subscribed"),
]
