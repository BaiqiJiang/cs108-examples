# Generated by Django 3.1.7 on 2021-04-20 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='reg_time',
        ),
    ]
