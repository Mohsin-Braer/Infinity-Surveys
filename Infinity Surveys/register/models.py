from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_lead = models.BooleanField(verbose_name="Project Lead") 
    inst = models.CharField(verbose_name="Institution", max_length=50, blank=True) 

    def __str__(self):
        return self.user.username 
