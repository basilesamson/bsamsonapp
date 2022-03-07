from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OP'
        CLOSE = 'CL'
        WAITING = 'WA'

    name = models.fields.CharField('Description', max_length=100)
    project = models.fields.CharField('Projet', null=True, max_length=100)
    progress = models.fields.IntegerField('Progression', default=0)
    status = models.fields.CharField('Status', default=Status.OPEN, choices=Status.choices, max_length=5)

    def __str__(self):
        return f'{self.name}'