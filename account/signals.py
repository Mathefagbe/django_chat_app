from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUsers,UserProfile
from django.conf import settings

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender,instance,created,**kwargs):
    if created:
            instructor_profile=UserProfile()
            instructor_profile.user=instance
            instructor_profile.save()
            return instructor_profile
  