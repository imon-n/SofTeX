# Generated by Django 5.0.6 on 2024-06-29 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('files', models.FileField(upload_to='routines/')),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='routine', to='courses.semester')),
            ],
        ),
    ]
