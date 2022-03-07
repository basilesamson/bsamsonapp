from os import stat
from django.db import close_old_connections, models

class Task(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OP'
        CLOSE = 'CL'
        WAITING = 'WA'

    name = models.fields.CharField(max_length=100)
    progress = models.fields.IntegerField(default=0)
    status = models.fields.CharField(default=Status.OPEN, choices=Status.choices, max_length=5)

    def __str__(self):
        return f'{self.name}'