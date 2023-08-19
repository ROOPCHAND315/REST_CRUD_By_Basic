from django.http import JsonResponse
from .models import StudensModel
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
@csrf_exempt
def studentapi(request):
    if request.method == 'GET':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        student_id = python_data.get('id',None)
    
        if student_id is not None:
            try:
                student = StudensModel.objects.get(id=student_id)
                serializer = StudentSerializer(student)
                return JsonResponse(serializer.data)
            except StudensModel.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)
        
        students = StudensModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)  # safe=False for serializing a list


    if request.method == 'POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        print(python_data)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')    
    
    if request.method == 'PUT':
        json_data=request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        print(python_data)
        student_id=python_data.get('id')
        stu=StudensModel.objects.get(id=student_id)
        print(stu)
        serializer= StudentSerializer(stu , data=python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method =='DELETE':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=StudensModel.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deteled!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    