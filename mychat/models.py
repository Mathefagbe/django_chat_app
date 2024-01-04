from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class ChatConversation(models.Model):
    firstUser=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_from',null=True)
    group_name=models.CharField(max_length=30,null=True)
    secondUser=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_to',null=True)

    def __str__(self) -> str:
        return f"{self.firstUser.username} chat {self.secondUser.username}"

class Messages(models.Model):
    conversation=models.ForeignKey(ChatConversation,on_delete=models.CASCADE,related_name='messages')
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_sender')
    message=models.CharField(max_length=500,null=True)
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_receiver',null=True)
    stamp_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.sender.username} message {self.receiver.username}"


class Contact(models.Model):
    user_from=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users_from')
    user_to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users_to')
    stamptime=models.DateTimeField(auto_now_add=True)


    
    def __str__(self) -> str:
        return f"{self.user_from.username} follows {self.user_to.username}"