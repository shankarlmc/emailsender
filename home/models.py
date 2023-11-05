from django.db import models
from django.contrib.auth.models import Group, User
from django.urls import reverse


class Notification(models.Model):
    """
    The notification model.
    Admins can create, send, update, and delete notifications.
    """
    receiver = models.ManyToManyField(
        User, blank=True, related_name='noti_receiver')
    receiver_group = models.ManyToManyField(
        Group, blank=True, related_name='noti_receiver_group',
        help_text='Select the group to send the notification to. If you select a group, the notification will be sent to all the users in that group. If you select a user, the notification will be sent to that user only. If you select both, the notification will be sent to both the user and the group.'
    )
    subject = models.CharField(max_length=254, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    seen_by = models.ManyToManyField(User, blank=True)
    path = models.CharField(max_length=254, null=True,
                            blank=True)
    attachment = models.FileField(
        upload_to='notifications/attachments/', null=True, blank=True)
    push_notification = models.BooleanField(default=True)
    send_email = models.BooleanField(default=False)
    send_message = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    mail_sent_to = models.ManyToManyField(
        User, blank=True, related_name='noti_mail_sent_to')

    def __str__(self):
        return "Notification #{}".format(self.pk)

    @property
    def short_message(self):
        return self.message[:50]

    @property
    def receiver_emails(self):
        RECEIVER_USER_EMAILS = []
        receiver_users = self.receiver
        receiver_groups = self.receiver_group
        for group in receiver_groups:
            pass
        for user in receiver_users:
            RECEIVER_USER_EMAILS.append(user.email)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    @staticmethod
    def is_mail_sent_to(cls, user):
        """ Returns True if the notification is sent to the user, False otherwise. """
        if user in cls.mail_sent_to.all():
            return True
        return False

    # def get_absolute_url(self):
    #     return reverse("notification-detail", kwargs={"id": self.pk})

    @property
    def is_seen(self):
        for receiver in self.receiver.all():
            if receiver in self.seen_by.all():
                return True
        return False

    def save(self, *args, **kwargs):
        # if not self.path:
        #     self.path = reverse('notification_detail', kwargs={'id': self.pk})
        if self.pk is not None:
            self.created_at = Notification.objects.get(pk=self.pk).created_at
        super(Notification, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class ScheduledEmail(models.Model):
    email = models.ForeignKey(Notification, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField(auto_now=True)
    is_sent = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.email.subject} is scheduled at {self.scheduled_time}'
