from django import forms
from django.contrib.auth.forms import UserCreationForm

from {{ project_name }}.authentication.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput)
