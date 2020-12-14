
# Django
from django.db import models
from rest_framework.authtoken.models import Token


# Models
from accounts.models import User


class Followers(models.Model):
    
    userFollower = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_follower'
    ) #Yo
    
    userFollowing = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_following'
    ) # Al que sigo