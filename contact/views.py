from django.shortcuts import render, reverse
from .forms import ContactUs
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView
from django.conf import settings

# Create your views here.
class ContactView(FormView):
    form_class = ContactUs
    template_name = "contact/contact.html"

    def contact(self, form):
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        contact_message = f"New contact message from {full_name} at {email}, {subject}: {message}"
        send_mail(subject="New contact form submission", message=full_message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.NOTIFY_EMAIL],)
        return super(contact, self).form_valid(form)

        print(contact_message)

    def success(request):
        if request.method == 'POST':
            form = ContactUs(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f"Thank you for contacting us {full_name}! We hope to reply within 24 hours.")
            else:
                messages.error(request, 'Invalid form! Try again')
                template = 'contact/contact_us.html'
                context = {
                'form': form,
                }
            return render(request, template, context)