from django.shortcuts import render
from .models import Student ,login_form
from .serializers import StudentSerializers ,login_formSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
# from .serializers import StudentSerializers,
from django.views.decorators.csrf import  csrf_exempt



# Create your views here.
#model object - single student data
def student_detail(request,pk):
     stu =Student.objects.get(id=pk)
     # print(stu)
     serializer=StudentSerializers(stu)
     # print(serializer)
     json_data=JSONRenderer().render(serializer.data)
     # print(json_data)
     return HttpResponse(json_data,content_type='application/json')


# Query set -all Student Data
def student_list(request):
     stu =Student.objects.all()
     # print(stu)
     serializer=StudentSerializers(stu,many=True)
     # print(serializer)
     json_data=JSONRenderer().render(serializer.data)
     # print(json_data)
     return HttpResponse(json_data,content_type='application/json')


def list(request):
     log=login_form.objects.all()
     ser_log=login_formSerializers(log,many=True)
     json_data_login=JSONRenderer().render(ser_log.data)
     return HttpResponse(json_data_login,content_type='application/json')

def list_form(request,pk):
     log=login_form.objects.get(id=pk)
     ser_log=login_formSerializers(log)
     json_data_login=JSONRenderer().render(ser_log.data)
     return HttpResponse(json_data_login,content_type='application/json')

@csrf_exempt
def login_create(request):
     if request.method=='POST':
          json_data=request.body
          stream=io.BytesIO(json_data)
          python_data=JSONParser().parse(stream)
          serializer=login_formSerializers(data=python_data)
          if serializer.is_valid():
           serializer.save()
           msg={'ms':'data Create !'}
           json_msg=JSONRenderer().render(msg)
           return HttpResponse(json_msg,content_type='application/json')
          json_msg-JSONRenderer().render(serializer.errors)
          return HttpResponse(json_msg,content_type='application/json')



