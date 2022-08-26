from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']