from django.contrib import admin
from dashboard.models import Project, Skill, Formation

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Project, ProjectAdmin)

class FormationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Formation, FormationAdmin)