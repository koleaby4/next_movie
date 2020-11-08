import logging

from django.contrib.auth.models import Permission
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from movies_collector.imdb_collector import get_movie_reviews
from users.models import CustomUser
from webpush import send_user_notification

from movies.models import Movie, Review

log = logging.getLogger(__name__)


# fetch and save reviews when a new movie is created
@receiver(post_save, sender=Movie)
def persist_reviews(sender, instance, created, **kwargs):

    if not created:
        return

    reviews = get_movie_reviews(instance.imdb_id)
    log.warning(f"\n\nFetched reviews: {reviews}")

    for review_details in reviews:
        Review.from_review_details(instance, review_details)

@receiver(post_save, sender=Movie)
def notify_users_of_new_movie(sender, instance, created, **kwargs):

    if not created:
        return

    payload = {
        "head": "Another good movie",
        "body": instance.title,
        "url": reverse("movie_detail", args=[instance.pk]),
    }

    if instance.poster_url:
        payload["icon"] = instance.poster_url

    log.warning("\nMovie's post_save triggered 'notify_users_of_new_movie' function")

    imdb_rating = instance.imdb_rating

    good_movie_imdb_threshold = 7
    if imdb_rating is None or imdb_rating < good_movie_imdb_threshold:
        log.warning(f"IMDB rating too low ({imdb_rating}). Skipping notifications.")
        return

    log.warning(f"Movie {instance} has a rating of {imdb_rating}. Preparing to notify subscribers")

    paid_for_membership_permission = Permission.objects.get(codename="paid_for_membership")

    for user in CustomUser.objects.filter(Q(user_permissions=paid_for_membership_permission)):
        log.warning(f"Sending push notification to prime membership user: {user}\n")
        send_user_notification(user=user, payload=payload)
