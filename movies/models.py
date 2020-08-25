import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


def max_value_current_year(value):
    next_year = datetime.date.today().year + 1
    return MaxValueValidator(next_year)(value)


class Movie(models.Model):
    imdb_id = models.SlugField(primary_key=True, max_length=20, editable=False)
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    plot = models.CharField(max_length=2000)
    poster_url = models.URLField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    full_json_details = models.JSONField(default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.imdb_id)])

    class Meta:
        permissions = [
            ('paid_for_membership', 'Has access to premium content'),
        ]

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=2000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review
