# Generated by Django 3.2.8 on 2021-11-30 03:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_list_type_of_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='list_skil_tag',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=64, null=True), blank=True, null=True, size=10),
        ),
    ]
