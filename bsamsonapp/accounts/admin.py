from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(UserProfile, UserProfileAdmin)