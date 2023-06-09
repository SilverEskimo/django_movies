# Generated by Django 4.1.7 on 2023-03-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_actor_movieactor'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(through='movies_app.MovieActor', to='movies_app.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='movies_app.MovieActor', to='movies_app.actor'),
        ),
    ]
