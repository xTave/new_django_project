from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from .form import LoginForm, RegistrationForm
from .settings import PAGE_TO_REDIRECT


def need_authentication(func):
    def f(request, *args, **kwargs):
        if not isinstance(request.user, get_user_model()):
            return redirect('auth/auth.html')
        return func(request, *args, **kwargs)
    return f


def log_out(request):
    logout(request)
    return redirect("/auth")


def auth(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            if user is not None and user.is_active:
                login(request, user)
                return redirect(PAGE_TO_REDIRECT)
    form = LoginForm()
    return render(request, 'auth/auth.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.registrate()
            login(request, user)
            return redirect(PAGE_TO_REDIRECT)
    form = RegistrationForm()
    return render(request, "auth/registration.html", {'form': form})
