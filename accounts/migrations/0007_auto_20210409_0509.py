# Generated by Django 3.1.7 on 2021-04-09 05:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210409_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='showdown_alts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), size=None),
        ),
    ]
