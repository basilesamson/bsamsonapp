from pyexpat import model
from attr import field
from django import forms
from task.models import Task, Step

class StepForm(forms.ModelForm):
    class Meta:
        model: Step
        fields= ['name', 'status']