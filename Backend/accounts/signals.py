from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)   #the function will be called whenever it receives the post_save signal from the sender who is User
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# We also need to go ahead and import the signals we have used.
# In order to do that, we go to the apps.py file    
 