

from django.test import TestCase

# Models
from .models import SubComent
from .models import Post
from .models import User
from .models import Coment


user = User.objects.get(nickName='root')
post = Post.objects.get(id='asdaidbasds')


# getComent



SubComent.objects.create(
    user=user,
    text='Esto es un subcomentario',
    coment=Coment.objects.get(id=2)
)