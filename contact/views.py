from django.shortcuts import render, reverse
from .forms import ContactUs
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView
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

    def get_success_url(self):
        return reverse("contact")

    def contact(self, form):
        """
        Clean each field, layout the format of the message, use send_email to send the subject, message, from email, and recipient list
        """
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        contact_message = (
            f"New contact message from {full_name} at {email}, {subject}: {message}"
        )
        send_mail(
            subject="New contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)
