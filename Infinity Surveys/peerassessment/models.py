from django.db import models
from datetime import datetime
from django import forms 

# Create your models here.

#Model 


class PeerAssessment(models.Model):
    Average = models.CharField(max_length=50)
    Published = models.BooleanField(verbose_name="Published") 
    CurrentUser = models.CharField(max_length=50)  
    Name = models.CharField(max_length=50)
    Team = models.CharField(max_length=50)
    #Id = models.CharField(max_length=50) -> This is used in order to determine who gets to access to a given Peer Assessment
    Description = models.TextField(max_length=300)
    #dateCreated = models.DateField(default=datetime.now, blank=True)
    #dateDue = models.DateField(null=True)
    question1Likert = models.CharField(max_length=50)
    question2Likert = models.CharField(max_length=50)
    question3Likert = models.CharField(max_length=50)
    question4Likert = models.CharField(max_length=50)
    question5Open = models.TextField(max_length=1000, null=True)
    question6Open = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.Name

class PeerAssessmentCreate(models.Model):
    teams = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    end_date = models.DateField(default=None)
    reminder = models.CharField(default=None, max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Peer Assessment Creation"
