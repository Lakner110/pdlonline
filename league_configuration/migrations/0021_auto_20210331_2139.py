# Generated by Django 3.1.7 on 2021-03-31 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league_configuration', '0020_discord_settings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='conference',
        ),
        migrations.AddField(
            model_name='season',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='season',
            name='subleague',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league_configuration.subleague'),
        ),
    ]
