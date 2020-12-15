
# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Serializers
from .serializers import (
    FollowerSerailizer,
    ListFollowersSerailzier
)


@api_view(['GET','POST'])
def followerManager(request) -> Response:
    followerSerializer = FollowerSerailizer(data=request.data)
    followerSerializer.is_valid(raise_exception=True)
    dataResponse = followerSerializer.set_follow(followerSerializer.data)
    return Response(dataResponse)



@api_view(['GET','POST'])
def getFollowList(request) -> Response:
    followserailizer = ListFollowersSerailzier(data=request.data)
    followserailizer.is_valid(raise_exception=True)
    result = followserailizer.get_follower_list(data=followserailizer.data)
    return Response({
        'status':'ok',
        'result':result
    })




