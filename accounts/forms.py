from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.validators import UnicodeUsernameValidator as username_validator

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}))

class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text=('Obligatoire. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ uniquement.'),
        validators=[username_validator],
        error_messages={'unique': ("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nom d'utilisateur"})
    )
    email = forms.EmailField(
        max_length=50, 
        help_text='Obligatoire. Renseignez une adresse email valide.', 
        widget=(forms.TextInput(attrs={'class': 'form-control', "placeholder": "Adresse email"}))
    )
    password1 = forms.CharField(
        help_text="Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être entièrement numérique.", 
        widget=(forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Mot de passe"}))
    )
    password2 = forms.CharField(
        help_text=('Entrez le même mot de passe, pour vérification.'), 
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": "Confirmer le mot de passe"})
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

class UserPictureForm(forms.Form):
    file = forms.FileField(label='', widget=forms.FileInput(attrs={"placeholder": "Nom d'utilisateur", "accept": "image/*"}))