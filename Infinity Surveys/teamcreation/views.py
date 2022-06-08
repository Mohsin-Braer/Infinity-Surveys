from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Teams
from register.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
 
# Create your views here.
 
def contact_testing(request):
  
   #getAllUsers = UserProfile.objects.all()
 
   if 'cancel' in request.POST:
       return redirect("/view")
   elif 'create' in request.POST:
       form = ContactForm(request.POST)
       if form.is_valid():
           cd = form.cleaned_data
           # name = cd['Project']
           # section = cd['Section']
           # semester = cd['Semester']
           # studentsAdd = cd['Members']
 
           newTeam = Teams(
               Project = cd['Project'],
               Section = cd['Section'],
               Semester = cd['Semester'],
           )
           newTeam.save()
 
           studentsAdd = cd['Members'].replace(" ", "")
           splitNames = studentsAdd.split(",")

           newStudentsAdd = cd['Members_Email'].replace(" ", "")
           splitNewEmails = newStudentsAdd.split(",")

           emailList = []
           inviteEmailList = []
 
 
           try:
               tempLeadUser = UserProfile.objects.get(user=request.user)
               newTeam.Lead.add(tempLeadUser)
           except UserProfile.DoesNotExist:
               tempLeadUser = None
              
 
           for student in splitNames:
               try:
                   tempUser = User.objects.get(username=student)
                   emailList.append(tempUser.email)
               except User.DoesNotExist:
                   tempUser = None
 
               try:
                   tempUserProfile = UserProfile.objects.get(user=tempUser)
                   newTeam.members.add(tempUserProfile)
               except UserProfile.DoesNotExist:
                   tempUserProfile = None
                   
               # newTeam.members.add(tempUserProfile)
               # emailList.append(tempUser.email)
              #tempUser.save()

           print(splitNewEmails[0])

           for inviteStudent in splitNewEmails:
               if(inviteStudent.find('@') != -1):
                   tempName = inviteStudent[0:(inviteStudent.find('@'))]
                   tempEmailUser = User()  #User.objects.create_user(username=tempName, email=inviteStudent, password=(tempName+"12345678")) #(tempName+'12345678')

                   tempEmailUser.username = tempName
                   tempEmailUser.email = inviteStudent
                   tempEmailUser.password = (tempName + "12345678")
                   tempEmailUser.save()

                   tempEmailUserProfile = UserProfile(user = tempEmailUser, is_lead=False)
                   tempEmailUserProfile.save()

                   inviteEmailList.append(inviteStudent)
                   newTeam.members.add(tempEmailUserProfile)


            

           form = ContactForm()

           message = request.user.username + ' has added you to team ' + newTeam.Project + '!'
           send_mail("Infinity Surveys: You have been added to a new team!", message, EMAIL_HOST_USER, emailList, fail_silently=False) 

           message2 = "A temporary account has been created for you. \nPlease go ahead and update your profile with your personal information. \n\nTo login, your temporary username is the sequence of characters before the @ and your password is your username plus digits 1-8. \nFor example: infinity@gmail.com, \nusername: infinity \npassword: infinity12345678" 
           send_mail("Infinity Surveys: You have been added to a new team! Make an account to get started!", message2, EMAIL_HOST_USER,  inviteEmailList, fail_silently=False)
           
           return redirect("/dashboard")
          

   else:
       form = ContactForm()
  
   #return redirect('dashboard')
   return render(request, 'teamcreation/form.html', {'form': form})
 

 
# def contact(request):
#     if 'cancel' in request.POST:
#         return redirect("/view")
#     elif 'create' in request.POST:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             student = Teams(
#                 Project = cd['Project'],
#                 Section = cd['Section'],
#                 Semester = cd['Semester'],
#             )
#             student.save()
#             form  = ContactForm()
#     else:
#         form = ContactForm()
#     return render(request, 'teamcreation/form.html', {'form':form})
 
 
 
 
 
# def createNewCourse_01(request):
#     form = ContactForm()
#     return render(request, 'teamcreation/form.html', {'form':form})
 
# def createNewCourse(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/dashboard")
#     else:
#         form = ContactForm()
#     return render(request, 'teamcreation/form.html', {'form':form})
 