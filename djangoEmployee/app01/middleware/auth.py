from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

class AuthMiddleware(MiddlewareMixin):

    # 读取当前访问的用户session信息
    def process_request(self, request):
        # .path_info作用：获取用户当前访问的url【纯路由地址】
        path = request.path_info
        if path.startswith('/admin/'):
            return redirect('/myadmin/list/')

        if request.path_info in ['/login/', '/image/code/']:
            return None

        info_dict = request.session.get('info')
        print(info_dict)
        if info_dict:
            return None
    # 如果没有登录过，返回登录页面
        return redirect('/login/')
    
def process_response(self, request, response):
        return response