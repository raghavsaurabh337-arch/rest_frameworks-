from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
import io


@csrf_exempt
def Student_api(request):

    # GET Request
    if request.method == 'GET':
        json_data = request.body

        if json_data:
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id', None)

            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializers(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data,content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data,content_type='application/json')

    # POST Request
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        serializer = StudentSerializers(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created Successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    # PUT Request
    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
# complete update- required All Data from front end/client
        #serializer=StudentSerializers=(stu,json_data)
        serializer = StudentSerializers(stu,data=pythondata,partial=True) # partial update= ALL data not reqrired

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated Successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted Successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
       