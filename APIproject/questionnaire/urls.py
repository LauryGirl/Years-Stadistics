from django.urls import include, path

from .views import (QuestionnaireListView, questionnaire_view, save_response_questionnaire, questionnaire_manual, process_questionnaire, process_most_popular_themes, process_most_popular_subthemes)

app_name = 'questionnaires'

urlpatterns = [
    path('', QuestionnaireListView.as_view(), name='main-view'),
    path('questionnaire-response/', save_response_questionnaire, name='questionnaire-response'),
    path('questionnaire-create/', questionnaire_manual, name='questionnaire-create'),
    path('questionnaire-process/', process_questionnaire, name='questionnaire-process'),
    path('process-most-popular-themes/', process_most_popular_themes, name='process-most-popular-themes'),
    path('process-most-popular-subthemes/', process_most_popular_subthemes, name='process-most-popular-subthemes'),
]