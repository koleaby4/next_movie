# Generated by Django 3.1.2 on 2020-10-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_watched_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='images',
            field=models.JSONField(default=None, null=True),
        ),
    ]