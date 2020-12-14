

# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


# Serailizers
from .serializers import (
    AuthSerailizer,
    RegisterSerializer,
    AuthSocialSerializer
)


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
    authresponse = serailizerAuth.authenticate(data=serailizerAuth.data)
    return Response(authresponse)



@api_view(['GET','POST'])
def register(request) -> Response:
    """
      Esta funcion se encarga de registrar
      a los usuarios
    """
    regSerializer = RegisterSerializer(data=request.data)
    regSerializer.is_valid(raise_exception=True)
    responseUserData = regSerializer.create_user(valid_data=regSerializer.data)
    return Response(responseUserData)



