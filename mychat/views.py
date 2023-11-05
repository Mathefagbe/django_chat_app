from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChatConversation,Contact
from django.db.models import Q,Max
import json
from django.http import JsonResponse

User=get_user_model()

class HomeView(LoginRequiredMixin,ListView):
    template_name='home.html'
    context_object_name='chats'
    login_url='login'
  
    def get_queryset(self):
        return ChatConversation.objects.select_related("firstUser","secondUser")\
            .prefetch_related("messages").filter(group_name__icontains=self.request.user.id)\
                .annotate(latest=Max("messages__stamp_time")).order_by("-latest").all()
    
class ChatScreen(LoginRequiredMixin,DetailView):
    login_url='login'
    pk_url_kwarg='pk'
    template_name='chatscreen.html'
    context_object_name='user'
    queryset=User.objects.all()

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        self.friend_username=User.objects.get(id=self.kwargs['pk'])
        self.sender_reciever=f"{self.request.user.id}_{self.friend_username.id}"
        self.receiver_sender=f"{self.friend_username.id}_{self.request.user.id}"
        context["histories"]=ChatConversation.objects.prefetch_related("messages").select_related("firstUser","secondUser")\
            .filter(Q(group_name=self.sender_reciever)|Q(group_name=self.receiver_sender)).first()
        return context


class Friends(LoginRequiredMixin,ListView):
    template_name='friends.html'
    context_object_name='friends'
    login_url='login'

    def get_queryset(self) -> QuerySet[Any]:
        return Contact.objects.select_related('user_from',"user_to").filter(user_from=self.request.user).all()


class FollowUser(LoginRequiredMixin,CreateView):
    login_url='login'

    def post(self, request,*args,**kwargs):
        current_user=self.request.user
        friend_id=json.loads(request.body)['user']
        friend=User.objects.get(username__iexact=friend_id)
        if Contact.objects.filter(user_from=current_user,user_to=friend).exists():
            Contact.objects.filter(user_from=current_user,user_to=friend).delete()
            return JsonResponse({
                    "message":"success",
                    "data":"Unfollow",
                    "status":200
                })
        else:
            Contact.objects.create(user_from=current_user,user_to=friend)
            return JsonResponse({
                    "message":"success",
                    "data":"Following",
                    "status":200
                })

