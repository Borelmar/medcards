from django import forms
from .models import Client, Visit

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth']

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['client', 'visit_date', 'note']
        widgets = {
            'client': forms.HiddenInput()
        }
