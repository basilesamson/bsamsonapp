# Generated by Django 4.0.3 on 2022-03-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_alter_step_status_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Ouvert', 'Open'), ('Fermé', 'Closed')], default='Ouvert', max_length=20, verbose_name='Status'),
        ),
    ]
