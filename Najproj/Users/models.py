from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUser(AbstractUser):
    pass

    # add additional fields here

    def __str__(self):
        return self.email


#class Profile(models.Model):
#    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#    EmployeeId = models.CharField(max_length=20, blank=True)
#   branch = models.CharField(max_length=30, blank=True)
#   NationalId = models.IntegerField(max_length=30, blank=True)
#   contact = models.CharField(max_length=20, blank=True)


#@receiver(post_save, sender=CustomUser)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#       Profile.objects.create(CustomUser=instance)


#@receiver(post_save, sender=CustomUser)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
