from django import forms
from django.forms import ModelForm
from .models import Teams, Formation

class ContactForm(forms.Form):
    Project = forms.CharField(label = "Project Name", max_length = 25)
    # # Name = forms.CharField(label = "Name of User", max_length = 25)
    Section = forms.CharField(label = "Class Section", max_length = 4)
    Semester = forms.CharField(label = "Class Semester", max_length = 10)
    Members = forms.CharField(label = "Add Current Users", max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Enter usernames, separated by commas',
                                                                'class': 'form-control',
                                                                }))
    Members_Email = forms.CharField(label = "Invite New Users", max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Enter emails, separated by commas',
                                                                'class': 'form-control',
                                                                }))

    class Meta: 
        model = Teams
    