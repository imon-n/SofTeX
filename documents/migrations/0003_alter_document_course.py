# Generated by Django 5.0.6 on 2024-06-29 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('documents', '0002_document_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='courses.course'),
        ),
    ]
