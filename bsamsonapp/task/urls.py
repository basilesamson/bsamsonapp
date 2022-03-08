from django.urls import path

from task import views

app_name = 'task'
urlpatterns = [
    path('<int:task_id>/', views.task, name='task'),
    path('add_step/', views.addStep, name='addStep'),
    path('set_step_status/', views.setStepStatus, name='setStepStatus'),
]