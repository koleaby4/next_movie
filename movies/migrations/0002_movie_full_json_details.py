# Generated by Django 3.1 on 2020-08-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='full_json_details',
            field=models.JSONField(default=None),
        ),
    ]