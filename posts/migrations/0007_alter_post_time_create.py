# Generated by Django 3.2.8 on 2021-11-01 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 23, 55, 40, 906024)),
        ),
    ]
