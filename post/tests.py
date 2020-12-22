
# Django
from django.test import TestCase


# Models
from .models import Post
from accounts.models import User


user = User.objects.get(nickName='Soy___Angi123')


Post.objects.create(
        id='TEXTPOSYASUDGASUDASDASDA',
        user=user,
        text='Este es un por de pruebaaaaaaaaaaaaaaaaaaaaaaaaa',
        hashTags=''
)

