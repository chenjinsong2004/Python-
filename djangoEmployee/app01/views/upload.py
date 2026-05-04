from django.shortcuts import render, redirect
from app01 import models
from django.http import HttpResponse
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django import forms
import os
from django.conf import settings

def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')
    # print(request.POST)
    # print(request.FILES)
    file_object = request.FILES.get("avatar")
    print(file_object.name)

    with open(file_object.name, "wb") as f:
        for chunk in file_object.chunks():
            f.write(chunk)
    return HttpResponse("成功操作")

class UpForm(BootStrapForm):
    bootstrap_fields = ['img']
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")
    

def upload_form(request):
    title = "form上传"
    form = UpForm()
    if request.method == "GET":
        return render(request, 'upload_form.html', {"form":form, "title":title})
    
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        image_object = form.cleaned_data.get('img')
        

        db_file_path = os.path.join(settings.MEDIA_ROOT, image_object.name)
        file_path = os.path.join("app01", db_file_path)

        if not models.Boss.objects.filter(img=db_file_path).exists():
            with open(file_path, "wb") as f:
                for chunk in image_object.chunks():
                    f.write(chunk)

        # 将数据文件写入数据库
        if not models.Boss.objects.filter(img=db_file_path).exists():
            models.Boss.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                img=db_file_path,
            )
            return HttpResponse("添加成功")
        return HttpResponse("图片重复")
    return render(request, 'upload_form.html', {"form":form, "title":title})

class UpModelForm(BootStrapModelForm):
    class Meta:
        model = models.city
        fields = "__all__"

def upload_modalform(request):
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form":form, "title":'ModelForm上传文件'})
    
    form=UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        image_obj = form.cleaned_data.get('img')
        if not models.city.objects.filter(img=image_obj.name).exists():
            form.save()
            return HttpResponse("成功添加")
        else:
            return HttpResponse("图片已经存在")
    return render(request, 'upload_form.html', {"form":form, "title":'ModelForm上传文件'})