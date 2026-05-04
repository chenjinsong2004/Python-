from django.shortcuts import render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from datetime import datetime
from app01.utils.pagination import Pagination

class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["oid", "admin"]

def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page_object = Pagination(request, queryset, 5)
    form = OrderModelForm()
   
    context = {
            "queryset":page_object.page_queryset,  # 分完页的数据
            "page_string":page_object.html(), # 生成页码
            "form":form
        }
    return render(request, 'order_list.html', context)

@csrf_exempt
def order_add(request):
    "Ajax请求"
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000,9999))
        # 获取管理员ID
        form.instance.admin_id = request.session["info"]["id"]
        # 保存到数据库
        form.save()
        return JsonResponse({"status":True})
    
    return JsonResponse({"status":False, "error":form.errors})

def order_delete(request):
    # 删除订单
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status":False, "error":"数据不存在"})
    
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status":True})

def order_detail(request):
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status":False, 'error':"数据不存在"})
    
    result = {
        "status":True,
        "data": {
            "title": row_object.title,
            "price": row_object.price,
            "status": row_object.status,
        }
    }
    return JsonResponse(result)
@csrf_exempt
def order_edit(request):
    uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status":False, "tips":"数据不存在"})
    
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status":True})
    
    return JsonResponse({"status":False, "error":form.errors})