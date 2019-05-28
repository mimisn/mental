from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from assetManagement.Form import CproomForm,HostInfoForm
from assetManagement import models as assetmodels

# Create your views here.
import json

from mental.util.page import Page


class jsondata:
    result = "success"
    data = [
            {'time': '00:11:12', 'hero': '幻影刺客', 'action': '击杀', 'target': '斧王', 'desc': '幻影刺客击杀了斧王。'},
            {'time': '00:13:22', 'hero': '幻影刺客', 'action': '购买了', 'target': '隐刀', 'desc': '幻影刺客购买了隐刀。'},
            {'time': '00:19:36', 'hero': '斧王', 'action': '购买了', 'target': '黑皇杖', 'desc': '斧王购买了黑皇杖。'},
            {'time': '00:21:43', 'hero': '力丸', 'action': '购买了', 'target': '隐刀', 'desc': '力丸购买了隐刀。'}
        ]
    message = ""
    pager = {
            "page": 1,
            "recTotal": 1001,
            "recPerPage": 10,
        }


def jsontest(request):
    data = {
        "result": "success",
        "data": [
            {'time': '00:11:12', 'hero': '幻影刺客', 'action': '击杀', 'target': '斧王', 'desc': '幻影刺客击杀了斧王。'},
            {'time': '00:13:22', 'hero': '幻影刺客', 'action': '购买了', 'target': '隐刀', 'desc': '幻影刺客购买了隐刀。'},
            {'time': '00:19:36', 'hero': '斧王', 'action': '购买了', 'target': '黑皇杖', 'desc': '斧王购买了黑皇杖。'},
            {'time': '00:21:43', 'hero': '力丸', 'action': '购买了', 'target': '隐刀', 'desc': '力丸购买了隐刀。'}
        ],
        "message": "",
        "pager": {
            "page": 1,
            "recTotal": 1001,
            "recPerPage": 10,
        }
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

def _htmPageRetrun(request):
    referer = request.META['HTTP_REFERER']
    referer_list = referer.split("?")
    referer_url = "/"
    referer_page = "page=1"
    if len(referer_list) != 0:
        referer_url = referer_list[0]
        try:
            referer_uri = referer_list[1]
        except:
            referer_uri = ""
        if len(referer_uri) != 0:
            referer_uri_list = referer_uri.split("&")
            referer_page = referer_uri_list[0]
        else:
            referer_page = "page=1"
    else:
        referer_url = "/"
    return referer_url, referer_page


@login_required
def CproomController(request):
    if request.method == 'POST':
        cproomForm = CproomForm(request.POST)
        if cproomForm.is_valid():
            try:
                assetmodels.Cproom.objects.create(**cproomForm.cleaned_data).save()
                return render(request, 'cproomForm.html', {"mgs": "添加成功!"})
            except Exception as e:
                return render(request, 'cproomForm.html', {"err": e})
        else:
            return render(request, 'cproomForm.html', {"err": cproomForm.errors.as_json()})
    else:
        cproomlist = assetmodels.Cproom.objects.get_queryset().order_by("id")
        page = request.GET.get('page', 1)
        recPerPage = request.GET.get('recPerPage', 10)
        paginator = Page(len(cproomlist), int(recPerPage), page, 1)
        contacts = cproomlist[paginator.obj_slice_start:paginator.obj_slice_end]
        #print(paginator.obj_count)
        return render(request, 'cproom.html', locals())

@login_required
@csrf_exempt
def CpFormController(request):
    if request.method == 'POST':
        action = request.POST.get("action")
        if action == "edit":
            id = request.POST.get("id")
            question = assetmodels.Cproom.objects.filter(id=id)
            #print(question)
            data = serializers.serialize("json", question)
            #return HttpResponse(json.dumps(data), content_type="application/json")
            return JsonResponse(data, safe=False)
        elif action == "dele":
            id = request.POST.get("id")
            try:
                assetmodels.Cproom.objects.filter(id=id).delete()
                return HttpResponse("数据删除成功！")
            except Exception as e:
                return HttpResponse("数据删除失败！")
        elif action == "deleAll":
            id = request.POST.get("id")
            id_list = id.split(",")
            try:
                for val in id_list:
                    if val != '':
                        assetmodels.Cproom.objects.filter(id=int(val)).delete()
            except Exception as e:
                return HttpResponse("数据删除失败！")
            return HttpResponse("数据删除成功！")
        elif action == "update":
            id = request.POST.get("id")
            cproomForm = CproomForm(request.POST)
            referer = request.META['HTTP_REFERER']
            referer_list = referer.split("?")
            referer_url = "/"
            referer_page = "page=1"
            if len(referer_list) != 0:
                referer_url = referer_list[0]
                try:
                    referer_uri = referer_list[1]
                except:
                    referer_uri = ""
                if len(referer_uri) != 0:
                    referer_uri_list = referer_uri.split("&")
                    referer_page = referer_uri_list[0]
                else:
                    referer_page = "page=1"
            else:
                referer_url = "/"
            if cproomForm.is_valid() and cproomForm.has_changed():
                try:
                    assetmodels.Cproom.objects.filter(id=id).update(**cproomForm.cleaned_data)
                    return redirect("%s?%s" % (referer_url, referer_page))
                except Exception as e:
                    return redirect("%s?%s&error_message=%s" % (referer_url, referer_page, e))
            else:
                return redirect("%s?%s&error_message=%s" % (referer_url, referer_page, cproomForm.errors.as_json()))
        else:
            return HttpResponse("参数错误！")
    else:
        return render(request, 'cproomForm.html')



@login_required
def HostInfoController(request):
    if request.method == 'POST':
        hostinfoform = HostInfoForm(request.POST)
        if hostinfoform.is_valid():
            try:
                assetmodels.HostInfo.objects.create(**hostinfoform.cleaned_data).save()
                return render(request, 'HostInfoForm.html', {"mgs": "添加成功!", 'hostinfoform': hostinfoform })
            except Exception as e:
                return render(request, 'HostInfoForm.html', {"err": e, 'hostinfoform': hostinfoform})
        else:
            return render(request, 'HostInfoForm.html', {"err": hostinfoform.errors.as_json(), 'hostinfoform': hostinfoform})
    else:
        host_info_list = assetmodels.HostInfo.objects.get_queryset().order_by("id")
        page = request.GET.get('page', 1)
        recPerPage = request.GET.get('recPerPage', 10)
        paginator = Page(len(host_info_list), int(recPerPage), page, 1)
        contacts = host_info_list[paginator.obj_slice_start:paginator.obj_slice_end]
        #print(paginator.obj_count)
        return render(request, 'HostInfo.html', locals())


@login_required
@csrf_exempt
def HostinfoFormController(request):
    if request.method == 'POST':
        action = request.POST.get("action")
        id = request.POST.get("id")
        if action == "edit":
            question = assetmodels.HostInfo.objects.filter(id=id)
            cproom_list = assetmodels.Cproom.objects.all()
            data = {}
            data['question'] = serializers.serialize("json", question)
            data['cproom_list'] = serializers.serialize("json", cproom_list)
            data['active'] = question.values('room_id')[0]['room_id']
            return JsonResponse(data, safe=False)
        elif action =='update':
            hostinfoform = HostInfoForm(request.POST)
            referer_url, referer_page = _htmPageRetrun(request)
            if hostinfoform.is_valid() and hostinfoform.has_changed():
                try:
                    assetmodels.HostInfo.objects.filter(id=id).update(**hostinfoform.cleaned_data)
                    return redirect("%s?%s" % (referer_url, referer_page))
                except Exception as e:
                    return redirect("%s?%s&error_message=%s" % (referer_url, referer_page, e))
            else:
                return redirect("%s?%s&error_message=%s" % (referer_url, referer_page, hostinfoform.errors.as_json()))
        elif action == 'dele':
            try:
                assetmodels.HostInfo.objects.filter(id=id).delete()
                return HttpResponse("数据删除成功！")
            except Exception as e:
                return HttpResponse("数据删除失败！")
        elif action == 'deleAll':
            id_list = id.split(",")
            try:
                for val in id_list:
                    if val != '':
                        assetmodels.HostInfo.objects.filter(id=int(val)).delete()
            except Exception as e:
                return HttpResponse("数据删除失败！")
            return HttpResponse("数据删除成功！")
        else:
            return HttpResponse("参数错误！")
    else:
        hostinfoform = HostInfoForm()
        return render(request, 'HostInfoForm.html', locals())



@login_required
def HostGroupController(request):
    if request.method == 'POST':
        pass
    else:
        pass

@login_required
def ApplicationController(request):
    if request.method == 'POST':
        pass
    else:
        pass
