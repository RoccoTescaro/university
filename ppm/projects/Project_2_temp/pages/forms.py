from django import forms
from django.forms import ModelForm
from . import models

class VenueForm(ModelForm):
    class Meta:
        model = models.Venue
        fields = '__all__' # could also write it ('name', 'address', 'zip_code', 'phone', 'web', 'email')

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Luogo'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indirizzo'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Web'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ('name', 'date', 'venue', 'manager', 'description')

        labels = {
            'name': '',
            'date': '',
            'venue': '', 
            'manager': '',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data'}),
            'venue': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrizione'}),
        }