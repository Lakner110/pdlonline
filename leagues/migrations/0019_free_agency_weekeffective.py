# Generated by Django 3.1.7 on 2021-04-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0018_auto_20210408_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_agency',
            name='weekeffective',
            field=models.CharField(default='1', max_length=30),
            preserve_default=False,
        ),
    ]
