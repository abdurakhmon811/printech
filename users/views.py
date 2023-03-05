from .assistants import *
from django.contrib import messages
from django.contrib.auth import login
from django_ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect
from .backends import CustomBackend
from .forms import BusinessUserCreationForm, \
    CaptchaForm, \
    IndividualUserCreationForm, \
    PhoneNumberLoginForm, \
    UsernameLoginForm
from .models import CustomUser

import time
import json


@ratelimit(key='ip', rate='10/m')
def choose_registration_type(request):
    """
    Renders the page for choosing whether to register as an individual or a legal entity.
    """

    return render(request, 'registration/choose_registration_type.html')


@ratelimit(key='ip', rate='10/m')
def register_individual(request):
    """
    Renders the page for creating a new user.
    """

    users = CustomUser.objects.all()
    usernames = [str(user.username) for user in users]
    phone_numbers = [str(user.phone_number) for user in users]

    captcha_form = CaptchaForm()

    if request.method == 'POST':
        form = IndividualUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = True
            new_user.last_login = time.strftime('%Y-%m-%d', time.localtime())
            new_user.date_joined = time.strftime('%Y-%m-%d', time.localtime())
            new_user.save()
            login(request, new_user, backend='users.backends.CustomBackend')
            return redirect('index')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'captcha_form': captcha_form,
        'phone_numbers': phone_numbers,
        'usernames': usernames,
    }
    return render(request, 'registration/register_individual.html', context)


@ratelimit(key='ip', rate='10/m')
def register_legal_entity(request):
    """
    Renders the page for creating a new user.
    """

    users = CustomUser.objects.all()
    usernames = [str(user.username) for user in users]
    phone_numbers = [str(user.phone_number) for user in users]

    captcha_form = CaptchaForm()

    if request.method == 'POST':
        form = BusinessUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = True
            new_user.is_legal_entity = True
            new_user.last_login = time.strftime('%Y-%m-%d', time.localtime())
            new_user.date_joined = time.strftime('%Y-%m-%d', time.localtime())
            new_user.save()
            login(request, new_user, backend='users.backends.CustomBackend')
            return redirect('index')

    context = {
        'captcha_form': captcha_form,
        'phone_numbers': phone_numbers,
        'usernames': usernames,
    }
    return render(request, 'registration/register_legal_entity.html', context)


@ratelimit(key='ip', rate='10/m')
def login_with_username(request):
    """
    Renders the page for authenticating a registered user with a username.
    """

    validator = AuthenticationValidator()

    results = {
        'username_valid': None,
        'password_valid': None,
        'user_not_found': None,
    }

    posted_username = None
    posted_password = None

    if request.method == 'POST':
        form = UsernameLoginForm(data=request.POST)
        posted_username = request.POST.get('username')
        posted_password = request.POST.get('password')
        results['username_valid'] = validator.validate_username(str(posted_username))
        results['password_valid'] = validator.validate_password(str(posted_password))
        print(results)
        if form.is_valid() and results['username_valid'] and results['password_valid']:
            backend = CustomBackend()
            user = backend.authenticate(
                request=request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                results['user_not_found'] = False
                login(request, user, backend='users.backends.CustomBackend')
                return redirect('index')
            else:
                results['user_not_found'] = True
                messages.error(request, "Foydalanuvchi nomi (login) yoki parol noto'g'ri kiritildi!")
        else:
            messages.error(request, "Foydalanuvchi nomi (login) yoki parol noto'g'ri kiritildi!")
    
    json_results = json.dumps(results)

    context = {
        'posted_username': '' if posted_username is None else posted_username,
        'posted_password': '' if posted_password is None else posted_password,
        'json_results': json_results,
    }
    return render(request, "registration/login_with_username.html", context)


@ratelimit(key='ip', rate='10/m')
def login_with_phone_number(request):
    """
    Renders the page for authenticating a registered user with a phone number.
    """

    validator = AuthenticationValidator()

    results = {
        'phone_number_valid': None,
        'password_valid': None,
        'user_not_found': None,
    }

    posted_phone_number = None
    posted_password = None
    
    if request.method == 'POST':
        form = PhoneNumberLoginForm(data=request.POST)
        posted_phone_number = request.POST.get('phone_number')
        posted_password = request.POST.get('password')
        results['phone_number_valid'] = validator.validate_phone_number(str(posted_phone_number))
        results['password_valid'] = validator.validate_password(str(posted_password))
        if form.is_valid() and results['phone_number_valid'] and results['password_valid']:
            backend = CustomBackend()
            user = backend.authenticate(
                request=request,
                phone_number=form.cleaned_data['phone_number'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                results['user_not_found'] = False
                login(request, user, backend='users.backends.CustomBackend')
                return redirect('index')
            else:
                results['user_not_found'] = True
                messages.error(request, "Telefon raqam yoki parol noto'g'ri kiritildi!")
        else:
            messages.error(request, "Telefon raqam yoki parol noto'g'ri kiritildi!")
    
    json_results = json.dumps(results)

    context = {
        'posted_phone_number': '+998' if posted_phone_number is None else posted_phone_number,
        'posted_password': '' if posted_password is None else posted_password,
        'json_results': json_results,
    }
    return render(request, "registration/login_with_phone_number.html", context)
