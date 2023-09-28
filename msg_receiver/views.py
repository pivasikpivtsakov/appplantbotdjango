import datetime
import time

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from msg_receiver.models import MessageHistory
from msg_receiver.serializers import MessageSerializer
from telegram_methods import send_to_tg_bot


class ReceiverView(APIView):
    def post(self, request: Request) -> Response:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            now = datetime.datetime.now()  # timezone
            serializer.save(sent_at=now)
            send_to_tg_bot(data["text"], 1)
            return Response("hello")
        else:
            return Response(status=400)


class ListMessagesView(APIView):
    def get(self, request: Request):
        return MessageHistory.objects.all()
