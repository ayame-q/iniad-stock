from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, **kwargs):
    try:
        Profile.objects.get(user=kwargs["instance"])
    except Profile.DoesNotExist:
        Profile.objects.create(user=kwargs['instance'])
