from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Booking


@shared_task
def send_booking_email(user_id, booking_details):
    user = User.objects.get(id=user_id)
    subject = "Booking Confirmation"
    message = f"Hello {user.username},\n\nYour booking for {booking_details['listing']} has been confirmed.\n\nDetails:\n{booking_details}\n\nThank you!"
    recipient_list = [user.email]
    send_mail(subject, message, None, recipient_list, fail_silently=False)
    return "Email sent successfully!"

@shared_task
def send_booking_reminder():
    """Send a reminder email for upcoming bookings."""
    now = timezone.now()
    upcoming_bookings = Booking.objects.filter(date__gte=now, date__lt=now + timezone.timedelta(hours=24))

    for booking in upcoming_bookings:
        subject = "Upcoming Booking Reminder"
        message = f"Hello, you have an upcoming booking on {booking.start_date}. Please be prepared."
        send_mail(subject, message, None, [booking.user.email])

    return f"Sent {upcoming_bookings.count()} reminders."
