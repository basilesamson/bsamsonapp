# Generated by Django 3.2.3 on 2022-03-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.CharField(blank=True, max_length=100, verbose_name='Projet'),
        ),
    ]