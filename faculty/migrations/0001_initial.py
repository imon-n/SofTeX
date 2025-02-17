# Generated by Django 5.0.6 on 2024-07-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('office_address', models.CharField(max_length=300)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='faculty_pictures/')),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('academic_background', models.TextField()),
                ('publications', models.TextField()),
            ],
        ),
    ]
