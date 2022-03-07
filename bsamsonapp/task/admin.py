from django.contrib import admin
from task.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Task, TaskAdmin)