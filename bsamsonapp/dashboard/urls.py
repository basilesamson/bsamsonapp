from django.urls import path

from dashboard.views import *

app_name = 'dashboard'
urlpatterns = [
    path('add-project/', addProject, name='addProject'),
    path('add-skill/', addSkill, name='addSkill'),
    path('add-formation/', addFormation, name='addFormation'),
    # path('calendar/', views.xxx, name='calendar'),
    # path('projects/', views.xxx, name='projects'),
    # path('profile/', views.xxx, name='profile'),

]