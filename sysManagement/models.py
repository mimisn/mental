from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from assetManagement.models import HostInfo


class UserInfo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=128, null=True)
    Photo = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=64, default='离线')
    def __str__(self):
        return self.username


# Create your models here.


class software(models.Model):
    host = models.ForeignKey(to=HostInfo, on_delete=models.CASCADE)
    server_name = models.CharField(max_length=256)
    server_version = models.CharField(max_length=512, null=True)
    server_port = models.CharField(max_length=1026, null=True)
    def __str__(self):
        return self.server_name