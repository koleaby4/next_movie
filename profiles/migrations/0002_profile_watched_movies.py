# Generated by Django 3.1 on 2020-09-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200914_1923'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='watched_movies',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Movie'),
        ),
    ]
