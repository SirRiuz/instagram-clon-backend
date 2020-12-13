

# Rest_framework 
from rest_framework import serializers


# Models 
from .models import User


class AuthSerailizer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)



class RegisterSerializer(serializers.Serializer):

    name = serializers.CharField(required=True,max_length=50)
    nickName = serializers.CharField(required=True,max_length=50)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True , max_length=50)

    def create_user(self , valid_data:dict) -> User:
        try:
            user = User.objects.create_user(
                name=valid_data['name'],
                email=valid_data['email'],
                password=valid_data['password'],
                nickName=valid_data['nickName']
            )
            return user
        except Exception as e:
            return ({
                'type-error':str(e).lower().replace(' ' , '-'),
                'messege':'Error al registrar el usuario'
            })
