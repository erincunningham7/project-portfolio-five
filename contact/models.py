from django.db import models
from .forms import ContactUs

# Create your models here.

class ContactModel(models.Model):
    class Meta:
        ordering = [-1]