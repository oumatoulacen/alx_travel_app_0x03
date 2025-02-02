from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_email_confirmation(user, booking_details):
    subject = "Booking Confirmation"
    message = f"Hello {user.username},\n\nYour booking is confirmed!\n\nDetails:\n{booking_details}\n\nThank you!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
    return "Email sent successfully!"
