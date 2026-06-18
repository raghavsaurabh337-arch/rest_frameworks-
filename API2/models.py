# Create your models here.
from django.db import models
# Create your models here.
class Student(models.Model):
     name=models.CharField(max_length=30)
     email=models.EmailField( max_length=254)
     clas=models.CharField(max_length=30)
     city=models.CharField(max_length=100)


