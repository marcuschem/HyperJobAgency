from django.urls import path
from .views import ResumeView, MyLoginView, MySignupView, HomeView, NewResumeView, NewVacancyView
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

app_name = 'resume'

urlpatterns = [
    path('resumes/', ResumeView.as_view(), name='resume'),
    path('home', HomeView.as_view()),
    path('resume/new', NewResumeView.as_view()),
    path('vacancy/new', NewVacancyView.as_view()),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', MySignupView.as_view(), name='signup'),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),


]