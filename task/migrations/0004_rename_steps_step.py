# Generated by Django 3.2.3 on 2022-03-07 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20220307_2041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Steps',
            new_name='Step',
        ),
    ]
