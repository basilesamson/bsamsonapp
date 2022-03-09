from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        OPEN = 'Ouvert'
        CLOSED = 'Fermé'
        IN_PROGRESS = 'En cours'

    name = models.fields.CharField('Nom', max_length=100)
    description = models.fields.CharField('Description', blank=True, null=True, max_length=500)
    project = models.fields.CharField('Projet', blank=True, null=True, max_length=100)
    progress = models.fields.IntegerField('Progression', default=0)
    status = models.fields.CharField('Status', default=Status.OPEN, choices=Status.choices, max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['project', 'name', 'status']


class Step(models.Model):
    class Status(models.TextChoices):
        FINISHED = 'Terminé'
        BLOCKED = 'Bloqué'
        IN_PROGRESS = 'En cours'
        UNDEFINED = 'Créé'
    name = models.fields.CharField("Nom de l'étape", max_length=100)
    status = models.fields.CharField('Status', default=Status.UNDEFINED, choices=Status.choices, max_length=20)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['task', 'id']

