# Generated by Django 2.1.4 on 2020-01-28 22:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0061_auto_20200123_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentgame',
            name='game_start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 22, 34, 41, 695445, tzinfo=utc)),
        ),
    ]