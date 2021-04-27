# Generated by Django 3.1.7 on 2021-04-25 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20210425_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='phylum',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.phylum'),
        ),
        migrations.AlterField(
            model_name='class',
            name='update_time',
            field=models.DateTimeField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='class',
            name='update_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.userprofile'),
        ),
    ]