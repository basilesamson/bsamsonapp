# Generated by Django 4.0.3 on 2022-03-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_alter_step_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.CharField(max_length=100, null=True, verbose_name='Projet'),
        ),
    ]
