from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

@shared_task
def send_booking_email(user_id, booking_details):
    user = User.objects.get(id=user_id)
    subject = "Booking Confirmation"
    message = f"Hello <bold>{user.username}</bold>,\n\nYour booking for {booking_details['listing']} has been confirmed.\n\nDetails:\n{booking_details}\n\nThank you!"
    recipient_list = [user.email]
    print(f"from {settings.EMAIL_HOST_USER}")
    print(f"password {settings.EMAIL_HOST_PASSWORD}")
    send_mail(subject, message, None, recipient_list, fail_silently=False)
    print(f"Sending email to {user.email}")
    return "Email sent successfully!"
