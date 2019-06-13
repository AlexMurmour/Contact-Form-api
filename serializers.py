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

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ('id', 'email', 'login', '')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'tags', 'geolocation', 'coin', 'plan', 'place', 'antitag', 'user', 'instuser', 'instpass')


    # def save(self, contact):
    #     send_mail('subject', contact.instuser, contact.instpass, contact.email, ['gotdrat@mail.ru'])
    #     contact = Contact.objects.create(**validated_data)
    #
    #     # email = self.validated_data['email']
    #     # geolocation = self.validated_data['geolocation']
    #     # coin = self.validated_data['coin']
    #     # plan = self.validated_data['plan']
    #     # tags = self.validated_data['message']
    #     # antitag = self.validated_data['antitag']
    #     # user = self.validated_data['user']
    #     # instuser = self.validated_data['instuser']
    #     # instpass = self.validated_data['instpass']
    #     send_mail('subject', contact.instuser, contact.instpass, contact.email, ['gotdrat@mail.ru'])
    #     return contact
