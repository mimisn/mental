import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from assetManagement import models

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class CproomForm(forms.Form):
    name = fields.CharField(max_length=128, required=True, error_messages={'required': u'机房名字不能为空'})
    describe = fields.CharField(max_length=256, required=False)
    address = fields.CharField(max_length=128, required=True, error_messages={'required': u'机房地址不能为空'})
    contacts = fields.CharField(max_length=24, required=False)
    telephone = fields.CharField(max_length=11, required=False, validators=[mobile_validate, ])

class HostInfoForm(forms.Form):
    ip = fields.CharField(max_length=64, required=True,
                          error_messages={'required': u'IP不能为空'},
                          widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleIP'}))
    port = fields.CharField(max_length=8,
                            initial="5100",
                            widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'examplePort'}))
    msg = fields.CharField(max_length=64,
                           required=False,
                           widget=widgets.Textarea(attrs={'class': 'form-control', 'id': 'exampleMsg'}))
    hostname = fields.CharField(max_length=64,
                                required=False,
                                widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleHostname'}))
    in_ip = fields.CharField(max_length=64,
                             required=False,
                             widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleInIp'}))
    os_type = fields.CharField(max_length=64,
                               required=False,
                               widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleOsType'}))
    os_version = fields.CharField(max_length=64,
                                  required=False,
                                  widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleOsVersion'}))
    mem_total = fields.CharField(max_length=64,
                                 required=False,
                                 widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleMemTotal'}))
    mem_swap = fields.CharField(max_length=32,
                                required=False,
                                initial="0",
                                widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleMemSwap'}))
    cpu_type = fields.CharField(max_length=64,
                                required=False,
                                widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleCpuType'}))
    cpu_num = fields.CharField(max_length=16,
                               required=False,
                               widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleCpuMum'}))
    disk_info = fields.CharField(max_length=512,
                                 required=False,
                                 widget=widgets.TextInput(attrs={'class': 'form-control','id':'exampleDiskInfo'}))
    kernel = fields.CharField(max_length=64,
                              required=False,
                              widget=widgets.TextInput(attrs={'class': 'form-control','id':'exampleKernel'}))
    status = fields.CharField(max_length=16,
                              required=False,
                              widget=widgets.TextInput(attrs={'class': 'form-control', 'id': 'exampleStatus'}))
    room_id = fields.IntegerField(widget=widgets.Select(attrs={'class': 'form-control', 'id': 'exampleRoom'}))

    def __init__(self, *args, **kwargs):
        super(HostInfoForm, self).__init__(*args, **kwargs)
        self.fields['room_id'].widget.choices = models.Cproom.objects.values_list('id', 'name')



