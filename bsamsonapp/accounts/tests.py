from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from .forms import LoginForm, SignupForm
from .views import login_page, signup_page, logout_page

class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", email="user@mp.com", password="Secret123")


class Identification_Form_Test(TestCase):

    # Valid LoginForm Data
    def test_LoginForm_valid(self):
        form = LoginForm(data={'username': 'user', 'password': "Secret123"})
        self.assertTrue(form.is_valid())

    # Invalid LoginForm Data
    def test_LoginForm_invalid(self):
        form = LoginForm(data={'username': '', 'password': "mp"})
        self.assertFalse(form.is_valid())

    # Valid SignupForm Data
    def test_SignupForm_valid(self):
        form = SignupForm(data={'username': 'user', "email":"user@mp.com", 'password1': "Secret123", 'password2': "Secret123"})
        self.assertFalse(form.is_valid())
    
    # Invalid SignupForm Data
    def test_SignupForm_invalid(self):
        form = SignupForm(data={'username': '', 'password': "mp"})
        self.assertFalse(form.is_valid())

class User_Views_Test(Setup_Class):

    # Valid Data
    def test_login_validform_view(self):
        response = self.client.post("/accounts/login/", {'username': 'user', 'password': "Secret123"})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.post("/accounts/logout/")
        self.assertEqual(response.status_code, 200)

    def test_signup_validform_view(self):
        user_count = User.objects.count()
        response = self.client.post("/accounts/signup/", {'username': 'user', 'email': "user@mp.com", 'password1': "Secret123", 'password2': "Secret123"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), user_count+1)