# Generated by Django 3.1.7 on 2021-04-25 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20210425_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='phylum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.phylum'),
        ),
        migrations.AlterField(
            model_name='class',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='update_user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='project.userprofile'),
        ),
    ]