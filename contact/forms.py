from django import forms
from .models import Contact

class ContactUs(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Name"})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Enter email"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )
