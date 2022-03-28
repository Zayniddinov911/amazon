from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CustomerModel


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=60, widget=(
        forms.PasswordInput()
    ))

    class Meta:
        model = CustomerModel
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm(self):
        confirm = self.cleaned_data['confirm']
        password = self.cleaned_data['password']
        if confirm != password:
            raise ValidationError('Password did not match!')
        return confirm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)