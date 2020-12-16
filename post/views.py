
# rets_framework
from rest_framework.response import Response
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.permissions import IsAuthenticated


# Models
from .models import Post
from accounts.models import User


# Serializer
from .serailizers import PostSerailizer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from followers.serializers import ListFollowersSerailzier


class getPostByNickName(ListAPIView):

    """
      Obtiene todos los videos que a subido
      un usuario en particular
    """

    permission_classes = [IsAuthenticated]
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


    def post(self,request):
        user = request.user
        return Response('create post')



class getPostByFollower(ListAPIView):


    """
      Obtiene todos los videos de todos
      los usuarios al los que esta siguiendo
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerailizer
    pagination_class = LimitOffsetPagination


    def get_queryset(self) -> list:
        user = self.request.user
        followList = ListFollowersSerailzier().get_follower_list(user=user)
        usersListObject = User.objects.filter(nickName__in=followList)
        postList = Post.objects.filter(user__in=usersListObject)
        return postList


