from django import forms
from .models import User


class loginForm(forms.Form):
    email = forms.EmailField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
