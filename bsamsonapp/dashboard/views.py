from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from bsamsonapp.utils import handle_uploaded_file

from task.models import Task
from dashboard.models import Project, Skill, Formation
from dashboard.forms import ProjectForm, SkillForm, FormationForm

def index(request):
    context = { 
        'tasks' : Task.objects.filter(status='Ouvert')
    }
    
    return render(request, 'dashboard/index.html', context)

def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = Project.objects.create(name=request.POST.get("name"), user=User.objects.get(pk=request.POST.get("userId")))
            pictureExtension = request.FILES['picture'].content_type.rsplit('/', 1)[-1]
            picturePath = 'media/projects/project_{}.{}'.format(project.id, pictureExtension)
            project.picture = handle_uploaded_file(picturePath, request.FILES['picture'])
            project.description = request.POST.get("description")
            project.save()
            # return redirect('/projects/{}'.format(project.id))
            return redirect('/accounts/profile/{}'.format(request.POST.get("userId")))

    return render(request, 'dashboard/add_project.html', context={'form': form})

def addFormation(request):
    form = FormationForm()
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES)
        if form.is_valid():
            formation = Formation.objects.create(name=request.POST.get("name"), user=User.objects.get(pk=request.POST.get("userId")))

            pictureExtension = request.FILES['picture'].content_type.rsplit('/', 1)[-1]
            picturePath = 'media/formations/formation_{}.{}'.format(formation.id, pictureExtension)
            formation.picture = handle_uploaded_file(picturePath, request.FILES['picture'])

            logoExtension = request.FILES['logo'].content_type.rsplit('/', 1)[-1]
            logoPath = 'media/logos/logo_{}.{}'.format(formation.id, logoExtension)
            formation.logo = handle_uploaded_file(logoPath, request.FILES['logo'])

            formation.description = request.POST.get("description")
            formation.save()
            # return redirect('/projects/{}'.format(project.id))
            return redirect('/accounts/profile/{}'.format(request.POST.get("userId")))

    return render(request, 'dashboard/add_formation.html', context={'form': form})