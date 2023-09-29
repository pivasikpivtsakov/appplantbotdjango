import logging

from rest_framework.exceptions import APIException

from telegram_api.methods import send_message, SendMessageBody

logger = logging.getLogger(__name__)


def send_to_tg_bot(msg: str, user: int):
    result = send_message(SendMessageBody(chat_id=user, text=msg))
    if result["ok"] is False:
        logger.warning(
            f"something bad when sending message to tg: {result} chat id: {user}"
        )
        raise APIException(code='400', detail={"telegram_error_text": result["description"]})
    return result
