from django.db import models


# Create your models here.
class Student(models.Model):
     name=models.CharField(max_length=100)
     roll=models.IntegerField()
     city=models.CharField(max_length=200)
     block=models.CharField(max_length=50)
     course=models.CharField()


class login_form(models.Model):
     username=models.CharField(max_length=20)
     email=models.EmailField()
     password=models.CharField(max_length=10)     
