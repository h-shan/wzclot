# Generated by Django 2.1.4 on 2019-05-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0018_tournamentteam_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentgame',
            name='game_finished_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]