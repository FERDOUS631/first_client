from django import forms
from .models import contactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactMessage
        fields = ['name', 'email', 'subject', 'message']
     
    
