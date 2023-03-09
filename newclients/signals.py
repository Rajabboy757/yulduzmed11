from django.db.models import signals
from django.dispatch import receiver

from .models import Message

# @receiver(signals.pre_save, sender=Message)
# def valid_order(sender, instance, **kwargs):
#     print(instance)

# post_save method
@receiver(signals.post_save, sender=Message)
def create_message(sender, instance, created, **kwargs):
    print(instance)
    print(sender)