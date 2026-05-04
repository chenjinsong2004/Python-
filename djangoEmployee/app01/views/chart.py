from django.shortcuts import render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from datetime import datetime
from app01.utils.pagination import Pagination

def chart_list(request):
    
    return render(request, 'chart_list.html')

def chart_bar(request):
    # 构造柱状图的数据
    legend = ['蜡笔小新','张三']

    series_list = [
                {
                    'name': '蜡笔小新',
                    'type': 'bar',
                    'data': [5, 20, 36, 10, 10, 20]
                },
                {
                    'name': '张三',
                    'type': 'bar',
                    'data': [8, 17, 30, 16, 15, 15]
                },
            ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月'] 

    result = {
        "status": True,
        "data":{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis
        }
    }
    return JsonResponse(result)

def chart_pie(request):
    db_data_list = [
                        { 'value': 999, 'name': 'IT部门' },
                        { 'value': 735, 'name': '运营' },
                        { 'value': 580, 'name': '新媒体' },
                        { 'value': 484, 'name': '策划' },
                        { 'value': 300, 'name': '人事部' }
                    ]
    result = {
        "status":True,
        "data":db_data_list
    }
    return JsonResponse(result)

def chart_line(request):
    legend = ['深圳','广东']

    series_list = [
                {
                    'name': '深圳',
                    'type': 'line',
                    'stack': 'Total',
                    'data': [5, 20, 36, 10, 10, 20]
                },
                {
                    'name': '广东',
                    'type': 'line',
                    'stack': 'Total',
                    'data': [8, 17, 30, 16, 15, 15]
                },
            ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月'] 

    result = {
        "status": True,
        "data":{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis
        }
    }
    return JsonResponse(result)