from pyexpat import model
from turtle import mode
from django.db import models

# Create your models here.

class Car(models.Model):
    tittle = models.TextField(max_length=250)
    year =  models.TextField(max_length=4, null=True)

    