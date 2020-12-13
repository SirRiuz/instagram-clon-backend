

# Django
from django.contrib.auth.hashers import check_password


# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


# Serailizers
from .serializers import (AuthSerailizer,RegisterSerializer)


# Models
from .models import User


@api_view(['GET','POST'])
def auth(request) -> Response:
    """ 
        Esta funcion se encarga de hacer 
        el proceso de autenticacion y devolver
        un token al usuario
    """
    serailizerAuth = AuthSerailizer(data=request.data)
    serailizerAuth.is_valid(raise_exception=True)
    
    userObject = User.objects.filter(email=serailizerAuth.data['email'])
    if userObject:

        is_password = check_password(serailizerAuth.data['password'] , userObject[0].password)
        if is_password:
            userToke = Token.objects.get_or_create(user=userObject[0])
            return Response({
                'id':userToke[0].user.id,
                'nickName':userToke[0].user.nickName,
                'email':userToke[0].user.email,
                'token':userToke[0].key
            })
        else:
            return Response({
                'type-error':'password-error',
                'messege':'La contraseña no es correcta'
            })
    else:
        return Response({
                'type-error':'email-error',
                'messege':'La direccion de correo no existe'
        })


@api_view(['GET','POST'])
def register(request) -> Response:
    """
      Esta funcion se encarga de registrar
      a los usuarios
    """
    regSerializer = RegisterSerializer(data=request.data)
    regSerializer.is_valid(raise_exception=True)
    user = regSerializer.create_user(valid_data=regSerializer.data)
    
    if type(user) == User:
        newUserToken = Token.objects.create(user=user)
        return Response({
            'status':'ok',
            'messege':'Se a registrado correctamente el usaurio : {nick}'.format(nick=newUserToken.user.nickName),
            'auth':{
                'id':newUserToken.user.id,
                'user':newUserToken.user.nickName,
                'token':newUserToken.key
            }
        })
    
    else:
        return Response(user)


