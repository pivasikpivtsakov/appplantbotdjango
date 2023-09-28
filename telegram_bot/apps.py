from django.apps import AppConfig

from telegram_api.methods import set_webhook


class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self) -> None:
        set_webhook()
