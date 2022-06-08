from django import forms

from teamcreation.models import Teams
from .models import PeerAssessment, PeerAssessmentCreate
from datetime import datetime
from django.contrib.auth.models import User
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput

LikertChoices = [
    (1, "Highly Disagree"),
    (2, "Slighty Disagree"),
    (3, "Neutral"), 
    (4, "Slightly Agree"), 
    (5 , "Highly Agree")
]
user = User.objects.all()
class PA_form(forms.Form):
    Name = forms.ModelChoiceField(queryset=user)
    Team = forms.CharField(max_length=50)
    Description = forms.CharField(max_length=300)
    #dateCreated = forms.DateField(label= "Date Created",widget=forms.DateInput(format='%m-%d-%Y'))
    #dateDue = forms.DateField(label= "Date Due",widget=forms.DateInput(format='%m-%d-%Y'))
    question1Likert = forms.CharField(label="Did this person do their tasks on time?",
    widget=forms.Select(choices=LikertChoices)) 
    question2Likert = forms.CharField(label="Did this person help others on their team when needed?",
    widget=forms.Select(choices=LikertChoices)) 
    question3Likert = forms.CharField(label="Did this person effectively communicate?",
    widget=forms.Select(choices=LikertChoices)) 
    question4Likert = forms.CharField(label="How likely are you to work with this person again",
    widget=forms.Select(choices=LikertChoices))
    question5Open = forms.CharField(label="What was this person's strengths", max_length=1000)
    question6Open = forms.CharField(label="What was this person's weaknesses", max_length=1000)

    class Meta:
        model = PeerAssessment
        #fields = ['Name', 'Description', 'question1Likert', 'question2Likert', 'question3Likert', 'question4Likert',
                  #'question5Open', 'question6Open']
        
        #for date to be published
        # widgets = {

        # }

freq_opt = [
    (1, "Once a week"),
    (2, "Once evey two weeks"),
    (3, "Once every three weeks"), 
    (4, "Once a month"), 
]
reminder_opt = [
    (1, "24 hours before"),
    (2, "12 hours before"),
    (3, "6 hours before"),
]
teams = Teams.objects.all()

class PA_create(forms.Form):
    teams = forms.ModelChoiceField(queryset=teams)
    name = forms.CharField(label="What would you like to call this survey?")
    end_date = forms.DateField(label="When would you like this survey to be finished?", widget=DatePickerInput)
    reminder = forms.CharField(label="When should we remind people to fill out their surveys?",
    widget=forms.Select(choices=reminder_opt))

    class Meta:
        model = PeerAssessmentCreate



    # Name = forms.CharField(max_length=50)
    # Description = forms.CharField(max_length=300)
    # dateCreated = forms.DateField(label= "Date Created",widget=forms.DateInput(format='%m-%Y-%d'))
    # dateDue = forms.DateField(label= "Date Due",widget=forms.DateInput(format='%m-%Y-%d'))
    # question1Likert = forms.ChoiceField(label = "Question 1 Likert",choices=LikertChoices.choices)
    # question2Likert = forms.ChoiceField( label = "Question 2 Likert",choices=LikertChoices.choices)
    # question3Likert = forms.ChoiceField( label = "Question 3 Likert",choices=LikertChoices.choices )
    # question4Likert = forms.ChoiceField( label = "Question 4 Likert",choices=LikertChoices.choices)
    # question5Likert = forms.ChoiceField( label = "Question 5 Likert",choices=LikertChoices.choices)
    # question6Likert = forms.ChoiceField( label = "Question 6 Likert",choices=LikertChoices.choices)
    # question7OpenEnded = forms.CharField(label = "Question 7 Open Ended",max_length=50)
    # question8OpenEnded = forms.CharField(label = "Question 8 Open Ended",max_length=50) 

    # class Meta:
    #     model = PeerAssessment