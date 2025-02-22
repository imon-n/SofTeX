# Generated by Django 5.0.6 on 2024-08-01 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_alumni_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('student_id', models.IntegerField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='faculty_pictures/')),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('interested_fields', models.TextField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_student', to='alumni.session')),
            ],
        ),
    ]
