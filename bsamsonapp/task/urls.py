from django.urls import path

from task import views

app_name = 'task'
urlpatterns = [
    path('<int:task_id>/', views.task, name='task'),
    path('set_description/', views.setDescription, name='setDescription'),
    path('add_step/', views.addStep, name='addStep'),
    path('set_step_status/', views.setStepStatus, name='setStepStatus'),
    path('delete_step/', views.deleteStep, name='deleteStep'),
]