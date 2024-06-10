from django.shortcuts import render, reverse
from .forms import ContactUs
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings


# Create your views here.
class SuccessView(TemplateView):
    """
    Display the success template
    """

    template_name = "contact/success.html"


class ContactView(FormView):
    """
    Display the contact form
    """

    form_class = ContactUs
    template_name = "contact/contact.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        user = form.save()
        
        return super(ContactView, self).form_valid(form)

