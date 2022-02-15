from django.urls import include, path

from .views import (QuestionnaireListView, questionnaire_view, save_response_questionnaire, questionnaire_manual, process_questionnaire)

app_name = 'questionnaires'

urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='main-view'),
    path('questionnaire-response/', save_response_questionnaire, name='questionnaire-response'),
    path('questionnaire-create/', questionnaire_manual, name='questionnaire-create'),
    path('questionnaire-process/', process_questionnaire, name='questionnaire-process'),
]