from rest_framework import serializers
from .models      import Student

class StudentSerializers(serializers.Serializer):
     city=serializers.CharField(max_length=100)
     name=serializers.CharField(max_length=30)
     email=serializers.EmailField( max_length=254)
     clas=serializers.CharField(max_length=30)