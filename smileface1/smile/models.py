from distutils.command.upload import upload
from enum import unique
from django.contrib.auth.models import User
from numpy import True_
from phonenumber_field.modelfields import PhoneNumberField

import email
from email.policy import default
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
import uuid
from .code import generate_code

# Create your models here.


class Smile (models.Model):
    smileID = models.AutoField
    smileReason = models.CharField(max_length=200)
    smile_Aprroval = models.BooleanField(default=False)
    smileUserName = models.CharField(max_length=100, default="")
    smileImage = models.ImageField(upload_to='smile/images', default="")
    referal_code = models.CharField(max_length=12, blank=True)
    
    def __str__(self):
        return self.smileUserName

    def save(self, *args, **kwargs):
        if self.referal_code == "":
            referal_code = generate_code()
            self.referal_code = referal_code
        return super().save(*args, **kwargs)



class profile(models.Model):
    profile_id = models.AutoField(auto_created=True, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    FName = models.CharField(max_length=15, blank=True,unique=True)
    LName = models.CharField(max_length=15, blank=True)
    Phone = PhoneNumberField(blank = True)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    profile_image = models.ImageField(upload_to='smile/images', default="")
    referal_code = models.CharField(max_length=12, blank=True)
    points = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.FName


