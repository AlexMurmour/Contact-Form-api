from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    
    def __str__(self):
        return Contact.user, Contact.email, Contact.instuser



