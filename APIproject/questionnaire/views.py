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
					Q.name = page['title']['default']
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
						if "hasNone" in element.keys():
							none_theme = Themes.objects.filter(name="none", father__id=theme.id).first()
							if not none_theme:
								none_theme = Themes()
								none_theme.name = "none"
								none_theme.father = theme
								none_theme.save()
							#create option
							opt = Option()
							opt.question = q
							opt.value = "none"
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
		user = User()
		user.save()
		user.email = f"mail{user.id}@mail.com"
		user.save()
		for key in json_data.keys():
			q = Question.objects.filter(questionnaire__id=25, theme__name=key).first()
			if q:
				for option in json_data[key]:
					if option == "other":
						tmp = f"{key}-Comment"
						opt = json_data[tmp]
						theme = Themes.objects.filter(name=key).first()
						other_theme = Themes.objects.filter(name=opt).first()
						if not other_theme:
							other_theme = Themes()
							other_theme.name = opt
							other_theme.father = theme
							other_theme.save()
						#create option
						o = Option()
						o.question = q
						o.value = opt
						o.save()
						#create answer
						answer = Answer()
						answer.question = q
						answer.user = user
						answer.answer = opt
						answer.save()
					else:
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
				t = Themes.objects.filter(id=tema['father_id']).first()
				if not (t.name in temas.keys()):
					temas.update({t.name: []})
				l = temas[t.name]
				l.append(tema['name'])
				temas.update({t.name: l})
			else:
				if not (tema['name'] in temas.keys()):
					l = temas['Poll']
					l.append(tema['name'])
					temas.update({'Poll': l})
		
		users_dict = {}
		for user in User.objects.all():
			users_dict.update({user.id: {}})
			answers_list = list(Answer.objects.filter(user__id=user.id).values())
			for answer in answers_list:
				q = list(Question.objects.filter(id=answer['question_id']).values())[0]
				theme = Themes.objects.filter(id=q['theme_id']).first()
				if not (theme.name in users_dict[user.id].keys()):
					users_dict[user.id].update({theme.name: []})
				l = users_dict[user.id][theme.name]
				l.append(answer['answer'])
				users_dict[user.id].update({theme.name: l})
		
		analize(temas, users_dict)
		return JsonResponse("OK", safe=False)

	return HttpResponse("Error")


@csrf_exempt
def process_most_popular_subthemes(request):
	if request.method == 'GET':
		answers_list = list(Answer.objects.all().values())
		
		subthemes_popularities = {}
		for answer in answers_list:
			if not (answer['answer'] in subthemes_popularities.keys()):
				subthemes_popularities.update({answer['answer']: 1})
			else:
				tmp = subthemes_popularities[answer['answer']]
				tmp+=1
				subthemes_popularities.update({answer['answer']: tmp})
		subthemes_popularities_sorted = dict(sorted(subthemes_popularities.items(), key=lambda item: item[1], reverse = True))
		result = []
		for (key, value) in subthemes_popularities_sorted.items():
			sol = {}
			sol.update({'name': key})
			sol.update({'votes': value})
			result.append(sol)
		return JsonResponse(result, safe=False)
	return HttpResponse("Error")

@csrf_exempt
def process_most_popular_themes(request):
	if request.method == 'GET':
		answers_list = list(Answer.objects.all().values())
		subthemes_popularities = {}
		for answer in answers_list:
			if not (answer['answer'] in subthemes_popularities.keys()):
				subthemes_popularities.update({answer['answer']: 1})
			else:
				tmp = subthemes_popularities[answer['answer']]
				tmp+=1
				subthemes_popularities.update({answer['answer']: tmp})

		themes_popularities = {}
		for (key, value) in subthemes_popularities.items():
			subtheme = Themes.objects.filter(name=key).first()
			theme = Themes.objects.filter(id=subtheme.father_id).first()
			
			if subtheme.name == "none":
				continue
			elif not (theme.name in themes_popularities.keys()):
				themes_popularities.update({theme.name: subthemes_popularities[subtheme.name]})
			else:
				tmp = themes_popularities[theme.name]
				tmp+= subthemes_popularities[subtheme.name]
				themes_popularities.update({theme.name: tmp})
		themes_popularities_sorted = dict(sorted(themes_popularities.items(), key=lambda item: item[1], reverse = True))
		
		result = []
		for (key, value) in themes_popularities_sorted.items():
			sol = {}
			sol.update({'name': key})
			sol.update({'votes': value})
			result.append(sol)
		return JsonResponse(result, safe=False)
	return HttpResponse("Error")