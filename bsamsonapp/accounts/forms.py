from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.validators import UnicodeUsernameValidator as username_validator

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label=("Nom d'utilisateur"),
        max_length=150,
        help_text=('Obligatoire. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ uniquement.'),
        validators=[username_validator],
        error_messages={'unique': ("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        max_length=50, 
        help_text='Obligatoire. Renseignez une adresse email valide.', 
        widget=(forms.TextInput(attrs={'class': 'form-control'}))
    )
    password1 = forms.CharField(
        label=('Mot de passe'), 
        help_text="Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être entièrement numérique.", 
        widget=(forms.PasswordInput(attrs={'class': 'form-control'}))
    )
    password2 = forms.CharField(
        label=('Confirmation du mot de passe'), 
        help_text=('Entrez le même mot de passe, pour vérification.'), 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')