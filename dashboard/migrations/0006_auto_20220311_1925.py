# Generated by Django 3.2.3 on 2022-03-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.DeleteModel(
            name='Formation',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]