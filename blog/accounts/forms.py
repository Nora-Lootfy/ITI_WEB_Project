from cProfile import label
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel

class Register(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']