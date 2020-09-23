import datetime
import json
import logging
import re

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from webpush import send_user_notification

from movies_collector.imdb_collector import get_movie_reviews, url_exists, get_movie_details
from users.models import CustomUser

log = logging.getLogger(__name__)


def max_value_current_year(value):
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
    watched_by = models.ManyToManyField(CustomUser, related_name="watched_by", blank=True)

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
        )

        try:
            movie.save()
        except Exception as e:
            log.error(f"\n\n/!\\ Unable to save movie details /!\\ \n{json.dumps(movie_details)}")
            log.error(f"Error info: type: {type(e)}, details: {e}")
            return

        return movie


@receiver(post_save, sender=Movie)
def notify_users_of_new_movie(sender, instance, created, **kwargs):
    payload = {
        "head": "Another good movie",
        "body": instance.title,
        "url": reverse("movie_detail", args=[instance.pk])
    }

    if instance.poster_url:
        payload["icon"] = instance.poster_url


    log.warning("\n\nMovie's post_save triggered 'notify_users_of_new_movie' function")

    imdb_rating = instance.imdb_rating

    good_movie_imdb_threshold = 7
    if imdb_rating is None or imdb_rating < good_movie_imdb_threshold:
        log.warning(f"IMDB rating too low ({imdb_rating}). Skipping notifications.")
        return

    log.warning(f"Movie {instance} has a rating of {imdb_rating}. Preparing to notify subscribers")

    paid_for_membership_permission = Permission.objects.get(codename="paid_for_membership")

    for user in CustomUser.objects.filter(Q(user_permissions=paid_for_membership_permission)):
        log.warning(f"\n\nSending push notification to prime membership user: {user}")
        send_user_notification(user=user, payload=payload)

# fetch and save reviews when a new movie is created
@receiver(post_save, sender=Movie)
def persist_reviews(sender, instance, created, **kwargs):
    reviews = get_movie_reviews(instance.imdb_id)
    log.warning(f"\n\nFetched reviews: {reviews}")

    for review_details in reviews:
        Review.from_review_details(instance, review_details)


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
            log.error(f"\n\n/!\ Unable to save review  /!\ \n{json.dumps(review_details)}")
            log.error(f"Error details: {e}")
            return

        log.warning(f"\nReview saved.")
        return review
