
# rest_framework
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# Serializers
from .serializers import (postLikeSerializer,comentLikeSerializer)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createLikeByComent(request,comentId) -> (Response):
    data = {'comentId':comentId}

    serailizer = comentLikeSerializer(data=data)
    serailizer.is_valid(raise_exception=True)
    resultLike = serailizer.create_like(
        user=request.user,
        comentId=serailizer.data['comentId']
    )

    return Response(resultLike)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createLikeByPost(request,postId) -> (Response):

    data = {'postId':postId}

    serailizerResult = postLikeSerializer(data=data)
    serailizerResult.is_valid(raise_exception=True)

    likePostResult = serailizerResult.create_like(
        user=request.user,
        postId=serailizerResult.data['postId']
    )

    return Response(likePostResult)