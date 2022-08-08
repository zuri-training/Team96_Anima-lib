from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class RegisterForm(UserCreationForm):    
    full_name = forms.CharField(max_length=50, required=True)    
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ['username', 'full_name', 'email','password1', 'password2']
