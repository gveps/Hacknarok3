# Generated by Django 2.2 on 2019-04-06 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190406_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
