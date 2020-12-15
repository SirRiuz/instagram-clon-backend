

# rets_framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer


# Models 
from .models import Followers
from accounts.models import User

class FollowerSerailizer(serializers.Serializer):
    
    token = serializers.CharField(required=True)     #Yo
    following = serializers.CharField(required=True)


    def is_following(self,userFollower,userFollowing) -> bool:
        """
          Comprueba si el usuario es seguidor o no
        """
        follow = Followers.objects.filter(
            userFollower=userFollower,
            userFollowing=userFollowing
        )
        if follow:
            return True

        return False


    def set_follow(self,data:dict) -> dict:
        token = data['token']
        nickName = data['following']
        try:
            userFollower = Token.objects.get(key=token)
            userFollowing = User.objects.get(nickName=nickName)
            
            is_follow = self.is_following(
                userFollower=userFollower.user,
                userFollowing=userFollowing
            )

            if is_follow:
                result = self.del_follow(
                    userFollower=userFollower.user,
                    userFollowing=userFollowing
                )
                return result

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

    def del_follow(self,userFollower,userFollowing):
        result = Followers.objects.filter(
            userFollower=userFollower,
            userFollowing=userFollowing
        )
        if result:
            result[0].delete()

        return ({
            'status':'ok',
            'messge':'Ya no estas siguiendo a {name}'.format(name=userFollowing.nickName)
        })


class ListFollowersSerailzier(serializers.Serializer):

    token = serializers.CharField(required=True)

    def get_follower_list(self,data) -> list:
        """ 
          Retorna una lista con todos los usuarios
          que esta siguiendo
        """
        token = data['token']
        try:
            user = Token.objects.get(key=token)
            followList=[]
            followingList = Followers.objects.filter(userFollower=user.user)
            for item in followingList:
                followList.append(item.userFollowing.nickName)

            return followList

        except Exception as e:
            print(e)
            return []