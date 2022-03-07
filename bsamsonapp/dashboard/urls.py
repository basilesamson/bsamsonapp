from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views

urlpatterns = [
    path('/', views.index, name='dashboard'),
    # path('calendar/', views.xxx, name='calendar'),
    # path('projects/', views.xxx, name='projects'),
    # path('profile/', views.xxx, name='profile'),

]