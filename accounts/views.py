

# Django
from django.contrib.auth.hashers import check_password


# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import sta


# Serailizers
from .serializers import AuthSerailizer


# Models
from .models import User


@api_view(['GET','POST'])
def auth(request) -> Response:
    serailizerAuth = AuthSerailizer(data=request.data)
    serailizerAuth.is_valid(raise_exception=True)
    
    userObject = User.objects.filter(email=serailizerAuth.data['email'])
    if userObject:

        is_password = check_password(serailizerAuth.data['password'] , userObject[0].password)
        if is_password:
            userToke = Token.objects.get_or_create(user=userObject[0])
            return Response(userToke[0].key)
        else:
            return Response(
                'type-error':'password-error',
                'messege':'La contraseña no es correcta'
            )
    else:
        return Response(
            'type-error':'email-error',
            'messege':'La direccion de correo no existe'
        )






