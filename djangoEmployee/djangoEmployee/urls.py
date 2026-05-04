"""
URL configuration for djangoEmployee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import views, account, task, order, chart, upload
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name="media"),
    # 部门管理
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('depart/multi/', views.depart_multi),

    # 用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/model/add', views.user_model_form_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),

    # 靓号列表
    path('pretty/list/', views.pretty_list),
    path('pretty/add/', views.pretty_add),
    path('pretty/<int:nid>/edit/', views.pretty_edit),
    path('pretty/<int:nid>/delete/', views.pretty_delete),
    
    # 管理员列表
    path('myadmin/list/', views.admin_list),
    path('myadmin/add/', views.admin_add),
    path('myadmin/<int:nid>/edit/', views.admin_edit),
    path('myadmin/<int:nid>/delete/', views.delete_edit),
    path('myadmin/<int:nid>/reset/', views.admin_reset),

    # 登录
    path('login/', account.login),
    path('logut/', account.logut),
    path('image/code/', account.image_code),

    # 任务管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),
    path('task/<int:nid>/edit/', task.task_edit),
    path('task/<int:nid>/delete/', task.task_delete),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modalform/', upload.upload_modalform),
]


