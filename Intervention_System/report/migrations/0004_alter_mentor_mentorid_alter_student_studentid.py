# Generated by Django 4.2.7 on 2024-02-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='mentorId',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentId',
            field=models.CharField(max_length=5),
        ),
    ]
