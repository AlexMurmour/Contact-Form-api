from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    tags = models.TextField()
    geolocation = models.TextField()
    coin = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    place = models.CharField(max_length=80)
    antitag = models.TextField()
    instuser = models.CharField(max_length=30)
    instpass = models.CharField(max_length=30)
    # time = models.DateTimeField(auto_now=True, blank=true)
    # confirm = models.BooleanField(default=False)

    # def numcontact(self):
    #     all_ratings = Contact.object.filter(id(User))
    #     return all_ratings
    def __str__(self):
        return Contact.user, Contact.email, Contact.instuser



