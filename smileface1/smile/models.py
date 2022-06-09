from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Smile (models.Model):
    smileID = models.AutoField
    smileReason = models.CharField(max_length=200)
    smile_Aprroval = models.BooleanField(default=False)
    smileUserName = models.CharField(max_length=100, default="")
    smileImage = models.ImageField(upload_to='smile/images', default="")

    def __str__(self):
        return self.smileUserName


class Category(models.Model):
    Category_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name   = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.category_name

class product(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name   = models.CharField(max_length=50, unique=True)
    Categories_id = models.ForeignKey(Category, on_delete=models.CASCADE)



