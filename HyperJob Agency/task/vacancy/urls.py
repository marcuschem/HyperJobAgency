from django.urls import path
from .views import VacancyView


app_name = 'vacancy'
urlpatterns = [
    path('vacancies/', VacancyView.as_view(), name='vacancy'),
]
