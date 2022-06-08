from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PA_form, PA_create
from .models import PeerAssessment, PeerAssessmentCreate
from register.models import UserProfile
import datetime
from django.contrib import messages
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
from teamcreation.models import Teams
# Create your views here.
# def PA_view(request):

#     form = PA_form()
#     return render(request, 'peerassessment/PA.html', {'form':form})

#creates an array of the current is_lead values and gets the most recent value
    


 

def get_PA_results(request):
    form = PA_form()
    if 'cancel' in request.POST:
        return redirect("/view")
    elif 'submit' in request.POST:
        form = PA_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            getTeam = cd['Team']
            getPeerCreate = PeerAssessmentCreate.objects.get(teams=getTeam)

            if(getPeerCreate.end_date >= datetime.date.today()):

                PA = PeerAssessment(
                    Published = False,
                    CurrentUser = request.user.username,
                    Name = cd['Name'],
                    Team = cd['Team'],
        #Id = models.CharField(max_length=50) -> This is used in order to determine who gets to access to a given Peer Assessment
                    Description = cd['Description'],
                    #dateCreated = cd['dateCreated'],
                    #dateDue = cd['dateDue'],
                    question1Likert = cd['question1Likert'],
                    question2Likert = cd['question2Likert'],
                    question3Likert = cd['question3Likert'],
                    question4Likert = cd['question4Likert'],
                    question5Open = cd['question5Open'],
                    question6Open = cd['question6Open'],)
                PA.save()
                form = PA_form()
            else:
                messages.error(request, "Time expired on peer assessment or assessment has been deleted.")
            
            return redirect("/dashboard")

    else: 
        form = PA_form()
    return render(request, 'peerassessment/PA.html', {'form':form})

def get_PA(request):
    
    form = PA_create()
    if 'cancel' in request.POST:
        return redirect("/view")
    elif 'submit' in request.POST:
        form = PA_create(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            PA = PeerAssessmentCreate(
                teams = cd['teams'],
                name = cd['name'],
                end_date = cd['end_date'],
                reminder = cd['reminder'],
            )
            PA.save()

            emailTeam = Teams.objects.get(Project=PA.teams)
            year = PA.end_date.strftime("%Y")
            month = PA.end_date.strftime("%m")
            day = PA.end_date.strftime("%d")
            message = request.user.username + ' has published a new assessment called ' + PA.name + '\nYou have until ' + month + '/' + day + '/' + year + ' to submit!'
            for member in emailTeam.members.all():
                send_mail("Infinity Surveys: New Peer Assessment Published!", message, EMAIL_HOST_USER, [member.user.email], fail_silently=False)

            form = PA_create()
            return redirect("/dashboard")
    else: 
        form = PA_create()
    return render(request, 'peerassessment/PA_create.html', {'form':form})

