# Generated by Django 5.0.2 on 2024-02-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intervkpmb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stuPass',
        ),
    ]