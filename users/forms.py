from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


# made for validation 
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Username',
        widget= forms.TextInput(attrs={
                                    "autofocus": True,
                                    'class': "form-control",
                                    'placeholder': "Username"   
                                       }))
        
    password = forms.CharField(
        label = 'Password',
        help_text = 'Your password',
        widget=forms.PasswordInput(attrs={
                                        "autocomplete": "current-password",
                                        'placeholder': "Password",
                                         'class': "form-control",
                                          }))
    
                               

    class Meta: 
        model = User
        fields = ['username', 'password']
