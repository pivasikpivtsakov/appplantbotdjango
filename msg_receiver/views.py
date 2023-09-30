from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from msg_receiver.models import MessageHistory
from msg_receiver.serializers import MessageSerializer, MessageOutSerializer
from telegram_methods import send_to_tg_bot


class ReceiverView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            now = timezone.now()
            user = request.user
            serializer.save(sent_at=now, sender=user)
            tg_id = user.telegram_id
            if tg_id is None:
                return Response(status=400, data="Connect via telegram bot first!")
            if user.user_token_verified is False:
                return Response(status=400, data="token verification failed")
            send_to_tg_bot(
                f"{user.screen_name}, я получил от тебя сообщение:\n"
                f"{data['text']}",
                tg_id
            )
            return Response(status=200)
        else:
            return Response(status=400)


class ListMessagesView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        user = request.user
        messages = MessageHistory.objects.filter(sender=user)
        serializer = MessageOutSerializer(messages, many=True)
        return Response(data=serializer.data)
