from django.db import models


class User(models.Model):
    name=models.CharField(max_length=100, blank=True)
    email= models.EmailField()
    password=models.CharField(max_length=100,blank=True)