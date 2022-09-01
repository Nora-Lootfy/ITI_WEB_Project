from django.shortcuts import render, HttpResponse, redirect
from . import forms
from django.contrib.auth import login as auth_login

# Create your views here.
def register(request):
    form = forms.Register()
    
    if request.POST:
        form = forms.Register(request.POST)
        if form.is_valid():
            print("Entered")
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    
    return render(request, 'accounts/register.html', {'form': form})
