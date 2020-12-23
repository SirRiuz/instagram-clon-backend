
# rest_framework
from rest_framework import serializers


# Models
from .models import Post


class PostSerailizer(serializers.ModelSerializer):

    class Meta(object):
        model = Post
        fields = [
            'id' ,'text','likes',
            'coments','videoDir',
            'reproductions','hashTags',
            'postDate','posteador'
        ]


    def create_post(self,user,data,postInstance) -> object:
        try:
            postInstance.objects.create(
                id=data['id'],
                text=data['text'],
                hashTags=data['hashTags'],
                user=user
            )
            return ({
                'status':'ok',
                'messege':'Se a creado la publicacion '
            })
            
        except Exception as e:
            return ({
                'status':'error',
                'type-error':'post-create-error',
                'messege':'Error al crear la publicacion : {e}'.format(e=e)
            })








