from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get['email']
        pword1 = request.POST.get['username']

        user = authenticate(request, email=email, password=pword1)

        if user is not None:
            login(request, user)
            return render(request, 'accounts/auth.html')

        else:
            messages.error(request, "Bad Credentials!")


    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get['username']
        email = request.POST.get['email']
        pword1 = request.POST.get['pword1']
        pword1 = request.POST.get['pword2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")

        if len(username) > 10:
            messages.error(request, "Username already registered!")

        myuser = User.objects.create_user(username, email, pword1)
        myuser.save()

        message.success(request, "Your account has been successfully created.")
        return redirect('login')

    return render(request, 'accounts/registration.html')

def logout(request):
    logout(request)
    # messages.success(request, "Logged Out successfully")
    return render(request, 'acccouts/index.html')

def forget(request):
    return render(request, 'accounts/forget.html')

def reset(request):
    return render(request, 'accounts/resetpassword.html')
