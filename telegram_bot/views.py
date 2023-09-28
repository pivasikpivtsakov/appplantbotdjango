from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class TgWebhookView(APIView):
    def post(self, request: Request):
        update = UpdateSerializer(data=request.data)
        return Response(status=200)
