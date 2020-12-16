
# rest_framework
from rest_framework import serializers


class PostSerailizer(serializers.Serializer):


    id = serializers.CharField(required=True)
    text = serializers.CharField(required=True)
    user = serializers.CharField(required=True)
    hashTags = serializers.CharField(required=True)







