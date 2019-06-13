from django.contrib.auth.models import User
from rest_framework import viewsets, status
from back.api.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from back.api.models import Contact
from back.api.serializers import ContactSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics


class Allowuser(BasePermission):
    def get_permission(self, request, view):
        if request.method=="POST":
            return True
        elif request.user == IsAdminUser:
            return True
        else:
            return super(Allowuser, self).get_permission(request.user)




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (Allowuser, )
    def get_queryset(self):
        username = self.request.user
        if username is not None:
            if username.is_superuser:
                return User.objects.all()
            return get_object_or_404(User, username=self.request.user)
        else:
            return None



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many= False)
        return Response({'token':token.key, 'user':serializer.data})



class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Contact.objects.all()
        else:
            queryset = Contact.objects.all().filter(user=self.request.user)
            return queryset

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            response = super(ContactView, self).create(request, *args, **kwargs)
            subject = "new contact"
            email = request.POST.get("email")
            text = request.POST.get("text")
            user = request.POST.get("user")
            message = "You have a message from user {0} with email {1}: {2}".format(user, email, text)

            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, ['example@gmail.com'], fail_silently=False,)
            return response






