from django.shortcuts import render

from users.models import *

def login(request):
    return render(request, 'users/login.html')

def registration(request):
    context = {
    }
    return render(request, 'users/registration.html')
