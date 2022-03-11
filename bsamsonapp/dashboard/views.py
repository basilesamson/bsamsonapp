from django.http import HttpResponse
from django.shortcuts import render

from task.models import Task

def index(request):
    context = { 
        'tasks' : Task.objects.filter(status='Ouvert')
    }
    
    return render(request, 'dashboard/index.html', context)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')