from django import forms
from app.model.contact import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=15)
    email = forms.EmailField()
    description = forms.CharField(max_length=50)