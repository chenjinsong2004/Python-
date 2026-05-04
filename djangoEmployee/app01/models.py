from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=32)

    def __str__(self):
        return self.username

class Department(models.Model):
    # 部门表
    id = models.BigAutoField(verbose_name='ID', primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32)
    # 新增这个方法，控制对象的展示文本
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    # 部门表
    name = models.CharField(verbose_name='名字', max_length=16)
    # password = models.CharField(verbose_name='密码', max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="工资", max_digits=10, decimal_places=2)
    create_time = models.DateField(verbose_name="入职时间")
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # 参数1：关联的模型名
    # 参数2：关联模型的字段名
    # 参数3：数据库层面允许空值
    # 参数4：表单/Admin后台层面允许空值
    # 参数5：关联数据删除时的行为

    gender_choice = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choice)

class MobileInfo(models.Model):
    mobile = models.CharField(verbose_name='号码', max_length=16)
    price = models.IntegerField(verbose_name="价格")
    
    level_choice = (
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4,'4级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choice,default=1)

    status_choices = (
        (1,'已占用'),
        (2,'未占用')
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices, default=2)

class Task(models.Model):
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)

class Order(models.Model):
    # 订单
    oid  = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    statue_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=statue_choices, default=1)
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)

class Boss(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄", max_length=32)
    img = models.FileField(verbose_name="文件", max_length=128)

class city(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    count = models.IntegerField(verbose_name="人口", max_length=32)
    img = models.FileField(verbose_name="Logo", max_length=128)