import datetime
import json
import logging

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from movies_collector.imdb_collector import url_exists
from users.models import CustomUser

log = logging.getLogger(__name__)


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
    watched_by = models.ManyToManyField(CustomUser, related_name="watched_by", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.imdb_id)])

    class Meta:
        permissions = [
            ("paid_for_membership", "Has access to premium content"),
        ]

    @staticmethod
    def from_movie_details(movie_details):
        log.warning(f"\n\nPreparing to save movie: {movie_details}")
        poster_url = movie_details.get("Poster")

        try:
            imdb_rating = float(movie_details.get("imdbRating"))
        except ValueError:
            imdb_rating = None

        movie = Movie(
            imdb_id=movie_details.get("imdbID"),
            title=movie_details.get("Title"),
            year=int(movie_details.get("Year")),
            plot=movie_details.get("Plot"),
            poster_url=poster_url if url_exists(poster_url) else None,
            imdb_rating=imdb_rating,
            full_json_details=json.dumps(movie_details),
        )

        try:
            movie.save()
        except Exception as e:
            log.error(fr"\n\n/!\ Unable to save movie details /!\ \n{json.dumps(movie_details)}")
            log.error(f"Error details: {e}")

        return movie


# class LatestMovie(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="latest_movie")


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    review_title = models.CharField(max_length=300, null=True)
    review_text = models.CharField(max_length=10000, null=True)
    submission_date = models.DateField(blank=True, null=True)
    author_rating = models.IntegerField(blank=True, null=True)
    contains_spoilers = models.BooleanField(default=False)

    def __str__(self):
        return self.review_text

    @staticmethod
    def from_review_details(movie, review_details):

        log.warning(f"\n\nPreparing to save review: {review_details}")

        review = Review(
            movie=movie,
            review_title=review_details.get("reviewTitle"),
            review_text=review_details.get("reviewText"),
            submission_date=datetime.datetime.fromisoformat(review_details.get("submissionDate")),
            author_rating=review_details.get("authorRating"),
            contains_spoilers=review_details.get("spoiler"),
        )

        try:
            review.save()
        except Exception as e:
            log.error(f"\n\n/!\ Unable to save review details /!\ \n{json.dumps(review_details)}")
            log.error(f"Error details: {e}")

        return review
