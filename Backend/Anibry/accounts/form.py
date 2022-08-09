from django import forms

class RegisterForm(forms.Form):
    class Meta:
        model = user
        fields = ['username', 'email', 'password']
    username = forms.CharField(label = 'Username', maxlength = 100)
    email = foerms.EmailField(label = 'Email')