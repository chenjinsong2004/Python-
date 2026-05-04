from django.shortcuts import render, redirect
from app01 import models
from django import forms
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app01.utils.pagination import Pagination

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            'detail': forms.TextInput
        }

def task_list(request):
    queryset = models.Task.objects.all().order_by('id')
    page_object = Pagination(request, queryset)
    form = TaskModelForm()
    content = {
        "form":form,
        "queryset":page_object.page_queryset,  # 分完页的数据
        "page_string":page_object.html(), # 生成页码
    }
    return render(request, 'task_list.html', content)

def task_edit(request):
    pass

def task_delete(request, nid):
    models.Task.objects.filter(id=nid).delete()
    return redirect('/task/list/')

@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    data_dict = {'statue': True, 'data': [11, 22, 33, 44]}
    # 把字典转成 JSON 字符串
    json_string = json.dumps(data_dict)
    return HttpResponse(json_string)

@csrf_exempt
def task_add(request):
    # <QueryDict: {'level': ['1'], 'title': ['1'], 'detail': ['2'], 'user': ['3']}>
    print(request.POST)

    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    
    data_dict = {"statue":False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))

