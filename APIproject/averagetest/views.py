from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from averagetest.models import AverageTest, SubjectTest
from user.models import User

# Humor and Creativity Tests
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
        sol = {}
        sol.update({"Average": suma / ave})
        result = []
        result.append(sol)
        return JsonResponse(result, safe=False)
    return HttpResponse("Error")

@csrf_exempt
def process_years_particularities(request, category):
    if request.method == 'GET':
        tests = list(AverageTest.objects.filter(category=category).values())
        result = []
        sol = {}
        s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
        if category == 'humor':
            for x in tests:
                if x['value'] <= 24:
                    s1 += 1
                elif x['value'] >= 25 and x['value'] <= 49:
                    s2 += 1
                elif x['value'] >= 50 and x['value'] <= 84:
                    s3 += 1
                elif x['value'] >= 85 and x['value'] <= 114:
                    s4 += 1
                else:
                    s5 += 1
            sol.update({"serio": s1})
            sol.update({"pobre": s2})
            sol.update({"justo": s3})
            sol.update({"promedio": s4})
            sol.update({"excelente": s5})
        else:
            for x in tests:
                if x['value'] <= 9:
                    s1 += 1
                elif x['value'] >= 10 and x['value'] <= 19:
                    s2 += 1
                elif x['value'] >= 20 and x['value'] <= 39:
                    s3 += 1
                elif x['value'] >= 40 and x['value'] <= 64:
                    s4 += 1
                elif x['value'] >= 65 and x['value'] <= 94:
                    s5 += 1
                else:
                    s6 += 1
            sol.update({"no creativo": s1})
            sol.update({"debajo promedio": s2})
            sol.update({"promedio": s3})
            sol.update({"encima promedio": s4})
            sol.update({"muy creativo": s5})
            sol.update({"excepcional": s6})
        result.append(sol)
        return JsonResponse(result, safe=False)
    return HttpResponse("Error")


# Subject Test
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
        sol.update({"name": subject.name})
        sol.update({"likes": subject.likes})
        sol.update({"dislikes": subject.dislikes})
        sol.update({"dontcare": subject.dontcare})
        result = []
        result.append(sol)
        return JsonResponse(result, safe=False)
    return HttpResponse("Error")

@csrf_exempt
def get_subject_test_all_result(request):
    if request.method == 'GET':
        subjects = SubjectTest.objects.all()
        result = []
        for sub in subjects:
            sol = {}
            sol.update({"name": sub.name})
            sol.update({"likes": sub.likes})
            sol.update({"dislikes": sub.dislikes})
            sol.update({"dontcare": sub.dontcare})
            result.append(sol)
        return JsonResponse(result, safe=False)
    return HttpResponse("Error")