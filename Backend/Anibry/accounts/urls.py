from django.contrib import admin
from django.urls import path, include
from .views import (index, login, register, logout,)


app_name = "accounts"

urlpatterns = [
    path('', index, name= 'index'),
    path('login/', login_view, name= 'login'),
    path('register', register_view, name= 'register'),
    path('logout/', register_view, name= 'logout'),
    # path('forgetpassword/', register_view, name= 'logout'),
    # path('resetpassword/', register_view, name= 'logout'),
]