
# Django
from django.test import TestCase



# Models
from post.models import Post
from .models import (LikePost,LikeComent)
from coments.models import *


# serializer
from .serializers import (postLikeSerializer,comentLikeSerializer)


def createLikeToPost():
    postObject = Post.objects.get(id='jh123ug8rgfduqbjebv182313g12')
    ser = comentLikeSerializer(data={'comentId':'13'})
    ser.is_valid(raise_exception=True)
    res = ser.create_like(user=postObject.user , comentId='13')

createLikeToPost()








