from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUsers



class CustomUserChangerForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model=CustomUsers
        fields=['username','full_name','password','email']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=CustomUsers
        fields=['username','full_name','password','email']
    