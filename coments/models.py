
# Django
from django.db import models


# Models
from post.models import Post
from accounts.models import User


class AbstractBaseComent (models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)

    contenType = models.CharField(max_length=100,blank=True,null=True)
    contentUrl = models.URLField(blank=True,null=True)
    text = models.CharField(max_length=250,null=False,blank=False)
    postCommendDate = models.DateTimeField(auto_now_add=True)


    @property
    def posteador(self) -> (dict):
        return ({
            'posteador':{
                'id':self.user.id,
                'imageProfile':'',
                'nickName':self.user.nickName,
                'name':self.user.name
            }
        })


    class Meta(object):
        abstract=True


class Coment(AbstractBaseComent):

    post = models.ForeignKey(to=Post , on_delete=models.CASCADE,related_name='Post')

    @property
    def postTo(self) -> (str):
        return self.post.id

    @property
    def subComentLength(self) -> (int):
        lenSubComents = SubComent.objects.filter(coment=self)
        return len(lenSubComents)


    


class SubComent (AbstractBaseComent):
    coment = models.ForeignKey(to=Coment,on_delete=models.CASCADE)

    @property
    def toComet(self):
        return self.coment.id
