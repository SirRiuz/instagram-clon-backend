

# rets_framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Models 
from .models import Followers
from accounts.models import User

class FollowerSerailizer(serializers.Serializer):
    
    tokenFollower = serializers.CharField(required=True)     #Yo
    following = serializers.CharField(required=True)


    def is_following(self,userFollower,userFollowing) -> bool:
        follow = Followers.objects.filter(
            userFollower=userFollower,
            userFollowing=userFollowing
        )
        if follow:
            return True

        return False


    def set_follow(self,data):
        token = data['tokenFollower']
        nickName = data['following']

        try:
            userFollower = Token.objects.get(key=token)
            userFollowing = User.objects.get(nickName=nickName)
            
            is_follow = self.is_following(
                userFollower=userFollower.user,
                userFollowing=userFollowing
            )

            if is_follow:
                return ({
                    'status':'ok',
                    'messege':'Ya estas siguiendo a {following}'.format(following=nickName)
                })

            else:
                if userFollower.user == userFollowing:
                    return ({
                        'status':'error',
                        'type-error':'auto-follow',
                        'messege':'No puedes seguirte a ti mismo ...'
                    })

                else:
                    follow = Followers.objects.create(
                        userFollower=userFollower.user,
                        userFollowing=userFollowing
                    )
                    return ({
                        'status':'ok',
                        'messege':'Ahora estas siguiendo a {following}'.format(following=follow.userFollowing)
                    })

        except Exception as e:
            return({
                'status':'error',
                'type-error':'follow-error',
                'messege':str(e)
            })


            