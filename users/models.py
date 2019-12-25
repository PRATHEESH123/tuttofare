from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# 3rd party
from rest_framework.authtoken.models import Token
from cuser.models import AbstractCUser


class User(AbstractCUser):
    pass


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)