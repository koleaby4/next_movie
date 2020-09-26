import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from users.models import CustomUser

log = logging.getLogger(__name__)

# fetch and save reviews when a new movie is created
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        log.warning(f"Creating new profile for {instance}")
        Profile.objects.create(user=instance)
