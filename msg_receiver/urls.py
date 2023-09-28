from django.urls import path

from msg_receiver.views import ReceiverView, ListMessagesView

urlpatterns = [
    path("", ReceiverView.as_view()),
    path("list/", ListMessagesView.as_view())
]
