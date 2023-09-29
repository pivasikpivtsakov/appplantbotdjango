import logging

from django.apps import AppConfig

from telegram_api.methods import set_webhook

logger = logging.getLogger(__name__)


class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self) -> None:
        logger.debug("setting webhook...")
        webhook_result = set_webhook()
        logger.info(f"setwebhook result: \n {webhook_result}")
