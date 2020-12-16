
# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.permissions import IsAuthenticated


# Serializers
from .serializers import (
    FollowerSerailizer,
    ListFollowersSerailzier
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def followerManager(request) -> Response:
    followerSerializer = FollowerSerailizer(data=request.data)
    followerSerializer.is_valid(raise_exception=True)
    dataResponse = followerSerializer.set_follow(
        userObject=request.user,
        follow=followerSerializer.data['following']
    )
    return Response(dataResponse)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getFollowList(request) -> Response:
    user = request.user
    followserailizer = ListFollowersSerailzier()
    result = followserailizer.get_follower_list(user=user)
    return Response({
        'status':'ok',
        'result':result
    })




