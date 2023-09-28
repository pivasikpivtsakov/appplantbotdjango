from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from users.serializers import SignUpSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.services import get_user_data
from users.models import CustomUser


class RegisterView(APIView):
    permission_classes = []

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """
        Возвращает email юзера и 201 статус, если регистрация прошла успешно
        :param request:
        :return:
        """
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'email': serializer.data['email']}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_data = get_user_data(request.user.id)
            serializer = UserProfileSerializer(user_data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(data={'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)


class CreateTelegramTokenView(APIView):
    def post(self, request: Request):
        return Response(status=200)
