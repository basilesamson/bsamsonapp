from django.shortcuts import render

from task.models import Task, Step

def task(request, task_id):
    context = { 
        'task' : Task.objects.get(pk=task_id),
        'steps' : Step.objects.filter(task=Task.objects.get(pk=task_id))
    }
    
    return render(request, 'task/index.html', context)