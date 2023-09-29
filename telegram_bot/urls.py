from django.urls import path
from django.conf import settings

from telegram_bot.views import TgWebhookView

urlpatterns = [
    path(f"{settings.TG_API_TOKEN}/", TgWebhookView.as_view())
]
