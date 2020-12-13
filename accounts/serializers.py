

# Rest_framework 
from rest_framework import serializers


class AuthSerailizer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)