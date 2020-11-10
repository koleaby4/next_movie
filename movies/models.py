import datetime
import json
import logging
import re

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from movies_collector.imdb_collector import get_movie_details, url_exists

log = logging.getLogger(__name__)


def max_value_current_year(value):
    """Release year validator - value should not exceed next year"""
    next_year = datetime.date.today().year + 1
    return MaxValueValidator(next_year)(value)


class Movie(models.Model):
    imdb_id = models.SlugField(primary_key=True, max_length=20, editable=False)
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(
        blank=True, null=True, validators=[MinValueValidator(1900), max_value_current_year]
    )
    plot = models.CharField(max_length=2000)
    poster_url = models.URLField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    ratings = models.JSONField(default=None, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True)
    full_json_details = models.JSONField(default=None)
    images = models.JSONField(default=None, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.imdb_id)])

    @staticmethod
    def get_release_year(year_str):
        try:
            year = int(year_str)
        except ValueError:
            year_matches = re.match(r"[0-9]{4}", year_str)
            year = int(year_matches[0]) if year_matches else None
        return year

    class Meta:
        permissions = [
            ("paid_for_membership", "Has access to premium content"),
        ]

    @staticmethod
    def persist_movie(imdb_id):
        movie_details = get_movie_details(imdb_id)
        log.warning(f"Fetched movie details: {movie_details}")
        return Movie.from_movie_details(movie_details)

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
            year=Movie.get_release_year(movie_details.get("Year")),
            plot=movie_details.get("Plot"),
            poster_url=poster_url if url_exists(poster_url) else None,
            imdb_rating=imdb_rating,
            ratings=movie_details.get("Ratings"),
            genre=movie_details.get("Genre"),
            full_json_details=movie_details,
            images=movie_details.get("images")
        )

        try:
            movie.save()
        except Exception as e:
            log.error(f"\n\n/!\\ Unable to save movie details /!\\ \n{json.dumps(movie_details)}")
            log.error(f"Error info: type: {type(e)}, details: {e}")
            return

        return movie



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
            log.error(f"\n\n/!\\ Unable to save review  /!\\ \n{json.dumps(review_details)}")
            log.error(f"Error details: {e}")
            return

        log.warning(f"\nReview saved.")
        return review
