
# Utils
from .utils import *


# rets_framework
from rest_framework.response import Response
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .customPagination import customPagination

# Models
from .models import Post
from accounts.models import User


# Serializer
from .serailizers import PostSerailizer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from followers.serializers import ListFollowersSerailzier


class PostManager(ListAPIView):

    """
      Obtiene todos los videos que a subido
      un usuario en particular
    """

    permission_classes = [ IsAuthenticated ]
    serializer_class = PostSerailizer
    pagination_class = LimitOffsetPagination


    def get_queryset(self) -> list:
        try:
            nickName = self.request.data['nickName']
            user = User.objects.get(nickName=nickName)
            user_post = Post.objects.filter(user=user)
            return user_post
        except Exception as e:
            return []


    def post(self,request) -> Response:
        user = request.user
        postSerailizer = PostSerailizer(data=request.POST)
        postSerailizer.is_valid(raise_exception=True)
        result = postSerailizer.create_post(
          data=postSerailizer.data,
          user=request.user,
          postInstance=Post
        )
        return Response(result,status=status.HTTP_200_OK)



class getPostByFollower(ListAPIView):


    """
      Obtiene todos los videos de todos
      los usuarios al los que esta siguiendo
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerailizer
    pagination_class = customPagination


    def get_queryset(self) -> list:        
        user = self.request.user
        followList = ListFollowersSerailzier().get_follower_list(user=user)
        usersListObject = User.objects.filter(nickName__in=followList)
        postList = Post.objects.filter(user__in=usersListObject).order_by('-postDate')
        return postList


class PostManagerById(APIView):


    """
      Esta clase se encarga de obtener
      editar y eliminar un post 
      atraves del id
    """

    permission_classes = [IsAuthenticated]

    def get(self,request,id) -> Response:
        """
          Este metodo se engarga obtener un 
          post atraves del id
        """
        try:
          postObject = Post.objects.get(id=id)
          return Response({
            'data':{
              'post':{
                'id':postObject.id,
                'messege':postObject.text,
                'video':'',
                'likes':postObject.likes,
                'hastTags':postObject.hashTags,
                'reproductions':postObject.reproductions
              },
              'posteador':postObject.posteador
            }
          },status=status.HTTP_200_OK)

        except Exception as e:
          return Response({
            'error':{
              'type-error':'post-not-exit',
              'messge':'El post no existe ...'
            }
          },status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id) -> Response:
        """
          Este metodo es el engargado de eliminar un
          post, pero solo lo va a poder hacer el 
          usuario que lo publico , los demas usuarios
          no podran eliminarlo
        """
        try:
          requestUser = request.user
          post = Post.objects.get(id=id)
          is_posteador = isPosteador(requestUser,post)

          if is_posteador:
            post.delete()
            return Response({
              'data':{
                'messege':'Post eliminado'
              }
            })

          else:
            return Response({
              'error':{
                'type-error':'permission-error',
                'messege':'No tienes permisis para eliminar este post'
              }
            },status=status.HTTP_400_BAD_REQUEST)
          

        except Exception as e:
          print('[Error] -> ',e)
          return Response({
            'error':{
              'type-errpr':'404-post-errpr',
              'messege':'El post no existe'
            }
          },status=status.HTTP_404_NOT_FOUND)


    def put(self,request,id) -> Response:
        """
          Este metodo es el de editar una 
          publicacion. Solo se podra editar 
          el texto y los hashTags

          Solo el posteador tendra el permiso
          de editar la publicacion
        """

        try:
          post = Post.objects.get(id=id)
          is_posteador = isPosteador(request.user,post)
          if is_posteador:
            data = request.data
            post.text = data.get('text',post.text)
            post.hashTags = data.get('hashTags',post.hashTags)
            post.save()

            return Response({
              'data':{
                'status':'ok',
                'messege':'La publicacion a sido modificada'
              }
            })

          else:
            return Response({
              'error':{
                'type-error':'acces-denig',
                'messege':'No tienes permisos de escritura para este post'
              }
            })
          
        except Exception as e:
          return Response({
            'error':{
              'type-errpr':'404-post-errpr',
              'messege':'El post no existe'
            }
          },status=status.HTTP_404_NOT_FOUND)






