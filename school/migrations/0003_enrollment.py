# Generated by Django 5.0.4 on 2024-04-15 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_rename_students_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], default='M', max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
    ]