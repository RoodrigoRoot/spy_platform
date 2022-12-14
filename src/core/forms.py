from django import forms
from src.hitmens.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    
    """
    This form is blank, maybe in a future we need more logic or fields to login
    """
    
    ...


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email", help_text="Enter your email",
    widget=forms.TextInput(attrs={
        "placeholder":"rod@spy.com"
    })
    )
    password = forms.CharField(label="Password", help_text="Enter a password", widget=forms.PasswordInput(attrs={
        "placeholder":"Enter a password"
    }))

    name = forms.CharField( max_length=200, required=False)
    description = forms.CharField(widget=forms.Textarea)
    def clean_email(self):
        email = str.lower(self.cleaned_data['email'])
        if User.objects.filter(email=email).exists():
            raise ValidationError("This Email are not available. Check your email.")
        return email