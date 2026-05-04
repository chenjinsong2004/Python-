from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from app01.utils.bootstrap import BootStrapModelForm
from app01 import models
from django.core.exceptions import ValidationError
from app01.utils.encrypt import md5
# 用户 ModelForm 表单类
class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "age", "account", "gender", "depart"]
# 手机号填写
class PrettyModelForm(BootStrapModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[
            RegexValidator(r'^1[3-9]\d{9}$', "请输入正确的11位手机号")
        ]
    )
    class Meta:
        model = models.MobileInfo
        fields = "__all__"
# 手机号修改
class PrettyEditModelForm(forms.ModelForm):
    class Meta:
        model = models.MobileInfo
        fields = ["price", "level", "status"]
# 管理员
class AdminModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="确认密码", 
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password":forms.PasswordInput
        }
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
    
    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm

class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']

class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码", 
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password":forms.PasswordInput
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        # 用修复后的md5函数，对比旧密码
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5(pwd)).exists()
        if exists:
            raise ValidationError("密码不能一致")
        return md5(pwd)  # 加密后返回

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")  # 已经是加密后的密码
        confirm = md5(self.cleaned_data.get("confirm_password"))  # 加密确认密码
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm