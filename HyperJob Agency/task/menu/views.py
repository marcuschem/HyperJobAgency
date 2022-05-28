from django.shortcuts import render
from django.views.generic.base import TemplateView


class MenuView(TemplateView):
    template_name = 'home.html'

    @classmethod
    def get(cls, request, *args, **kwargs):
        return render(request, cls.template_name, *args, **kwargs)
