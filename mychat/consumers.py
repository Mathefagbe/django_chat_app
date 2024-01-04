from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import ChatConversation,Messages
from django.contrib.auth import get_user_model
from django.db.models import Q


User=get_user_model()

class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.accept()
        self.user=self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.receiver=User.objects.get(id=self.id)
        self.sender_reciever=f"{self.user.id}_{self.receiver.id}"
        self.receiver_sender=f"{self.receiver.id}_{self.user.id}"
        self.room_name=None

        if ChatConversation.objects.filter(Q(group_name=self.sender_reciever)|Q(group_name=self.receiver_sender)).exists():
            self.room_name=ChatConversation.objects.get(Q(group_name=self.sender_reciever)|Q(group_name=self.receiver_sender))
        else:
            self.room_name=ChatConversation.objects.create(firstUser=self.user,group_name=self.sender_reciever,secondUser= self.receiver)
                
        async_to_sync(self.channel_layer.group_add)(
        self.room_name.group_name,
        self.channel_name)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
        self.room_name.group_name,
            self.channel_name
            )
        super().disconnect(code)

    #receive message from incoming socket
    def receive_json(self, content, **kwargs):
        async_to_sync(self.channel_layer.group_send)(
        self.room_name.group_name,
        {
            'type': 'chat_message',
            'message': content['message'],
            'sender':self.user.username,
            "senderImage":self.user.user_profile.image.url,
        }
        )
        Messages.objects.create(
            conversation=self.room_name,
            sender=self.user,
            message=content['message'],
            receiver=self.receiver
        )
    def chat_message(self,event):
        self.send_json(event)


    