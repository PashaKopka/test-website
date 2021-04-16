from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    """Review Form"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
        }