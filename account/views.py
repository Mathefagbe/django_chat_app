from typing import Any
from django.core.handlers.wsgi import WSGIRequest
from django.db import models
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView,LogoutView
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView,ListView,DetailView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy,reverse
from django.http import JsonResponse
import json
from django.contrib.auth import (get_user_model, login as auth_login,
    logout as auth_logout
)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
User=get_user_model()



# class UserLogin(LoginView):
#     template_name="login.html"
    

#     def get_success_url(self) -> str:
#         return reverse("home")
     
class UserLoginView(LoginView):
    template_name='login.html'

    def post(self, request,*args,**kwargs):
            data=json.loads(request.body)
            user=authenticate(request,**data)
            if user is None:
                return JsonResponse({
                    "error":"Login credentials does not exist",
                    "data":[],
                    "status":"404"})
            else:
                auth_login(request,user)
                return JsonResponse({
                    "message":"success",
                    "data":[],
                    "status":200
                })
            
    def get_success_url(self) -> str:
        return reverse("home")


class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    template_name='sign-up.html'

    def post(self, request, *args, **kwargs):
            json_obj=json.loads(request.body)
            if User.objects.filter(username=json_obj['username']).exists():
                 return JsonResponse({
                   "error":"User with this credential already exist",
                   "data":[],
                   "status":404})
            else:
                user_obj=User()
                user_obj.username=json_obj['username']
                user_obj.email=json_obj['email']
                user_obj.full_name=json_obj['full_name']
                user_obj.set_password(json_obj['password'])
                user_obj.save()
                return JsonResponse({
                    "message":"success",
                    "data":[],
                    "status":201
                })

                
class UserView(LoginRequiredMixin,ListView):
    template_name='people.html'
    context_object_name="users"


    def get_queryset(self) -> QuerySet[Any]:
          return User.objects.prefetch_related("users_from","users_to").all().exclude(id=self.request.user.id)
    def get_context_data(self, **kwargs: Any):
         context=super().get_context_data(**kwargs)
         context['followings']=self.request.user.users_from.values_list("user_to",flat=True)
         return context
    

class Profile(LoginRequiredMixin,DetailView):
    template_name='profile.html'
    context_object_name='profile'

    def get_queryset(self):
          return UserProfile.objects.select_related("user").all()
    def get_object(self):
        try:
            obj = self.get_queryset().get(user=self.request.user)
        except self.get_queryset().model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': self.get_queryset().model._meta.verbose_name})
        return obj


class UploadImage(LoginRequiredMixin,CreateView):
     
     def post(self, request,*args,**kwargs):
          profileImage=request.FILES.get("profile")
          profile=UserProfile.objects.get(user=self.request.user)
          profile.image=profileImage
          profile.save()
          return JsonResponse({
                    "message":"success",
                    "data":"Profile Uploaded",
                    "status":201})
     
class UserLogoutView(View):
    
    def post(self, request, *args, **kwargs):
          auth_logout(request=request)
          return JsonResponse({
               "message":"logout successfull",
               "data":[],
               "status":200})