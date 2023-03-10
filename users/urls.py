from django.urls import path, include

from users.views import *

app_name = 'users'
urlpatterns = [
    path("login/", login, name='login'),
    path('register/', registration, name='regist')
]

