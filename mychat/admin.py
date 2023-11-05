from django.contrib import admin
from .models import ChatConversation,Messages,Contact


admin.site.register(ChatConversation)
admin.site.register(Messages)
admin.site.register(Contact)
# Register your models here.
