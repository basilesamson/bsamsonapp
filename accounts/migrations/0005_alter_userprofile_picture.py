# Generated by Django 4.0.3 on 2022-03-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.CharField(default='media/profile_picture/default.png', max_length=100),
        ),
    ]
