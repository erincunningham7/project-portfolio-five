from django.shortcuts import render, reverse
from .forms import Newsletter
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings


# Create your views here.
class SubscribedView(TemplateView):
    """
    Display the susbcribed template
    """

    template_name = "newsletter/subscribed.html"


class NewsletterView(FormView):
    """
    Display the newsletter form
    """

    form_class = Newsletter
    template_name = "newsletter/newsletter.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('subscribed')

    def form_valid(self, form):
        user = form.save()

        return super(NewsletterView, self).form_valid(form)
