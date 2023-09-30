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
            if data["message"]:
                msg_text = data["message"]["text"].strip()
                chat_id = data["message"]["chat"]["id"]
                self._process_message(msg_text, chat_id)
        else:
            logger.warning("update incorrect")
        return Response(status=200)

    def _process_message(self, msg_text: str, chat_id: int):
        if msg_text == "/start":
            msg_sending_result = send_to_tg_bot(
                "Добрый день! "
                "Пожалуйста, введите ваш логин, чтобы связать бота с сервисом и начать получать сообщения.",
                chat_id,
            )
        else:
            user = CustomUser.objects.filter(telegram_id=chat_id).first()
            if not user:
                user_by_login = CustomUser.objects.filter(login=msg_text).first()
                if user_by_login:
                    user_by_login.telegram_id = chat_id
                    user_by_login.save()
                    msg_sending_result = send_to_tg_bot(
                        "Логин установлен. Теперь введите токен",
                        chat_id,
                    )
                else:
                    msg_sending_result = send_to_tg_bot(
                        "Такой пользователь не зарегистрирован. "
                        "Пожалуйста, пройдите регистрацию через сервис. ",
                        chat_id,
                    )
            else:
                if not user.user_token:
                    msg_sending_result = send_to_tg_bot(
                        "Сначала нужно задать токен в сервисе! ",
                        chat_id,
                    )
                else:
                    if user.user_token == msg_text:
                        user.user_token_verified = True
                        user.save()
                        msg_sending_result = send_to_tg_bot(
                            "Токен установлен. Бот успешно настроен на прием сообщений!",
                            chat_id,
                        )
                    else:
                        msg_sending_result = send_to_tg_bot(
                            "Токен не совпадает, попробуйте ещё раз.",
                            chat_id,
                        )
