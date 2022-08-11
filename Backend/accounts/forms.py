from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class RegisterForm(UserCreationForm):    
    full_name = forms.CharField(max_length=50, required=True)    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email','password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        full_name = self.cleaned_data["full_name"].split()
        first_name, last_name = full_name[0], full_name[-1]
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user    
# placeholder="Harletolarewaju17@gmail.com", name="email" placeholder=""
# (attrs={'placeholder':'(xxx)xxx-xxxx'})
class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder':'Harlet Olarewaju'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder':'Harletolarewaju17@gmail.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Tell us more about what information you are looking to recieve.'}))   
