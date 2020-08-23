import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def max_value_current_year(value):
    next_year = datetime.date.today().year + 1
    return MaxValueValidator(next_year)(value)


class Movie(models.Model):
    imdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    plot = models.CharField(max_length=2000)
    poster_url = models.URLField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
