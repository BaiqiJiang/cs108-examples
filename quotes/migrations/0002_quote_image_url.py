# Generated by Django 3.1.7 on 2021-03-17 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
