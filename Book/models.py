from django.db import models
from django.contrib.auth.models import User
import datetime

class Menu(models.Model):
   price = models.IntegerField(default=0)
   details = models.CharField(max_length=50)
   title = models.CharField(max_length=50)
   img = models.ImageField(upload_to="static/image", blank=True, null=True)


class Special(models.Model):
    price = models.IntegerField(default=0)
    details = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="static/image", blank=True, null=True)
   
    
   

class Table(models.Model):
  
    table = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="static/image", blank=True, null=True)

   
   

class Book(models.Model):
    number_of_people = models.IntegerField(default=0)
    table = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    occasion = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    date = models.DateField(auto_now=False, blank=False)
    time = models.CharField(max_length=25)
   
    
   
    


