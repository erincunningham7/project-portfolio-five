from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=3000)
