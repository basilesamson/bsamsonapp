from django import forms

from dashboard.models import Project, Skill

class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nom du projet"}),
    )
    picture = forms.FileField(
        help_text="Une belle image qui mettra bien en valeur ton projet !",
        widget=forms.FileInput(attrs={"accept": "image/*"})
    )
    description = forms.CharField(
        max_length=500,
        help_text="Facultatif, mais c'est quand même mieux pour comprendre le projet.", 
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Ajouter une description"}),
    )

    class Meta:
        model = Project
        fields = ['name', 'picture', 'description']

class SkillForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nom du projet"}),
    )
    color = forms.FileField(
        widget=forms.TextInput(attrs={'type': 'color'}),
    )
    value = forms.IntegerField(
        max_value=100,
        min_value=0,
    )

    class Meta:
        model = Skill
        fields = ['name', 'color', 'value']

class FormationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nom du diplôme ou de la formation"}),
    )
    logo = forms.FileField(
        required=False,
        help_text="Logo : Facultatif, mais ça peut être sympa de leur faire une petite pub à ton école",
        widget=forms.FileInput(attrs={"accept": "image/*"})
    )
    picture = forms.FileField(
        help_text="Une belle image qui mettra bien en valeur ta formation et qui EN PLUS embellira ton profil !",
        widget=forms.FileInput(attrs={"accept": "image/*"})
    )
    description = forms.CharField(
        max_length=500,
        help_text="Facultatif, mais c'est quand même mieux pour comprendre le projet.", 
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Ajouter une description"}),
    )

    class Meta:
        model = Skill
        fields = ['name', 'logo', 'picture', 'description']