from django.utils import timezone

from django.core.mail import send_mail
from home.models import ScheduledEmail
from django.conf import settings


def send_scheduled_emails(sender, receiver):
    scheduled_mails = ScheduledEmail.objects.filter(
        is_sent=False, scheduled_time__lte=timezone.now())

    for item in scheduled_mails:
        send_mail(
            item.notification.subject,
            item.notification.message,
            settings.EMAIL_HOST_USER,  # Replace with your email address
            item.email.receiver_emails,
            fail_silently=False,
        )
        item.is_sent = True
        item.save()
