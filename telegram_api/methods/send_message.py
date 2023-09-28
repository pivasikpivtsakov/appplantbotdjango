from ..utils import make_tg_request, Method, FormDataModel


class Body(FormDataModel):
    chat_id: str | int
    text: str


def send_message(body: Body):
    return make_tg_request(Method.SEND_MESSAGE, body)
