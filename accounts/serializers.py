# Django
from django.contrib.auth.hashers import check_password


# Rest_framework 
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Models 
from .models import User


class AuthSerailizer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def authenticate(self,data:dict) -> dict:
        email = data['email']
        password = data['password']

        user = User.objects.filter(email=email)
        if user:
            is_password = check_password(password , user[0].password)
            if is_password:
                token = Token.objects.get_or_create(user=user[0])
                return ({
                    'statis':'ok',
                    'id':token[0].user.id,
                    'user':token[0].user.name,
                    'token':token[0].key
                })
            
            else:
                return ({
                    'type-error':'password-error',
                    'messege':'La contraseña no es correcta'
                })

        else:
            return ({
                'type-error':'email-error',
                'messege':'El correo no existe'
            })




class RegisterSerializer(serializers.Serializer):

    name = serializers.CharField(required=True,max_length=50)
    nickName = serializers.CharField(required=True,max_length=50)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True , max_length=50)

    def create_user(self , valid_data:dict) -> dict:
        try:
            user = User.objects.create_user(
                name=valid_data['name'],
                email=valid_data['email'],
                password=valid_data['password'],
                nickName=valid_data['nickName']
            )

            data = { 
                'email':user.email,
                'password':valid_data['password']
            }

            auth = AuthSerailizer(data=data)
            auth.is_valid(raise_exception=True)
            return auth.authenticate(auth.data)

        except Exception as e:
            return ({
                'type-error':str(e).lower().replace(' ' , '-'),
                'messege':'Error al registrar el usuario'
            })

