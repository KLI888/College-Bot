# Generated by Django 5.1.5 on 2025-02-25 07:24

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(choices=[('btech', 'B.Tech'), ('mtech', 'M.Tech'), ('bca', 'BCA'), ('mca', 'MCA'), ('other', 'Other')], max_length=10)),
                ('semester', models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', '3rd Semester'), ('4', '4th Semester'), ('5', '5th Semester'), ('6', '6th Semester'), ('7', '7th Semester'), ('8', '8th Semester')], max_length=2)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('feedback', models.TextField()),
                ('improvements', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
