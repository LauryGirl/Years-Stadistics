from django.urls import include, path

from .views import (process_average_test, process_years_average, process_years_particularities, process_subject_test, get_subject_test_result, get_subject_test_all_result)

app_name = 'averagetests'

urlpatterns = [
    path('process-average-test/<category>', process_average_test, name='process-average-test'),
    path('process-years-average/<category>', process_years_average, name='process-years-average'),
    path('process-years-particularities/<category>', process_years_particularities, name='process-years-particularities'),
    path('process-subject-test/', process_subject_test, name='process-subject-test'),
    path('process-subject-test-result/<subjectName>', get_subject_test_result, name='process-subject-test-result'),
    path('process-subject-test-all-result/', get_subject_test_all_result, name='process-subject-test-all-result'),
]
