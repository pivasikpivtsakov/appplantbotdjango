from rest_framework import serializers

from msg_receiver.models import MessageHistory


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = ("message", )
        extra_kwargs = {
            "sent_at": {}
        }

    message = serializers.CharField(
        source="text", required=True, allow_blank=False, allow_null=False, max_length=4096,
    )
