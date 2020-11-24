
""" serialization of models """
from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Message

class SerializerUser(serializers.ModelSerializer):
    """ serialization of User """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        field = ['username', 'password']


class SerializerMessage(serializers.ModelSerializer):
    """ serialization of Message """

    id = serializers.ReadOnlyField(required=False)
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    delete = serializers.BooleanField(required=False)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'message', 'delete']
