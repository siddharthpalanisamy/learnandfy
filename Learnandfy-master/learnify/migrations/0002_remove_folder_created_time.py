# Generated by Django 5.0.1 on 2024-02-15 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='created_time',
        ),
    ]