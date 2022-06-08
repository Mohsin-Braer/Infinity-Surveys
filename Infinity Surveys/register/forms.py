from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from .models import UserProfile
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

# ACCOUNT_OPTIONS = [('General Member', 'General Member'), ('Project Lead', 'Project Lead')]
#registers members as project lead (True) in pre-built django first_name attribute

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    '''first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    confirm_password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))'''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = UserProfile
        fields = ('is_lead', 'inst')
        widgets = {
            'Institution': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: none;',
                'placeholder': 'List Teams',
                'font-family': 'Questrial'
                }),
        }
    
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }