import logging

from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from statistics import mean
from .models import Profile
from collections import Counter
import re

log = logging.getLogger(__name__)


@receiver(post_save, sender=Profile)
def update_profile_stats(sender, instance: Profile, created: bool, **kwargs):

    if created:
        log.warning(f"\nSkipping recalculation of watched_movies_average_rating for newly created profiles")
        return

    # temporarily disconnect listeners to prevent recursive call of update_profile_stats
    post_save.disconnect(update_profile_stats, sender=sender)

    log.warning(f"\nRecalculating profile stats for: {instance}\n")

    recalculate_watched_movies_average_rating(sender, instance)
    recalculate_watched_movies_genres(sender, instance)
    recalculate_watched_movies_years(sender, instance)

    # rec-nnect listeners
    post_save.connect(update_profile_stats, sender=sender)

def recalculate_watched_movies_average_rating(sender, instance: Profile):

    ratings_of_watched_movies = [m.imdb_rating for m in instance.watched_movies.all() if m.imdb_rating]
    new_average_rating = mean(ratings_of_watched_movies) if ratings_of_watched_movies else None

    log.warning(f"\nOld average_rating: {instance.watched_movies_average_rating}.\nNew average_rating: {new_average_rating}")

    instance.watched_movies_average_rating = new_average_rating
    instance.save()

def recalculate_watched_movies_genres(sender, instance: Profile):

    watched_movies_genres = [m.genre.strip() for m in instance.watched_movies.all() if m.genre]

    if not watched_movies_genres:
        instance.watched_movies_genres = None
        instance.save()
        return

    new_watched_movies_genres = ",".join(watched_movies_genres)
    new_watched_movies_genres = re.sub(r",\s*", ",", new_watched_movies_genres)
    new_watched_movies_genres = new_watched_movies_genres.split(",")

    new_watched_movies_genres = dict(Counter(new_watched_movies_genres))

    log.warning(f"\nOld watched_movies_genres: {instance.watched_movies_genres}.\nNew watched_movies_genres: {new_watched_movies_genres}")

    instance.watched_movies_genres = new_watched_movies_genres
    instance.save()

def recalculate_watched_movies_years(sender, instance: Profile):

    watched_movies_years = [x.year for x in instance.watched_movies.all() if x.year]

    if not watched_movies_years:
        instance.watched_movies_years = None
        instance.save()
        return

    watched_movies_years = dict(Counter(watched_movies_years))

    log.warning(f"\nOld watched_movies_years: {instance.watched_movies_years}.\nNew watched_movies_years: {watched_movies_years}")

    instance.watched_movies_years = watched_movies_years
    instance.save()
