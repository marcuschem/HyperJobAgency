from django.shortcuts import render
from .models import Vacancy
from django.views.generic.base import TemplateView


class VacancyView(TemplateView):
    template_name = 'vacancy/vacancy.html'

    @classmethod
    def get(cls, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, template_name=cls.template_name, context={'vacancies': vacancies})

