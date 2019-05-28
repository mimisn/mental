import threading

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
import time
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from assetManagement.models import HostInfo
from mental.util.page import Page




from django.contrib.auth.models import User
from multiprocessing import Process
import os

from sysManagement import models

# 权限控制装饰器
def Perms_required(func):
    def wrapper(request, *args, **kwargs):
        return func(request, *args, **kwargs)
    return wrapper


@csrf_exempt
def Login(request):
    msg = 'login'
    if request.method == 'POST':
        login_username = request.POST.get('username')
        login_passwd = request.POST.get('password')
        user = authenticate(username=login_username, password=login_passwd)
        if user:
            login(request, user)
            user = models.User.objects.get(username=login_username)
            models.UserInfo.objects.update(user_id=user.id, status="在线")
            request.session['username'] = login_username
            return redirect('/')
        else:
            msg = "用户名或密码不正确"
            return render(request, "login/login.html", locals())
    else:
        return render(request, "login/login.html", locals())


def Logout(request):
    user = models.User.objects.get(username=request.session.get("username"))
    models.UserInfo.objects.update(user_id=user.id, status="离线")
    logout(request)
    msg = 'login'
    request.session.delete("username")
    return render(request, "login/login.html", locals())

@login_required
def index(request):
    user = models.User.objects.get(username=request.session.get("username"))
    userinfo = models.UserInfo.objects.get(user_id=user.id)
    data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return render(request, 'index/index.html', locals())

# ========================HOST=============================
