# Generated by Django 3.2.7 on 2021-11-30 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 10, 34, 57, 669645)),
        ),
    ]
