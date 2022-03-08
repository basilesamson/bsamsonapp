from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from task.models import Task, Step

def task(request, task_id):
    context = { 
        'task' : Task.objects.get(pk=task_id),
        'steps' : Step.objects.filter(task=Task.objects.get(pk=task_id))
    }

    return render(request, 'task/index.html', context)

def addStep(request):
    step = Step.objects.create(name=request.POST.get("stepName"), task=Task.objects.get(pk=request.POST.get("taskId")))
    step.save()

    task = Task.objects.get(name=step.task)
    task.progress = int(Step.objects.filter(task=task).filter(status="Terminé").count() / Step.objects.filter(task=task).count() * 100)
    task.save()

    return JsonResponse({
        "stepId": step.pk,
        "stepName": step.name,
        "stepStatus": step.status,
        "progress": task.progress,
    })


@csrf_exempt
def setStepStatus(request):
    step = Step.objects.get(pk=request.POST.get("step"))
    step.status = request.POST.get("status")
    step.save()

    task = Task.objects.get(name=step.task)
    task.progress = int(Step.objects.filter(task=task).filter(status="Terminé").count() / Step.objects.filter(task=task).count() * 100)
    task.save()

    return JsonResponse({
        "status": step.status,
        "progress": task.progress,
    })