# Generated by Django 3.1.6 on 2021-03-06 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0007_todolist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile',
            new_name='profile_image',
        ),
    ]