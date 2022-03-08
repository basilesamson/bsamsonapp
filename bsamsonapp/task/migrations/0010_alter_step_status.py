# Generated by Django 4.0.3 on 2022-03-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_alter_step_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='status',
            field=models.CharField(choices=[('Terminé', 'Finished'), ('Bloqué', 'Blocked'), ('En cours', 'In Progress'), (' ', 'Undefined')], default=' ', max_length=20, verbose_name='Status'),
        ),
    ]
