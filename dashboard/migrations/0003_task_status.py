# Generated by Django 4.0.3 on 2022-03-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_task_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('OP', 'Open'), ('CL', 'Close'), ('WA', 'Waiting')], default='OP', max_length=5),
        ),
    ]
