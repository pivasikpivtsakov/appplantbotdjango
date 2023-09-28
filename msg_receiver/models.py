from django.db import models

from users.models import CustomUser


class MessageHistory(models.Model):
    sent_at = models.DateTimeField(blank=False, null=False)
    text = models.CharField(blank=False, null=False, max_length=4096)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
