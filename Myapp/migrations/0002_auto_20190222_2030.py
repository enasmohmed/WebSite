# Generated by Django 2.1.7 on 2019-02-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamescore',
            old_name='First_team',
            new_name='first_team',
        ),
        migrations.RenameField(
            model_name='gamescore',
            old_name='First_team_score',
            new_name='first_team_score',
        ),
        migrations.RenameField(
            model_name='gamescore',
            old_name='Second_team',
            new_name='second_team',
        ),
        migrations.RenameField(
            model_name='gamescore',
            old_name='Second_team_score',
            new_name='second_team_score',
        ),
        migrations.AddField(
            model_name='gamescore',
            name='game_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
