from django.db import models

# Create your models here.

# 类名代表数据库中的表名，类下面的字段名代表数据库中的列名
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    size = models.IntegerField(default=2)
    data = models.IntegerField(null=True, blank=True)

class Department(models.Model):
    title = models.CharField(max_length=16)


# ----------新建数据--------------
# insert into app01_department(title) values("销售部")
# Department.objects.create(title="销售部")

# UserInfo.objects.create(name="蜡笔小新", password="123", age=5)


"""
create table app01_userinfo(
    name varchar(32),
    password varchar(64),
    age int
)
"""