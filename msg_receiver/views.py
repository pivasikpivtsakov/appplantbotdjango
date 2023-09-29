import datetime
import time

from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from msg_receiver.models import MessageHistory
from msg_receiver.serializers import MessageSerializer
from telegram_methods import send_to_tg_bot
from users.models import CustomUser


class ReceiverView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            now = datetime.datetime.now()  # timezone
            user = request.user
            serializer.save(sent_at=now, sender=user)
            tg_id = user.telegram_id
            if tg_id is None:
                return Response(status=400, data="Connect via telegram bot first!")
            send_to_tg_bot(data["text"], tg_id)
            return Response("hello")
        else:
            return Response(status=400)


class ListMessagesView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        return MessageHistory.objects.all()
