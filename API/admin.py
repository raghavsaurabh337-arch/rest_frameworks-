from django.contrib import admin
from .models import Student , login_form

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
     list_display=['id','name','roll','city','block','course']

@admin.register(login_form)
class login_formAdmin(admin.ModelAdmin):  
     list=('id','username','email','password')
