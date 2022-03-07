from django.contrib import admin
from dashboard.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Task, TaskAdmin)