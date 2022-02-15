from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from questionnaire import models, serializers
from questionnaire.models import Questionnaire, Question, Answer, Option, Themes
from user.models import User
from django.views.generic import ListView
from .backend.poll import analize

class QuestionnaireListView(ListView):
	model = Questionnaire
	template_name = 'questionnaires/main.html'

@csrf_exempt
def questionnaire_manual(request):
	if request.method == 'POST':
		json_data = json.loads(request.body)
		Q = Questionnaire()
		Q.name = "NONE"
		questions = []
		themes = []
		
		if json_data['pages']:
			for page in json_data['pages']:
				if Q.name == "NONE":
					Q.name = page['title']
					Q.pub_date = datetime.now()
					Q.save()
				if page['elements']:
					for element in page['elements']:
						#theme
						name = element['name']
						theme = Themes.objects.filter(name=name).first()
						if not theme:
							theme = Themes()
							theme.name = name
							theme.save()
						#question
						q = Question()
						q.questionnaire = Q
						q.text = element['title']
						q.theme = theme
						q.save()	
						#choices
						for ch in element['choices']:
							name1 = ch
							try: 
								name1 = ch['value']
							except:
								name1 = ch
							theme1 = Themes.objects.filter(name=name1).first()
							if not theme1:
								theme1 = Themes()
								theme1.name = name1
								theme1.father = theme
								theme1.save()
							#create option
							opt = Option()
							opt.question = q
							opt.value = ch
							opt.save()
		return JsonResponse("OK", safe=False)
	return HttpResponse("Error")

def questionnaire_view(request, pk):
	q = Questionnaire.objects.get(pk=pk)
	return render(request, 'questionnaires/questionnaire.html', {'obj': q})

@csrf_exempt
def save_response_questionnaire(request):
	if request.method == 'POST':
		json_data = json.loads(request.body)
		for key in json_data.keys():
			q = Question.objects.filter(questionnaire__id=12, theme__name=key).first()
			user = User()
			user.save()
			user.email = f"mail{user.id}@mail.com"
			user.save()
			if q:
				for option in json_data[key]:
					answer = Answer()
					answer.question = q
					answer.user = user
					answer.answer = option
					answer.save()
		return JsonResponse("OK", safe=False)
	return HttpResponse("Error")

@csrf_exempt
def process_questionnaire(request):
	if request.method == 'GET':
		temas_list = list(Themes.objects.all().values())
		temas = {}
		temas.update({'Poll': []})
		for tema in temas_list:
			if tema['father_id']:
				continue
			else:
				if not (tema['name'] in temas.keys()):
					l = temas['Poll']
					l.append(tema['name'])
					temas.update({'Poll': l})
		users_dict = {}
		for user in User.objects.filter(id=1):
			users_dict.update({user.name: {}})
			answers_list = list(Answer.objects.filter(user__id=user.id).values())
			for answer in answers_list:
				q = list(Question.objects.filter(id=answer['question_id']).values())[0]
				theme = Themes.objects.filter(id=q['theme_id']).first()
				if not (theme.name in users_dict[user.name].keys()):
					users_dict[user.name].update({theme.name: []})
				l = users_dict[user.name][theme.name]
				l.append(answer['answer'])
				users_dict[user.name].update({theme.name: l})
		 
		return JsonResponse(analize(temas, users_dict), safe=False)

	return HttpResponse("Error")