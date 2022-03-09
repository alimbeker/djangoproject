from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField( max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()


class Prize(models.Model):
    typeofmedal = models.CharField(max_length=50)
    yearofOlympics= models.IntegerField() 


class Men(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.TextField(max_length=20000)
    text = models.TextField(max_length=15000)
    

 
class Women(models.Model):
    fullnamew = models.CharField(max_length=50)
    photow = models.TextField(max_length=20000)
    textw = models.TextField(max_length=15000)   

class MenPrize(models.Model):
    fullnames = models.CharField(max_length=50)
    medaltype = models.CharField(max_length=1000)
    

