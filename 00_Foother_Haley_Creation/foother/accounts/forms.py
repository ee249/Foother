from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'user_nick', 'user_phone', 'user_birth', 'user_profile_image',)