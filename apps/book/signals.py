from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.book.models import LostAnimal


@receiver(post_save, sender=LostAnimal)
def send_update(sender, instance, created, **kwargs):
    if created:
        instance.notify_telegram_bot()
