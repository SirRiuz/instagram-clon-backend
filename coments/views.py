

# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


# serailizers
from .serializer import (ComentSerailizer,GetComentSerializer,SubComentSerailizer)


# Models
from .models import (Coment,SubComent)
from post.models import Post




# /api/v1/coments/:comentID - [ Get coments all video ]

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def getComentById(request,comentId) -> (Response):

    """
      Obtiene un comentario por su id 
    """
    try:
        coment = Coment.objects.get(id=comentId)
        comentSerializer = GetComentSerializer(coment,many=False)
        return Response(data={
            'data':comentSerializer.data
        })
    except Exception as e:
        return Response(data={
            'error':{
                'type-error':'coment-err',
                'messege':'El comentario no existe'
            }
        })




class ComentsManager(ListAPIView):

    permission_classes = [ IsAuthenticated ]
    pagination_class = LimitOffsetPagination
    serializer_class = GetComentSerializer

    """
      Obtiene todos los comentarios de
      un post
    """

    def get_queryset(self) -> (list):
        try:
            postId = self.kwargs['postId']
            postObject = Post.objects.get(id=postId)
            comentList = Coment.objects.filter(post=postObject).order_by('-postCommendDate')
            return comentList
        except Exception as e:
            return []



    # /api/v1/coments - [create coment]
    # Este metodo crea un comentario

    def post(self,request,postId) -> (Response):
        data = ComentSerailizer(data=request.POST)
        data.is_valid(raise_exception=True)
        comentResult = data.create_coment(
            postId=postId,
            userObject=request.user,
            text=data.data.get('text','')
        )
        return Response(data=comentResult)


    
    def delete(self,request) -> (Response):
        try:
            id = request.POST['comentId']
            Coment.objects.get(id=id).delete()
            return Response({
                'data':{
                    'messege':'El comentario se a eliminado'
                }
            })
        except Exception as e:
            print(e)
            return Response({
                'error':{
                    'type-error':'coment-not-found',
                    'messege':'El comentario no existe'
                }
            })





class SubComentsManager(ListAPIView):


    """
      Obtiene todos los subcomentarios
      de un comentario
    """

    permission_classes = [ IsAuthenticated ]
    serializer_class = SubComentSerailizer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        try:
            id = self.kwargs['comentId']
            comentObject = Coment.objects.get(id=id)
            subComentsObjectList = SubComent.objects.filter(coment=comentObject).order_by('-postCommendDate')
            return subComentsObjectList

        except Exception as e:
            return []



    def post(self,request,comentId) -> (Response):
        """
          Este metodo es el encargado de
          la creacion de sub comentarios
        """
        try:
            subComentObject = SubComent.objects.create(
                user=request.user,
                text=request.POST['text'],
                coment=Coment.objects.get(id=comentId)
            )
            return Response({
                'data':{
                    'messege':'SubCometario creado'
                }
            })
        except Exception as e:
            return Response({
                'error':{
                    'type-error':'coment-not-found',
                    'messege':'El comentarop no existe'
                }
            })




class SubComentsManagerById(APIView):


    def get(self,request,subComentId,comentId) -> (Response):
        """ Obtiene un sub comentario por el id """
        try:
            comentObject = Coment.objects.get(id=comentId)
            subComentObject = SubComent.objects.get(coment=comentObject , id=subComentId)
            subComentData = SubComentSerailizer(subComentObject,many=False)
            return Response({
                'data':subComentData.data
            })

        except Exception as e:
            print('[Error] -> ' , e)
            return Response({
                'error':{
                    'type-error':'coment-error',
                    'messege':'Error al obtener el comentario'
                }
            })


    def delete(self,request,subComentId,comentId) -> (Response):
        """ Elimina un sub comentario """

        try:
            userRequest = request.user
            comentObject = Coment.objects.get(id=comentId)
            subComentObject = SubComent.objects.get(coment=comentObject , id=subComentId)
            
            if (userRequest == subComentObject.user):
                subComentObject.delete()
                return Response({
                    'data':{
                        'messege':'El sub comentario a sido eliminado !'
                    }
                })

            else:
                return Response({
                    'error':{
                        'type-error':'permission-error',
                        'messege':'No tienes permitido eliminar esto !'
                    }
                })

        except Exception as e:
            print('[Error] -> ' , e)
            return Response({
                'error':{
                    'type-error':'delete-error',
                    'messege':'Ocuerrio un error al eliminar el subcomentario'
                }
            })



