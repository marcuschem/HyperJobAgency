from .models import Resume
from vacancy.models import Vacancy
from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .forms import AddingForm


class ResumeView(View):
    template_name = 'resume/resume.html'

    @classmethod
    def get(cls, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, template_name=cls.template_name, context={'resumes': resumes})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'resume/login.html'


class HomeView(View):

    @classmethod
    def get(cls, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'resume/home.html')
        else:
            return HttpResponseRedirect('/login')


class NewResumeView(View):

    @classmethod
    def post(cls, request, *args, **kwargs):
        form = AddingForm(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            description = clean_form['description']
            if request.user.is_authenticated and not request.user.is_staff:
                r = Resume.objects.create(description=description, author=request.user)
                r.save()
                return HttpResponseRedirect('/home')
            else:
                return HttpResponseForbidden()
        return HttpResponseForbidden()


class NewVacancyView(View):

    @classmethod
    def post(cls, request, *args, **kwargs):
        form = AddingForm(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            description = clean_form['description']
            if request.user.is_authenticated and request.user.is_staff:
                r = Vacancy.objects.create(description=description, author=request.user)
                r.save()
                return HttpResponseRedirect('/home')
            else:
                return HttpResponseForbidden()
        return HttpResponseForbidden()
