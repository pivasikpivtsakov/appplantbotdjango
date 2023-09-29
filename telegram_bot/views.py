import logging

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

import telegram_api.models
from telegram_methods import send_to_tg_bot
from users.models import CustomUser

logger = logging.getLogger(__name__)


class TgWebhookView(APIView):
    def post(self, request: Request):
        logger.info(f"received update from telegram: {request.data}")
        update = telegram_api.models.Update.drf_serializer(data=request.data)
        if update.is_valid():
            data = update.validated_data
            msg_text = data["message"]["text"].strip()
            chat_id = data["message"]["chat"]["id"]
            if msg_text == "/start":
                msg_sending_result = send_to_tg_bot(
                    "Добрый день! "
                    "Пожалуйста, введите ваш логин, чтобы связать бота с сервисом и начать получать сообщения.",
                    chat_id,
                )
                if msg_sending_result["ok"] is False:
                    logger.warning(f"something bad when sending message to tg: {msg_sending_result} chat id: {chat_id}")
                    return Response(status=400, data={"telegram_error_text": msg_sending_result["description"]})
            else:
                user = CustomUser.objects.get(telegram_id=chat_id)
                if not user:

                    msg_sending_result = send_to_tg_bot(
                        "Логин установлен. Теперь введите токен",
                        chat_id,
                    )
                else:
                    if user.user_token is None:
                        user.telegram_id = chat_id
                        user.save()
                        msg_sending_result = send_to_tg_bot(
                            "Токен установлен. Бот успешно настроен на прием сообщений!",
                            chat_id
                        )
        else:
            logger.warning("update incorrect")
        return Response(status=200)
