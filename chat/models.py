"""Class Message """
from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):

    """ configuration of the properties of a message """

    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1200)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    delete = models.BooleanField(default=False)
    image = models.FileField(upload_to='documents/')

