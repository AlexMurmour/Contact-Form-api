from django.contrib.auth.models import User
from rest_framework import serializers
from back.api.models import Contact

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'text',  'user')


   
