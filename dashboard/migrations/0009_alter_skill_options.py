# Generated by Django 4.0.3 on 2022-03-21 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20220312_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-value']},
        ),
    ]
