

# Rest_framework
from rest_framework import serializers


# models
from .models import LikePost,LikeComent
from post.models import Post
from coments.models import Coment



class comentLikeSerializer(serializers.Serializer):

    comentId = serializers.CharField(required=True)

    #  Este metodo hay que refactorizarlo !!!

    def create_like(self,user:object,comentId:str) -> (object):
        #LikePost.objects.create()
        try:
            comentObject = Coment.objects.get(id=comentId)
            likeResult = LikeComent.objects.filter(coment=comentObject,user=user)

            if likeResult:
                likeResult.delete()
                print('Eliminda')
                return ({
                    'data':{
                        'messege':'Like eliminado'
                    }
                })

            else:
                LikeComent.objects.create(coment=comentObject,user=user)
                print('Creado')
                return ({
                    'data':{
                        'messege':'Like creado'
                    }
                })

        except Exception as e:
            print('[Error] : ',e)
            return ({
                'error':{
                    'type-error':'like-error-created',
                    'messege':'Error al crear el like'
                }
            })




class postLikeSerializer(serializers.Serializer):

    postId = serializers.CharField(required=True)


    #  Este metodo hay que refactorizarlo !!!

    def create_like(self,user:object,postId:str) -> (object):
        #LikePost.objects.create()
        try:
            postObject = Post.objects.get(id=postId)
            likeResult = LikePost.objects.filter(post=postObject,user=user)

            if likeResult:
                likeResult.delete()
                return ({
                    'data':{
                        'messege':'Like eliminado'
                    }
                })

            else:
                LikePost.objects.create(post=postObject,user=user)
                return ({
                    'data':{
                        'messege':'Like creado'
                    }
                })

        except Exception as e:
            print('[Error] : ',e)
            return ({
                'error':{
                    'type-error':'like-error-created',
                    'messege':'Error al crear el like'
                }
            })








