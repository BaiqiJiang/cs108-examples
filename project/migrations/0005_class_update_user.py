# Generated by Django 3.1.7 on 2021-04-20 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210421_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='update_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.userprofile'),
        ),
    ]