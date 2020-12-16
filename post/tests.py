
# Django
from django.test import TestCase


# Models
from .models import Post
from accounts.models import User


user = User.objects.get(nickName='Soy___Angi123')


for position in range(0,1000):
    Post.objects.create(
        id='oooo{position}'.format(position=position),
        user=user,
        text='Hola mundo',
        hashTags=''
    )

