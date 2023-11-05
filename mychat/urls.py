from django.contrib import admin
from django.urls import path
from .views import HomeView,ChatScreen,FollowUser,Friends

urlpatterns = [
    path('chats/',HomeView.as_view(),name='home'),
    path('chat/<pk>/',ChatScreen.as_view(),name='chat'),
    path('follow/',FollowUser.as_view(),name='follow'),
    path('following/',Friends.as_view(),name='friends'),
]
