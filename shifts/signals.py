from .models import Shift, ShiftProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= Shift)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ShiftProfile.objects.create(shift=instance)