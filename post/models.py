
# test
import random


# Django
from django.db import models


# Models
from accounts.models import User


class Post(models.Model):

    id = models.CharField(max_length=250,primary_key=True,help_text='Id del post')

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    text = models.CharField(max_length=350,blank=True,null=True,help_text='Texto de la publicacion')
    hashTags = models.CharField(max_length=400,blank=True,null=True,help_text='Tags de la publicacion')

    postDate = models.DateTimeField(auto_now_add=True)


    @property
    def posteador(self) -> dict:
        return {
            'id':self.user.id,
            'imagePicture':'/image/{id}.png'.format(id=self.user.id),
            'nickName':self.user.nickName,
            'name':self.user.name
        }

    @property
    def PointRank(self) -> float:
        return 0.0


    @property
    def reproductions(self) -> int:
        return 0


    @property
    def shareNum(self) -> int:
        return 0

    @property
    def likes(self) -> int:
        return random.randint(0,1000)

    @property
    def videoDir(self) -> str:
        return '/video/{postId}.mp4'.format(postId=self.id)




