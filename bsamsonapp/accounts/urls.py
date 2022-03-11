from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),

    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset_email.html', success_url='/accounts/password_reset_done'), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url='/accounts/reset/done'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('profile/<int:user_id>/', views.user_profile, name='userProfile'),
    path('profile/set_user_description/', views.set_user_description, name='setUserDescription'),
    path('profile/set_user_picture/', views.set_user_picture, name='setUserPicture'),
]