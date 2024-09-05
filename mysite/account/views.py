from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    form.add_error(None, 'Аккаунт пользователя неактивен')
                    # form.errors = {'name': ['Аккаунт пользователя не активен']}
                    # return render(request, 'account/login.html', {'form': form})
                    # return HttpResponse('Аккаунт не активен')
            else:
                form.add_error(None, 'Неверная пара логин/пароль')
                # return HttpResponse('Invalid login')
                # form.errors = {'name': ['неверная пара логин/пароль']}
                # return render(request, 'account/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login_user'))

