# Generated by Django 3.1 on 2020-09-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_watched_movies_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='watched_movies_genres',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]