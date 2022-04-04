# Generated by Django 3.1.7 on 2022-04-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_configuration', '0026_discord_settings_server'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='season',
            name='drafttype',
            field=models.CharField(choices=[('Snake', 'Snake'), ('Auction', 'Auction')], default='Snake', max_length=25),
        ),
    ]
