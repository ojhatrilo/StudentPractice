# Generated by Django 5.1.1 on 2024-09-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('badge_no', models.CharField(max_length=10, unique=True)),
                ('code_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('secret_mission', models.TextField()),
                ('active', models.BooleanField()),
                ('no_of_assignments', models.IntegerField()),
            ],
        ),
    ]