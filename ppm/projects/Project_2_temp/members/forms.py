from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SigninForm(UserCreationForm):
    first_name = forms.CharField(max_length=23, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    last_name = forms.CharField(max_length=23, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cognome'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Conferma Password'})
        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = f"{user.first_name}{user.last_name}"  # Concatenate for display
        if commit:
            user.save()
        return user