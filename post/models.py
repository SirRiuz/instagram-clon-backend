
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



