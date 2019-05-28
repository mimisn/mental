from django.db import models


# Create your models here.
#ji fang
import sysManagement.models as sysManage


class Cproom(models.Model):
    name = models.CharField(max_length=128, null=True)
    describe = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=128, null=True)
    contacts = models.CharField(max_length=24, null=True)
    telephone = models.CharField(max_length=11, null=True)
    def __str__(self):
        return self.name



class HostInfo(models.Model):
    ip = models.CharField(max_length=64, unique=True) #可关闭唯一性索引
    port = models.CharField(max_length=8, default="5100")
    msg = models.CharField(max_length=64, null=True)
    hostname = models.CharField(max_length=64, null=True)
    in_ip = models.CharField(max_length=64, null=True)
    os_type = models.CharField(max_length=64, null=True)
    os_version = models.CharField(max_length=64, null=True)
    mem_total = models.CharField(max_length=64, null=True)
    mem_swap = models.CharField(max_length=32, default="0")
    cpu_type = models.CharField(max_length=64, null=True)
    cpu_num = models.CharField(max_length=16, null=True)
    disk_info = models.CharField(max_length=512, null=True)
    kernel = models.CharField(max_length=64, null=True)
    status = models.CharField(max_length=16, null=True)
    addTime = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(to=Cproom, on_delete=models.CASCADE)
    def __str__(self):
        return self.ip

#zhu ji zu
class HostGroup(models.Model):
    name = models.CharField(max_length=128, null=True)
    describe = models.CharField(max_length=256, null=True)
    def __str__(self):
        return self.name

#zhu ji yu zhu ji zu guan xi ying se biao
class HostGroupRel(models.Model):
    host1 = models.ForeignKey(to=HostInfo, on_delete=models.CASCADE, related_name='host')
    hostgroup = models.ForeignKey(to=HostGroup, on_delete=models.CASCADE, related_name='hostgroup')


