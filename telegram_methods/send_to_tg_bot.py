from telegram_api.methods import send_message, SendMessageBody


def send_to_tg_bot(msg: str, user: int):
    return send_message(SendMessageBody(chat_id=user, text=msg))
