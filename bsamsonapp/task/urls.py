from django.urls import path

from task import views

app_name = 'task'
urlpatterns = [
    path('<int:task_id>/', views.task, name='task'),
]