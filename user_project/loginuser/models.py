from django.db import models
from django import forms

class AllUsers(models.Model):
    
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    email= models.CharField(max_length=30, primary_key= True)
    password = models.CharField(max_length=30)

    #USERNAME_FIELD ='email' 