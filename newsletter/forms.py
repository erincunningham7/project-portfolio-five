from django import forms
from .models import Newsletter


class Newsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Enter email"})
    )