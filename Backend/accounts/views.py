from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Lib
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout


# Create your views here.


# Landing page view
def index(request):
    animation_objects = Lib.objects.all()
    animation_types = []
    for animation in animation_objects:
        if animation.anima_type not in animation_types:
            animation_types.append(animation.anima_type) 
    paginator = Paginator(animation_types,8)
    page = request.GET.get('page') 
    animation_types = paginator.get_page(page)  
    context = {
        'animation_types': animation_types,
        'animation_objects': animation_objects        
    } 
    return render(request, 'accounts/index.html', context) 


# Registration view
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST': 
        form = RegisterForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.error(request, f'This username {username} already exists!')
            if User.objects.filter(email=email).exists():
                messages.error(request, f'The email {email} already exists!')
                return redirect('accounts:register') 
            form.save()                              
            messages.success(request, f'Welcome {username}, your account is created.')            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/registration.html', {'form':form})


# Profile page view
@login_required
def profilepage(request):
    return render(request, 'accounts/profile.html')

#Login page view
def login_user (request):
    if request.method == 'POST':
        email = request.POST.get['Email']
        password = request.POST.get['Password']
        user = authenticate(request, Email= email, Password = password)
        
        if  user is not None:
            login (request, user)
            # return redirect
            
        else:
            messages.error(request, "Incorrect Email address or Password")
        
    return render(request,'accounts/login.html' )

#logout page view
def logout_user(request):
    
    logout(request)
    return redirect (request, 'index.html')

#ContactUs Page View

def contact(request):
    return render(request, 'accounts/contact.html')

