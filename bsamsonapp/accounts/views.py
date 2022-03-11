from distutils import extension
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render

from accounts.models import User, UserProfile
from accounts.forms import LoginForm, SignupForm, UserPictureForm
from bsamsonapp.utils import *

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                try:
                    return redirect(request.POST.get("next"))
                except:
                    return redirect(settings.LOGIN_REDIRECT_URL)
                    
            else:
                message = 'Identifiants invalides.'
    return render(request, 'accounts/login.html', context={'form': form, 'message': message})


def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'accounts/signup.html', context={'form': form})

def logout_page(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

def user_profile(request, user_id):
    try:
        userProfile = UserProfile.objects.get(pk=user_id)
    except:
        userProfile = UserProfile.objects.create(pk=user_id, user=User.objects.get(pk=user_id))
        userProfile.save()

    context = { 
        'userProfile' : userProfile,
        'form' : UserPictureForm()
    }

    if request.method == 'POST':
        form = UserPictureForm(request.POST, request.FILES)
        if form.is_valid():
            fileExtension = request.FILES['file'].content_type.rsplit('/', 1)[-1]
            filePath = 'media/profile_picture/profile_picture_{}.{}'.format(user_id, fileExtension)
            userProfile.picture = handle_uploaded_file(filePath, request.FILES['file'])
            userProfile.save()
            context['userProfile'] = userProfile
            
            return render(request, 'accounts/user_profile.html', context)

    return render(request, 'accounts/user_profile.html', context)

def set_user_description(request):
    userProfile = UserProfile.objects.get(pk=request.POST.get("userId"))
    userProfile.description = request.POST.get("userDescription")
    userProfile.save()

    return JsonResponse({
        "userProfileDescription": userProfile.description,
    })

def set_user_picture(request):
    print(request.POST)
    print(request.POST.get["userPicture"])
    # userProfile = UserProfile.objects.get(pk=request.POST.get("userId"))
    # userProfile.picture = request.POST.get("userPicture")
    # userProfile.save()

    # return JsonResponse({
    #     "userProfilePicture": userProfile.picture,
    # })