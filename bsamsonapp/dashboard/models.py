from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.fields.CharField('Nom', max_length=100)
    picture = models.CharField(default='media/projects/default.png', max_length=100)
    description = models.fields.CharField('Description', blank=True, null=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Skill(models.Model):
    name = models.fields.CharField('Compétence', max_length=100)
    color = models.fields.CharField('Couleur', default='#06D7A0', max_length=7)
    value = models.fields.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-value']


class Formation(models.Model):
    name = models.fields.CharField('Nom', max_length=100)
    logo = models.fields.CharField(default='', max_length=100)
    picture = models.CharField(default='media/formations/default.png', max_length=100)
    description = models.fields.CharField('Description', blank=True, null=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']