# Generated by Django 2.1.4 on 2019-05-16 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0012_auto_20190424_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentteam',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wlct.GroupStageTournamentGroup'),
        ),
        migrations.AddField(
            model_name='tournamentteam',
            name='rr_tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rr_tournament', to='wlct.RoundRobinTournament'),
        ),
        migrations.AlterField(
            model_name='roundrobintournament',
            name='first_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rr_first_place', to='wlct.TournamentTeam'),
        ),
        migrations.AlterField(
            model_name='roundrobintournament',
            name='second_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rr_second_place', to='wlct.TournamentTeam'),
        ),
    ]