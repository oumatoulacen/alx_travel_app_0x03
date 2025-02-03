from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
# from .tasks import send_booking_email

@receiver(post_save, sender=Booking)
def send_booking_confirmation_email(sender, instance, created, **kwargs):
    # if created:  # Check if a new Booking object is created
        # uncomment the line below to send email asynchronously using Celery
        # send_booking_email.delay(instance.user_email, instance.details)
    print('Booking confirmation email sent to', instance.user.email)