# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from .models import Student
# from .serializers import StudentSerializers
# # from rest_framework.renderers import JSONORenderer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse


# # Create your views here.
# # class Student_api(serializers.ModelSerializer):
# # class Student_api(serializers.ModelSerializer):
# #       if request.method =='GET':
# class Student_api(serializers.ModelSerializer):
#      if request.method =='GET':
#           json_data=request.body
#           stream=io.BytesIO(json_data)
#           parsed_data=JSONParser().parse(stream)
#           id=parsed_data.get('id',None)
#           if id is not None:
#                stu=Student.objects.get(id=id)
#                serializer=StudentSerializers(stu)
#                # json_data=JSONParser().render(serializer.data)
#                json_data = JSONRenderer().render(serializer.data)
#                return HttpResponse(json_data,content_type='application/json')     




from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
import io


def Student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id) 
            serializer = StudentSerializers(stu)

            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')