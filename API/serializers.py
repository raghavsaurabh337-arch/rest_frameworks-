from rest_framework import serializers
from .models import Student,login_form
class StudentSerializers(serializers.Serializer):
     name=serializers.CharField(max_length=100)
     roll=serializers.IntegerField()
     city=serializers.CharField(max_length=200)
     block=serializers.CharField(max_length=50)
     course=serializers.CharField()

     def create(self, validated_data):
          return super().create(validated_data)

class login_formSerializers(serializers.Serializer):
     username=serializers.CharField(max_length=20)
     email=serializers.EmailField()
     password=serializers.CharField(max_length=10)  


     def create(self, validated_data):
          return super().create(validated_data)  