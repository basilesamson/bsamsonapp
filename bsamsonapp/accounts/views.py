from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

from . import forms


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                try:
                    return redirect(request.POST.get("next"))
                except:
                    return redirect(settings.LOGIN_REDIRECT_URL)
                    
            else:
                message = 'Identifiants invalides.'
    return render(request, 'accounts/login.html', context={'form': form, 'message': message})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'accounts/signup.html', context={'form': form})

def logout_page(request):
    logout(request)
    return redirect(settings.LOGIN_URL)