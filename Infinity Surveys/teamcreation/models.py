from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
from register.forms import UserProfile

from django.contrib.auth import get_user_model as User1
from datetime import datetime


# Create your models here.
class Teams(models.Model):
    Project = models.CharField(max_length = 25)
    #Name = models.CharField(max_length = 25)
    Section = models.CharField(max_length = 4)
    Semester = models.CharField(max_length = 10)
    Lead = models.ManyToManyField(UserProfile, related_name= 'team_lead_of')
    #Members = models.CharField(max_length=200)
    members = models.ManyToManyField(UserProfile, blank=True)
    
    def __str__(self):
        return self.Project

    class Meta:
            #Addresses unneccessary S at the end of plural 
            verbose_name_plural = "Teams" 

# class Students(models.Model):
#         Name = models.CharField(max_length = 25)
#         email = models.EmailField(max_length = 25)

#         def __str__(self):
#          return self.Name 

#          class Meta:
#             #Addresses unneccessary S at the end of plural 
#             verbose_name_plural = "Students"

# class Groups(models.Model):
#     Name = models.TextField()
#     Section = models.TextField()
#     Semester = models.TextField()
#     TotalStudents = models.IntegerField()
#     student = models.ManyToManyField(Students)

#     #students = models.ManyToManyField(User)

#     def __str__(self):
#         return self.Name

#     class Meta:
#             #Addresses unneccessary S at the end of plural 
#             verbose_name_plural = "Groups"
        
class Formation(models.Model):
    formation_name = models.CharField(max_length = 35, default="Formation Object")
    student = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    group = models.ForeignKey(Teams, on_delete = models.CASCADE)
    date_enrolled = models.DateField(default=datetime.now)

    def __str__(self):
        return self.formation_name

    class Meta: 
        unique_together = [['student', 'group']]



