from django.contrib import admin
from task.models import Task, Step

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Task, TaskAdmin)

class StepAdmin(admin.ModelAdmin):
    list_display = ('task', 'name', 'status') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Step, StepAdmin)