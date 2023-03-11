from django.db.models import signals
from django.dispatch import receiver

from .models import Message, Doctor
import asyncio
from django.dispatch import receiver
from django.db.models.signals import post_save

from newclients.bot import sendd

#
# def form_sender(sender, instance, **kwargs):
#     asyncio.run(sendd(instance.title, instance.body, instance.author))
#     return True
#
#
# post_save.connect(form_sender, sender=Message)


@receiver(signals.post_save, sender=Message)
def create_message(sender, instance, created, **kwargs):
    doctor = str(Doctor.objects.get(id=instance.doctor))
    asyncio.run(sendd(instance.first_name, instance.phone, doctor, instance.date, instance.time))
    print(instance)
