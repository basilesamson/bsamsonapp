from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from task.models import Task

class TaskForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        help_text="Obligatoire. Et oui sinon comment on sait ce qu'il faut faire gros malin !", 
        widget=forms.TextInput(attrs={"placeholder": "Nom de la nouvelle tâche"}),
    )
    description = forms.CharField(
        max_length=500,
        help_text="Facultatif, on peut en rajouter une à n'importe quel moment &#128521;", 
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Ajouter une description"}),
    )

    class Meta:
        model = Task
        # fields = ['name', 'description']
        fields = ['name', 'description', 'users']
