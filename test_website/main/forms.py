from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
        }


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': None,
        }