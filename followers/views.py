
# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Serializers
from .serializers import FollowerSerailizer


@api_view(['GET','POST'])
def followerManager(request):
    followerSerializer = FollowerSerailizer(data=request.data)
    followerSerializer.is_valid(raise_exception=True)
    dataResponse = followerSerializer.set_follow(followerSerializer.data)
    return Response(dataResponse)






