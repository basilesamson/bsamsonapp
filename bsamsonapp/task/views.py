from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from dashboard.views import index
from task.models import Task, Step
from task.forms import TaskForm

def task(request, task_id):
    Task.objects.get(pk=task_id).getProgress()

    context = { 
        'task' : Task.objects.get(pk=task_id),
        'steps' : Step.objects.filter(task=Task.objects.get(pk=task_id))
    }

    return render(request, 'task/index.html', context)

def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(name=request.POST.get("name"), description=request.POST.get("description"))
            # print(request.POST.get("users"))
            # task.user = request.POST.get("user")
            task.save()
            return redirect('/task/{}'.format(task.id))
    return render(request, 'task/add-task.html', context={'form': form})


@csrf_exempt
def deleteTask(request):
    Task.objects.get(pk=request.POST.get("task")).delete()

    return JsonResponse({
        "status": "task succesfully deleted",
        "url": "/",
    })

@csrf_exempt
def setStatus(request):
    task = Task.objects.get(pk=request.POST.get("task"))
    task.status = request.POST.get("status")
    task.save()

    return JsonResponse({
        "status": task.status,
    })

def setDescription(request):
    task = Task.objects.get(pk=request.POST.get("taskId"))
    task.description = request.POST.get("taskDescription")
    task.save()

    return JsonResponse({
        "taskDescription": task.description,
    })

def addStep(request):
    try:
        Step.objects.get(name=request.POST.get("stepName"), task=Task.objects.get(pk=request.POST.get("taskId")))
        return JsonResponse({ "error": "Step already exist" })
    except:
        step = Step.objects.create(name=request.POST.get("stepName"), task=Task.objects.get(pk=request.POST.get("taskId")))
        step.save()

    return JsonResponse({
        "stepId": step.pk,
        "stepName": step.name,
        "stepStatus": step.status,
        "progress": Task.objects.get(name=step.task).getProgress(),
    })

@csrf_exempt
def deleteStep(request):
    Step.objects.get(pk=request.POST.get("step")).delete()

    return JsonResponse({
        "status": "step succesfully deleted",
        "progress": Task.objects.get(name=step.task).getProgress(),
    })

@csrf_exempt
def setStepStatus(request):
    step = Step.objects.get(pk=request.POST.get("step"))
    step.status = request.POST.get("status")
    step.save()

    return JsonResponse({
        "status": step.status,
        "progress": Task.objects.get(name=step.task).getProgress(),
    })