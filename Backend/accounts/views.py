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
from . tokens import generate_token


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
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/registration.html', {'form':form})

# Registration view
# def register(request):
#     # Post user input to the database
#     if request.method == "POST":
#         fullname = request.POST['fullname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         # Check email
#         if User.objects.filter(email = email):
#             messages.error(request, "Email already register")
#             return redirect('register')
        
#         myuser = User.objects.create_user(fullname, username, email, password)
#         myuser.is_active = False
#         myuser.save()

#         messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email")

#         # Welcome Email
#         subject = "Welcome to Anibry"
#         message = "Hello " + username + "!! \n" + "Welcome  to Anibry!! \n Thanks for visiting our Website."
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [myuser.email]
#         send_mail(subject, message, from_email, to_list, fail_silently=True)

#         # Email Address Confirmation Email
#         current_site = get_current_site(request)
#         email_subject = "Confirm your email @ accounts - Django Login!!"
#         message2 = render_to_string("email_confirmation.html"),{
#             'name': username,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#             'token': generate_token.make_token(myuser)
#         }
#         email = EmailMessage(
#             email_subject,
#             message2,
#             settings.EMAIL_HOST_USER,
#             [myuser.email],
#         )
#         email.fail_silently = True
#         email.send()

#         return redirect('login')

#     return render(request, "accounts/registration.html")

#Login page
def login(request):

    # Post user input to the database
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate email and password
        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect(request, "accounts/homepage.html")

        else:
            messages.error(request, "Incorrect email or password.")
            return redirect(request, "accounts/login.html")

    return render(request, "accounts/login.html")

#Logout page
def logout(request):
    logout(request, user)
    messages.success(request, "Logged out Successfully")
    return render(request, "accounts/index.html")

#Email activation View
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base_decode(uidb64))
        mysuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, "activation_failed.html")

#Reset password page
def reset(request):
    return render(request, "accounts/resetpassword.html")

#Forgot password page
def forgot(request):
    return render(request, "accounts/forgotpassword.html")

#Login page
# def login(request):
#     return render(request, "accounts/login.html")


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
