from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from {{ project_name }}.authentication.forms import LoginForm


def login_view(request):
    if request.method == 'GET':
        return _login_view_get(request)
    else:
        return _login_view_post(request)


def _login_view_get(request):
    form = LoginForm()
    context = dict(form=form)
    return render(request, 'authentication/login.html', context)


def _login_view_post(request):
    form = LoginForm(request.POST)
    if not form.is_valid():
        context = dict(form=form)
        return render(request, 'authentication/login.html', context=context, status=403)
    email = form.cleaned_data.get('email')
    senha = form.cleaned_data.get('senha')
    user = authenticate(email=email, password=senha)
    if user is None:
        context = dict(form=form)
        return render(request, 'authentication/login.html', context=context, status=403)
    login(request, user)
    next_url = request.GET.get('next', '/')
    return redirect(next_url)



def logout_view(request):
    logout(request)
    return redirect(reverse('auth:login'))
