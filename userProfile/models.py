from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class userProfile(models.Model):
    name = models.CharField(max_length = 100)
    userName = models.CharField(max_length=30,unique = True)
    userId = models.CharField(max_length = 50)
    email = models.EmailField(max_length=50,unique= True)
    dateAndTime = models.DateTimeField(auto_now_add=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(12),MaxValueValidator(120)],null = True,blank = True)
    mode = models.CharField(max_length = 10,default = 'Light',blank = True)

class userNotification(models.Model):
    #foreign key for teams
    #foreign key for workspaces
    notification =  models.CharField(max_length = 300)
    status = models.BooleanField(default = False,blank = True)
    #url = models.CharField()

class userCalender(models.Model):
    date = models.DateField()
    #event
    time = models.TimeField()
    #team
    #workspaces
    #url
