import logging

from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from statistics import mean
from .models import Profile

log = logging.getLogger(__name__)


@receiver(post_save, sender=Profile)
def update_profile_stats(sender, instance: Profile, created: bool, **kwargs):

    if created:
        log.warning(f"\nSkipping recalculation of watched_movies_average_rating for newly created profiles")
        return

    # temporarily disconnect listeners to prevent recursive call of update_profile_stats
    post_save.disconnect(update_profile_stats, sender=sender)

    recalculate_watched_movies_average_rating(sender, instance)

    # rec-nnect listeners
    post_save.connect(update_profile_stats, sender=sender)

def recalculate_watched_movies_average_rating(sender, instance: Profile):

    ratings_of_watched_movies = [m.imdb_rating for m in instance.watched_movies.all() if m.imdb_rating]
    new_average_rating = mean(ratings_of_watched_movies) if ratings_of_watched_movies else None

    log.warning(f"\nRecalculating average average_rating for profile: {instance}")
    log.warning(f"Old average_rating: {instance.watched_movies_average_rating}.\n New average_rating: {new_average_rating}")

    instance.watched_movies_average_rating = new_average_rating
    instance.save()
