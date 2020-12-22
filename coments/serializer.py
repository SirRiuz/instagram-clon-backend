

# rest_framework
from rest_framework import serializers


# Models
from post.models import Post
from .models import (Coment,SubComent)



class SubComentSerailizer(serializers.ModelSerializer):

    class Meta(object):
        model = SubComent
        fields = ['id' ,'text','toComet', 'posteador']

class GetComentSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Coment
        fields = [ 'id' ,'subComentLength', 'contenType','postTo' , 'contentUrl' ,'text' ,'postCommendDate','posteador' ]



class ComentSerailizer(serializers.Serializer):

    postId = serializers.CharField(required=False)
    text = serializers.CharField(required=False)
    #posteador = serializers.CharField(required=False)
    
    def create_coment(self,postId,userObject,text) -> (dict):
        try:
            postObject = Post.objects.get(id=postId)
            comentObject = Coment.objects.create(
                post=postObject,
                user=userObject,
                text=text
            )
            return({
                'data':{
                    'comentId':comentObject.id,
                    'creator':comentObject.user.nickName,
                    'mesege':'Coment create !'
                }
            })
        except Exception as e:
            return ({
                'error':{
                    'type-error':'post-error',
                    'messege':'El post no existe'
                }
            })



