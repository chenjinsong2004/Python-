from django.shortcuts import render, redirect
from app01 import models
from django import forms
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from django.http import HttpResponse
from app01.utils.yzm import generate_random_captcha, generate_complex_captcha
from captcha.image import ImageCaptcha
from io import BytesIO

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput,
        required=True,
        )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput,
        required=True,
        )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput,
        required=True,
        )
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ['username', 'password']

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 拿用户输入
        user_input = form.cleaned_data.get('code')

        # 拿真实验证码
        real_captcha = request.session.get("captcha", "")
        if user_input.upper() != real_captcha.upper():
            form.add_error('code', "验证码错误")
            return render(request, 'login.html', {'form':form})

        # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password']).first()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        admin_object = models.Admin.objects.filter(username=username, password=password).first()
        if not admin_object:
            form.add_error("password", '用户名或密码错误')
            return render(request, 'login.html', {'form':form})
        
        request.session['info'] = {'id':admin_object.id, 'name':admin_object.username}
        request.session.set_expiry(60*60*24*7)
        return redirect("/admin/list/")
    return render(request, 'login.html', {'form':form})

def logut(request):
    request.session.clear()

    return redirect('/login/')

def image_code(request):
    # 生成验证码
    captcha_code = generate_random_captcha()
    # 存session（统一小写校验，防大小写问题）
    request.session['captcha'] = captcha_code.lower()

    # 生成复杂验证码图片
    img = generate_complex_captcha(captcha_code)

    # 内存输出 不存本地
    buf = BytesIO()
    img.save(buf, 'PNG')

    return HttpResponse(buf.getvalue(), content_type='image/png')