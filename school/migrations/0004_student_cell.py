# Generated by Django 5.0.4 on 2024-04-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cell',
            field=models.CharField(default='', max_length=12),
        ),
    ]
