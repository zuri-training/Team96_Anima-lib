from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Lib
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from Anibry import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str 
# from . tokens import generate_token


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
            messages.success(request, f'Hi {username}, your account is created!')            
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/registration.html', {'form':form})


#Login page
def login(request):

    # Post user input to the database
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate email and password
        User = authenticate(username = username, password = password)

        if User is not None:
            login(request, User)
            return redirect(request, "accounts/homepage.html")

        else:
            messages.error(request, "Incorrect email or password.")
            return redirect(request, "accounts/login.html")

    return render(request, "accounts/login.html")

#Logout page
def logout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return render(request, "accounts/index.html")



# Profile page view
@login_required(login_url='login/')
def profilepage(request, pk):
    user = User.objects.get(id=pk)

    return render(request, 'accounts/profile.html', {'user':user})

# Library Page
@login_required(login_url='login/')
def library(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/library.html', {'user':user})

@login_required(login_url='login/')
def portfolio(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/portfolio.html', {'user':user})

@login_required(login_url='login/')
def team(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/teampage.html', {'user':user})

@login_required(login_url='login/')
def community(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/community.html', {'user':user})

@login_required(login_url='login/')
def edit(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/editprofile.html', {'user':user})

@login_required(login_url='login/')
def start(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/gettingstarted.html', {'user':user})

@login_required(login_url='login/')
def homepage(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/homepage.html', {'user':user})

@login_required(login_url='login/')
def important(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/importantanimationtips.html', {'user':user})

@login_required(login_url='login/')
def usingclasses(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'accounts/usingclasses.html', {'user':user})

#Login page view
# def login_user (request):
#     if request.method == 'POST':
#         email = request.POST.get['Email']
#         password = request.POST.get['Password']
#         user = authenticate(request, Email= email, Password = password)
        
#         if  user is not None:
#             login (request, user)
#             # return redirect
            
#         else:
#             messages.error(request, "Incorrect Email address or Password")
        
#     return render(request,'accounts/login.html' )

#logout page view
def logout_user(request):
    
    logout(request)
    return redirect (request, 'index.html')

#ContactUs Page View

def contact(request):
    submitted = False
    form = ContactForm()
    if request.method == 'POST':
        if form.is_valid():
            form = ContactForm(request.POST)
            cd = form.cleaned_data
            # assert False
            # form = ContactForm()
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')

    return render(request, 'accounts/contact.html', {'form': form, 'submitted': submitted})

# Documentation page view
def documentation(request):
    return render(request, 'accounts/documentation.html')

def about(request):
    return render(request, 'accounts/teampage.html')
