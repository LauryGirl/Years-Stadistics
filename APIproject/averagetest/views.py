from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from averagetest.models import AverageTest, SubjectTest
from user.models import User

@csrf_exempt
def process_average_test(request, category):
    if request.method == 'POST':
        user = User()
        user.save()
        user.email = f"mail{user.id}@mail.com"
        user.save()
        json_data = json.loads(request.body)
        values = []
        for key in json_data:
            try:
                value = int(json_data[key].split('#')[0])
            except: 
                for x in json_data[key]:
                    value = int(x.split('#')[0]) 
                    values.append(value)
        suma = sum(values)
        test = AverageTest()
        test.user = user
        test.value = suma
        test.category = category
        test.save()
        return JsonResponse("OK", safe=False)
    return HttpResponse("Error")

@csrf_exempt
def process_years_average(request, category):
    if request.method == 'GET':
        tests = list(AverageTest.objects.filter(category=category).values())
        suma = 0
        for x in tests:
            suma += x['value']
        ave = 1
        if len(tests):
            ave = len(tests)
        return JsonResponse({"Average": suma / ave}, safe=False)
    return HttpResponse("Error")



@csrf_exempt
def process_subject_test(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        values = []
        for key in json_data['subjects'].keys():
            subject = SubjectTest.objects.filter(name=key).first()
            if not subject:
                subject = SubjectTest()
                subject.name = key
            if json_data['subjects'][key] == 'Me gustó':
                subject.likes += 1
            elif json_data['subjects'][key] == 'Meh...':
                subject.dontcare += 1
            else:
                subject.dislikes += 1
            subject.save()
        return JsonResponse("OK", safe=False)
    return HttpResponse("Error")


@csrf_exempt
def get_subject_test_result(request, subjectName):
    if request.method == 'GET':
        subject = SubjectTest.objects.filter(name=subjectName).first()
        sol = {}
        sol.update({subject.name: {}})
        sol[subject.name].update({"likes": subject.likes})
        sol[subject.name].update({"dislikes": subject.dislikes})
        sol[subject.name].update({"dontcare": subject.dontcare})
        return JsonResponse({'Result': sol}, safe=False)
    return HttpResponse("Error")

@csrf_exempt
def get_subject_test_all_result(request):
    if request.method == 'GET':
        subjects = SubjectTest.objects.all()
        sol = {}
        for sub in subjects:
            sol.update({sub.name: {}})
            sol[sub.name].update({"likes": sub.likes})
            sol[sub.name].update({"dislikes": sub.dislikes})
            sol[sub.name].update({"dontcare": sub.dontcare})
        return JsonResponse({"Results": sol}, safe=False)
    return HttpResponse("Error")