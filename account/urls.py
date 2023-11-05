from django.contrib import admin
from django.urls import path
from .views import UserLoginView,SignUpView,UserView,Profile,UploadImage,UserLogoutView

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('sign-up/',SignUpView.as_view(),name='sign-up'),
    path('people/',UserView.as_view(),name="users"),
    path('profile/',Profile.as_view(),name="profile"),
    path('upload/',UploadImage.as_view(),name="upload"),
    path('logout/',UserLogoutView.as_view(),name='logout')
]
