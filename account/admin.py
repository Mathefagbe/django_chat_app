from django.contrib import admin
from .models import CustomUsers,UserProfile
from django.contrib.auth.admin import UserAdmin
from .forms import *
from django.utils.translation import gettext_lazy as _

class CustomAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangerForm
    model=CustomUsers
    list_display = ['username','email', 'is_staff',]
    ordering=[]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('email',"username",'full_name',"password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ( "password",)}),
        (_("Personal info"),
          {
            "fields": ("full_name",
                       "username",
                     "email",
                    
                                 )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(CustomUsers,CustomAdmin)

admin.site.register(UserProfile)