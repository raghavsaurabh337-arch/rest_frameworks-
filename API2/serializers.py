from rest_framework import serializers
from .models      import Student

class StudentSerializers(serializers.Serializer): 
     name=serializers.CharField(max_length=30)
     email=serializers.EmailField( max_length=254)
     clas=serializers.CharField(max_length=30)
     city=serializers.CharField(max_length=100)

     def create(self, validated_data):
          return Student.objects.create(**validated_data)

     def update(self,instance,validated_data):
          print(instance.name)
          instance.name=validated_data.get('name', instance.name)
          print(instance.name)
          instance.email=validated_data.get('email', instance.email)
          instance.clas=validated_data.get('clas', instance.clas)
          instance.city=validated_data.get('city', instance.city)
          instance.save()
          return instance