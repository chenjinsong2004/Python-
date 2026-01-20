# 第一章 Python入门



## 1. 笔记的使用

- 标题 # 空格
- 列表 - 空格  1.空格  tab  shift+tab
- 代码 ```
- 图片
- 引用

## 2. 环境的搭建

- 因为电脑只能识别：010101
- 所以需要语法解释器（类似于翻译官）

- 下载python3.6以上的版本

- 最常用的IDE就是：Pycharm

### 2.1 安装目录

我的目录为：C:\python

```
	c:\python
		- pyython.exe(解释器)
		- Scripts
			- pip.exe(帮助我们安装第三方的包)
        - Lib
        	- 文件/文件夹(python提供的内置功能)
        	- site-packages(通过pip去安装第三方的包时，会在这个目录)
```

### 2.2 path环境的设置

此电脑 -> 属性 -> 高级设置 -> path环境设置

# Python语法 

python 3.xx 版本默认使用的是UTF-8编码器

## 1 数据类型

- **整形**：100、200
- **字符串**(str)  :  "中国联通"
- **列表**(list)      :  [11,22,33]
  - append/insert/remove/pop/clear/sort

- **元组**(tuple)  :  (11,22,33)
- **字典**(dict)     :  {''k1'':123, "k2":456}
  - **独有功能**      :  upper/lower/isdecimal/strip/replace/join/split/center/zfill

```python
n1 = "root"
res = n1.upper()            # res = "ROOT"

n2 = "admin"
value = n2.upper()          # value = "VALUE"

data_list1 = [11,22,33,44]
data_list1.append(55)       # 列表的功能，在尾部最加某个值

# 独有功能&公共功能
```



- **字符型**："哈哈"、’字符型要加**引号**‘    一个成对的引号只能单行输入，多行输入需要用"""    """ 

  字符串可以相加，可以和数字相乘

  ```python
  "哈哈" * 3
  "哈哈" + "哈哈"
  
  """用于多行输入输出"""
  
  print(12 + 12)     # 24 整形
  
  print("12" + "12") # "1212" 字符型
  
  str(19)            # 19 -> "19" 整形变字符型
  
  int("88")          # "88" -> 88 字符型变整形
  
  # 字符串切割 ------------------------------------------------------------------------------------------------
  file_name = "day01 python基础入门.mp4"
  
  # 字符串切割后是一个列表
  # data_list = ["day01 python基础入门", "mp4"]
  data_list = file_name.split(".")
  
  data_list[0]        #"day01 python基础入门"
  data_list[1]        # "mp4"
  
  # 实例:
  data = input("请输入两个数字相加:")
  res = data.split("+")
  sum1 = res[0] + res[1]
  if sum1.isdecimal():
      sum = int(res[0]) + int(res[1])
      print(sum)
  else:
      print("输入错误")
  
  # 字符串拼接 -------------------------------------------------------------------------------------------------
  # 1.字符串相加
  v1 = "蜡笔"
  v2 = "小新"
  text = "我是" + v1 + v2
  
  # 2.字符串格式化
  v1 = "蜡笔"
  v2 = "小新"
  text = "{}是{}".format(v1,v2)
  
  # 3.将列表中字符串拼接起来
  data_list = ["算数","不会","求教"]
  res = ",".join(data_list)
  print(res)   # 算数，不会，求教
  
  
  data_list = ["算数","不会","求教"]
  res = "".join(data_list)
  print(res)   # 算数不会求教
  
  # 实例
  name_list = []
  while True:
      name_list.append(input("请输入姓名:"))
      num = input("终止请输入q/Q:")
      num = num.upper()
      if num != "Q":
          continue
      else:
          res = ",".join(name_list)
          print("最终为：" + res)
          break
          
  # 字符串转换成字节类型 -----------------------------------------------------------------------------------------
  data = "中国"
  v1 = data.encode("utf-8")
  print(v1)
  text = v1.decode("utf-8")
  print(text)
  
  # 长度补足 ---------------------------------------------------------------------------------------------------
  name = "蜡笔小新"
  text = name.center(6,"*")
  print(text)               # ***蜡笔小新***
  
  name = "蜡笔小新"
  text = name.ljust(6,"*")
  print(text)               # 蜡笔小新******
  
  name = "蜡笔小新"
  text = name.rjust(6,"*")
  print(text)               # ******蜡笔小新
  
  name = "1010"
  v1 = name.zfill(8)
  print(v1)                 # 00001010
  ```
  
  ```python
  # bool值
  # 整型中除了0，都是true
  print(bool(0))      # false
  print(bool(-1))     # true
  
  # 字符型除了空字符串，都是true
  print(bool(""))     # false
  print(bool(" "))    # true
  print(bool("哈哈"))  #true
  ```



- **变量**: 字母、数字、下划线

- 不能以数字开头，不能使用Python内置关键字

  ```python
  addr = "将这个字符串赋值给addr"
  
  print(addr)
  
  age = "5"
  name = "蜡笔小新"
  add = "动漫"
  address = age + name + add
  
  print(address)
  ```

### 1.1 字符串类型

注意：字符串是一个不可变的类型

```python
name = "蜡笔小新"
email = "xxxx@live.com"
```

 #### 1.1.1 独有功能

```python
data = "root"
res = data.功能名()    # res = 新的值
```

- 大写和小写

- ```python
  name = "root"
  res = name.upper()
  print(res)           # "ROOT"
  print(name)          # "root"
  
  # ------------------------------------
  
  name = "ROOT"
  res = name.lower()
  print(res)           # "root"
  print(name)          # "ROOT"
  ```

- isdecimal, 判断字符串里面是不是整数

```python
data = "999"
v1 = data.isdecimal()
print(v1)                # true

data2 = "aaa"
v2 = data2.isdecimal()
print(v2)                # false
```

- 关于作用域

```python
if 1 == 1:
    text = "钱"
    print(text)
print(text)      # "钱"，区别于java与c语言，python的作用域是一整块

if 1 != 1:
    text = "钱"
    print(text)
print(text)      # 报错
```

- startswith和endswith，判断字符串是以XX开头或是XX结尾

```python
name = "蜡笔小新"
v1 = name.startswith("蜡笔")  # true
v2 = name.endswith("蜡笔")    # false
```

- strip/lstrip/rstrip,去除空白

```python
name = " 台湾省 "

v1 = name.strip() # "台湾省"

v2 = name.lstrip() # "台湾省 "

v3 = name.rstrip() # " 台湾省"

# 实例1:
name = input("请输入姓名:")
data = name.strip()
if data == "":
    print("输入不能为空")
else:
    print(name)
```

- replace,替换

```python
text = "我是蜡笔小新"
data = text.replace("我是"，"你是")
print(data)             # "你是蜡笔小新"
print(text)             # "我是蜡笔小新"

# 实例1  将ls1,ls2,ls3,ls4变成***
text = input("请输入文本:")
text = text.replace("ls1","***")
text = text.replace("ls2","***")
text = text.replace("ls3","***")
data = text.replace("ls4","***")
print(data)
```



#### 1.1.2 公共功能

```python
# 1.长度-------------------------------------------------------------------------------------------------------
name = "蜡笔小新"
res = len(name)
print(res)       # 4

# 2.索引-------------------------------------------------------------------------------------------------------
text = "我爱学习python"
text[0]                # "我"
v2 = len(text)         # "10"
while v2 > 0:
    v2 -= 1
    print(text[v2])
    
# 3.切片-------------------------------------------------------------------------------------------------------
print(text[0:5])       # "我爱学习p"

num = 111
# 1.转换成二进制
bin_string = bin(num)
# 2.不要开头0b
data = bin_string[2:]
# 3.将二进制补足16位
result = data.zfill(16)

# 4.循环-------------------------------------------------------------------------------------------------------

# while 循环
data = "蜡笔小新"
index = 0
while index < len(data):
    char = data[index]
    print(char)
    index += 1
    
# for 循环
data = "蜡笔小新"
for item in data:
    print(item)
    
for item in range(len(data))
	print(item)
    
# 实例
message = "abcdefg"
for item in range(len(message)):
    num = len(message) - item - 1
    print(message[num])
    
text = "请输入asasas8as68686"
sum1 = []
for item in text:
    if item.isdecimal():
        sum1.append(item)
    else:
        continue
num_string = "".join(sum1)
num_int = int(num_string)
res = bin(num_int)
res = res[2:]
print(res)
    
# range函数的作用,帮你生成一个数字列表
v1 = range(5,10)      #5到10
v2 = range(5)         #1到5
v3 = range(5,10,2)    #5，7，9
v4 = range(10,1,-1)   #10到1

# 显示自己电脑上某个文件夹的所有文件--------------------------------------------------------------------------------
import os

data_list = os.listdir(r"C:\Program Files")
for file_name in data_list:
    print(file_name)              # 字符串
```



### 2.1 列表 （list）

列表，是一个有序且可变的容器，元素可以是不同的数据类型。

```python
# 定义 ---------------------------------------------------------------------------------------------
data_list = [11, 22, "蜡笔小新", True]

# 追加 ---------------------------------------------------------------------------------------------
data_list = []
data_list.append(11)
data_list.append("labixx")

hobby_list = []

# 案列
while True:
    hobby = input("请输入您的爱好:")
    if hobby.upper() == "Q":
    	break
    hobby_list.append(hobby)
    
# 插入 ----------------------------------------------------------------------------------------------
user_list = [33,44,55,66,77,88]
user_list.insert(0,22)
user_list.insert(0,11)

# 案列
user_list = []
while True:
    name = input("请输入姓名:")
    if name.upper() == "Q":
    	break
    if name.startswich("西"):
		user_list.insert(0,name)
    else:
        user_list.append(name)

# 删除 ------------------------------------------------------------------------------------------------
user_list = [33,44,55,66,77,88]
user_list.remove("44")
print(user_list)
# 利用remove去删除列表元素时，如果元素不存在，则会报错
if 44 in user_list:
    user_list.remove()

# 案列
import random
user_list = []
for i in range(1,200):
    name = "工号-{}".format(i)
    user_list.append(name)
data = random.choice(user_list)
print("获奖员工为: ", data)
user_list.remove(data)
data = random.choice(user_list)
print("获奖员工为: ", data)

# 删除(索引位置) ------------------------------------------------------------------------------------------
user_list = [33,44,55,66,77,88]
# 1.在源列表中删除指定索引的值
# 2.将刚刚删除的数据赋值给前面的变量
data = user_list.pop(1)
print(data)
print(user_list)

# 案列
user_queue = []
while True:
    name = input("购买火车票，输入姓名（Q/q）：")
    if name.upper() == "Q":
        break
    else:
        user_queue.append(name)
for i in range(3):
    username = user_queue.pop(0)
    message = "恭喜{}成功买到票".format(username)
    print(message)
others = ",".join(user_queue)
data = "以下人员没票: {}".format(others)
print(data)

# 清空列表 -----------------------------------------------------------------------------------------------
user_list = [33,44,55,66,77,88]
user_list.clear()
print(user_list)  # []

# 列表元素排序 --------------------------------------------------------------------------------------------
user_list = [33,66,55,44,88,77]
user_list.sort()                #从小到大
print(user_list)  

suer_list.sort(reverse = True)  # 从大到小
print(user_list)

# 长度----------------------------------------------------------------------------------------------------
user_list = [33,66,55,44,88,77]
res = len(user_list)
print(res)

# 索引 ---------------------------------------------------------------------------------------------------
user_list = [33,66,55,44,88,77]
# 获取值
user_list = [0]
user_list = [len(user_list) - 1]
# 修改值
user_list[1] == 99
print(user_list)
# 删除
del user_list[1]
print(user_list)

# 切片 ----------------------------------------------------------------------------------------------------
user_list = [33,66,55,44,88,77]
del user_list[1:4]
user_list[0:] = [11, 22, 33, 44]
print(user_list)

# for循环 -------------------------------------------------------------------------------------------------
user_list = [33,66,55,44,88,77]
for item in range(len(user_list)):
    data = "{}-{}".format(item, user_list)
    print(data)
    
# 嵌套 ----------------------------------------------------------------------------------------------------
data_list = [
    "55",
    "66",
    [77,88,99,1010],
    666,
    ["蜡笔小新"，"管制", [11, 22, 33]]
]
data_list[1]        # "66"
data_list[2][2]     #  99
data_list[4][2][2]  #  33
data_list[4][2][2] = 44 

# 案例 1.
user_list = []
while True:
    userlist = []
    user_name = input("请输入用户名：")
    if user_name.upper() == "Q":
        break
    user_pass = input("请输入密码：")
    userlist = [user_name, user_pass]
    user_list.append(userlist)
print(user_list)

# 2.
goods = [["飞机",3333],["大炮",2222],["m6",1111]]
for item in range(len(goods)):
    items = "{}-{}".format(item,goods[item][0])
    print(items)
while True:
    num = input("请输入你想买的商品序号:")
    if num.upper() == "Q":
        break
    num = int(num)
    print("你选择的商品是{},价格是{}".format(goods[num][0],goods[num][1]))
```



### 2.2 元组

列表，是一个有序且可变的容器，元素可以是不同的数据类型.

元组，是一个有序且不可变的容器，元素可以是不同的数据类型.

```python
# 元组个数不能修改；元组的元素也不可以被替换成其它的值
data = (11,22,33)
v1 = (666)         # v1 = 666
v2 = (666,)        # v2 = 元组，只有一个元素666

# 长度 ----------------------------------------------------------------------------------------------------
data = (11,22,33)
res = len(data)

# 索引 ----------------------------------------------------------------------------------------------------
data = (11,22,33)
data[-1]

#切片 -----------------------------------------------------------------------------------------------------
data = (11,22,33)
Data = data[0:1]

# for循环 -------------------------------------------------------------------------------------------------
data = (11,22,33)
for i in range(len(data)):
    print(i)
    
# 嵌套 ----------------------------------------------------------------------------------------------------
#元素不可变，元素个数也不可变
data = (
    11,
    22,
    (33,44,55)
)
data[2][1] = 77  # 可以改变

# 例题
color_list = ["红桃","黑桃","方块","梅花"]
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
result = []
for color in color_list:
    for num in num_list:
        text = (color,num)
        result.append(text)
print(result)
```



### 2.3 字典

字典是一个无序，键不重复且元素只能是键值对的可变的容器

```python
info = {"k1":123, "k2":999}

# 键不能重复，重复时数据会覆盖 -------------------------------------------------------------------------------
info = {"k1":123, "k1":333}
print(info)                   # {"k1":333}

# 键必须是可哈希的类型: int  bool  str  tuple
# 不可哈希          : 列表  字典
v1 = 123
v2 = [1,2,3]              # 不可哈希
res = hash(v2)
print(res)                # 报错

# 定义 ---------------------------------------------------------------------------------------------------
info = {
    "name":"蜡笔小新",
    "age":5,
    "hobby":"动漫"
}
```

#### 2.3.1 独有功能

```python
#1.获取值 ----------------------------------------------------------------------------------
info = {
    "name":"蜡笔小新",
    "age":5,
    "hobby":["动漫","篮球"]
}
v1 = info.get("name")
print(v1)                      # "蜡笔小新"

v2 = info.get("email", "xxx")  #当键不存在时， v3 = "xxx"
print(v2)                      # "xxx"

# 案例
user_dict = {
    "zhansan":"333",
    "lishi":"444",
    "wangwu":"555"
}
user = input("请输入用户名:")
pwd = input("请输入密码:")

# 键不存在 则db_password = None
# 键存在  则db_password = 密码
db_password = user_dict.get(user)
if db_password == None:
    print("用户不存在")
else:
    if db_password == pwd:
        print("登入成功")
    else:
        print("登入失败")
        
# 键 ---------------------------------------------------------------------------------------
info = {
    "name":"蜡笔小新",
    "age":5,
    "hobby":["动漫","篮球"]
}
for item in info.keys():               # 获取所有的键 keys()
    print(item)

for item in info.values():             # 获取所有的值 values()
    print(item)

for item in info.items():
    print(item)                        # 获取所有的键,所有的值 items()

for key,value in info.items():         # 获取所有的键,所有的值
    print(key,value)
```



#### 2.3.2 公共功能

```python
# 1.长度 ---------------------------------------------------------------------------------------
info = {
    "name":"蜡笔小新",
    "age":5,
    "hobby":["动漫","篮球"]
}
data = len(info)
print(data)         # 3

# 2.索引取值 ------------------------------------------------------------------------------------
info = {
    "name":"蜡笔小新",
    "age":5,
    "hobby":["动漫","篮球"]
}
v1 = info.get("name")
v2 = info.get("email")
print(v1,v2)               # "蜡笔小新" None

# 3.新增、删除与修改-----------------------------------------------------------------------------------
info = {
    "name":"蜡笔小新",
    "age":5,
    "hobby":["动漫","篮球"]
}
info["email"] = "2438012849@qq.com"
for item in info.items():
    print(item)            
# 如果存在则删除
if "email" in info:
    del info["email"]
    
# 嵌套 -----------------------------------------------------------------------------------------
info = {
    "k1":123,
    "k2":(1,2,3),
    "k3":[1,2,3],
    "k4":[1,2,3,{"v1":123,"v2":456}]
}
# 例题 -----------------------------------------------------------------------------------------
info = {}

while True:
    text = input(">>>")
    if text.upper() == "Q":
        break
    text_keys = text.split(",")
    info[text_keys[0]] = text_keys[1]

for item in info.items():
    print(item)
    
#例题：
goods = [
    {"name":"电脑","price":1999},
    {"name":"模型","price":10},
    {"name":"鼠标","price":29},
    {"name":"键盘","price":999}
]
for item in range(len(goods)):
    goods_list1 = goods[item].get("name")
    goods_list2 = goods[item].get("price")
    print(item+1,goods_list1,goods_list2)

while True:
    goods_num = input("请输入要买的商品:")
    if goods_num.upper() == "Q":
        break
    goods_num = int(goods_num)
    print("你要购买的商品为“{}”,价格为“{}”".format(goods[goods_num-1].get("name"),goods[goods_num-1].get("price")))
    
# 例题：
data_list = [1,2,3,4,5,6,7,8]
result = {}
for item in data_list:
    if item < 5:
        if "xx" in result:
            result["xx"].append(item)
        else:
            result["xx"] = [item]
    else:
        if "hh" in result:
            result["hh"].append(item)
        else:
            result["hh"] = [item]
print(result)

# 例题：
addr_list = [
['王*龙', '北京市,海淀区', '苏州街大恒科技大厦南座4层'],
['庞*飞', '北京市,昌平区', '汇德商厦四楼403'],
['顾*锐', '江苏省,扬州市', '三垛镇工业集中区扬州市立华畜禽有限公司'],
['王*飞', '上海市,徐汇区', '上海市徐汇区H88越虹广场B座5E'],
['华*升', '北京市,海淀区', '杰睿大厦'],
['朱*锴', '上海市,浦东新区', '川沙新镇华川家园33号楼503'],
['陈*盼', '浙江省,杭州市', '闲林街道,西溪华东园,十幢一单元401。'],
]
info = {}
for item in addr_list:
    addr_address = item[1].split(",")
    province = addr_address[0]                  # addr_address[0] = **省
    name = item[0]
    if province in info:
        info[province].append(name)
    else:
        info[province] = [name]
print(info)
```



### 2.4 集合(set)

```python      
# 集合是一个无序、可变、元素必须是哈希值且元素不重复
v1 = { 11, 22, 33, 44, 55}
v1.add(66)
print(v1)                             # { 11, 22, 33, 44, 55, 66}
v1.add(33)
print(v1)                             # { 11, 22, 33, 44, 55, 66}
```

#### 2.4.1 独特功能

```python
# 1.添加元素
v1 = set{}
v1.add(33)
v1.add("蜡笔小新")
print(v1)                              # {33,"蜡笔小新"}

# 2.删除元素
v1 = {11,22,33}
v1.discard(33)
print(v1)                              # {11,22}

# 3.并集
v1 = {"蜡笔小新","哆啦","管制"}
v2 = {"管制","空心","张三"}

res = v1.union(v2)
print(res)                         # {'哆啦', '张三', '管制', '空心', '蜡笔小新'}

res2 = v1 | v2
print(res2)                        # {'哆啦', '张三', '管制', '空心', '蜡笔小新'}

# 差集
v1 = {"蜡笔小新","哆啦","管制"}
v2 = {"管制","空心","张三"}

res = v1.difference(v2)
print(res)                         # {'哆啦', '蜡笔小新'}

res2 = v1 & v2
print(res2)                        # { '管制'}
```



#### 2.4.2 公共功能

```python
# 1.长度
v1 = {"蜡笔小新","哆啦","管制"}
data = len(v1)
print(data)                     #3

# 2.for循环
v1 = {"蜡笔小新","哆啦","管制"}
for item in v1:
	print(item)
    
# 3.in查询
v1 = {"蜡笔小新","哆啦","管制"}
if "蜡笔小新" in v1:
    print("在")
else:
    print("不在")
```



### 2.5 容器转换

- list

```python
v1 = [1,2,3,4]
```

- tuple

```python
v2 = (1,2,3,4)
```

- set

```python
v3 = {1,2,3,4}
```

原则：想转换谁就用谁的英文字母包裹一下

```python
v1 = [1,2,3,4]
res = tuple(v1)
print(res)             # (1,2,3,4)

v2 = [1,1,2,3,3,4]
res = set(v2)
print(res)             # {1,2,3,4}
```

 

### 2.6 None类型

None表示空值

```python
# v1设置为空
v1 = None
v1 = "蜡笔小新"

v2 = ""
v2 = "蜡笔小新"              # 区别：又独立创建了一块内存
```

### 2.7 布尔类型

```python
0、""、[]、{}、set()、None  ->  False
其它都是True
```

### 2.8 浮点型

```python
v1 = 0.1
v2 = 0.2
v3 = v1 + v2
print(v3)              # 0.3000...4

v1 = decimal.Decimal("0.1")
v2 = decimal.Decimal("0.2")
v3 = v1 + v2
print(v3)              #0.3
```

### 2.9 字节类型(bytes)

```python
name = "蜡笔小新"                           # str字符串，底层是unicode编码存储
data = name.encode("utf-8")               # bytes字节，底层是utf-8编码
print(data)                               # b'\xe8\x9c\xa1 \xe7\xac\x94\ xe5\xb0\x8f \xe6\x96\xb0'


name = "蜡笔小新"                           # str字符串，底层是unicode编码存储
data = name.encode("gbk")                 # bytes字节，底层是gbk编码
print(data)                               # b'\xc0\xaf \xb1\xca \xd0\xa1 \xd0\xc2'
```



## 2 注释

```python
# 单行注释

"""
多
行
注
释
"""
```



## 3 输入

```python
text = input("请输入名字") # 用户输入的永远是字符串类型
print(text)
```



## 4 条件语句

```python
if 条件/真假 ：
	条件成立后执行此处代码
else:
    不成立，走此处代码
    
if 1 > 2:
    print("真的")
else:
    print("假的")
    
# 实例1  使用format时需要配合{}使用
name = input("请输入name：")
name_code = name.upper()
if name_code != "Q":
    print("恭喜{}".format(name))
else:
    print("遗憾{}".format(name))
    
# 多条件
if 条件1:
    print("条件A")
elif 条件2:
    print("条件B")
elif 条件3:
	print("条件C")
else:
    print('前面都不符合，执行else')
    
```



## 5 嵌套

```python
if 条件A:
	if 条件B:
		if 条件C:
    		pass
        else:
        	pass
    else:
        pass
elif 条件D:
    pass


# 模拟客服
print("欢迎致电1001，提供以下服务：1.花费服务；2.宽带业务；3.企业业务；4.人工服务")

choice = input("请选择序号")

if choice == "1"
	print("话费业务")
    print("1.话费查询 2.话费充值 3.话费异常")
    second_choice = input("请输入：")
    if second_choice == "1":
    	XXX
    elif second_choice == "2":
    	xxx
    elif second_choice == "3":
    	xxx
    else:
        xxx
elif choice == "2":
    xxx
elif choice == "3":
    xxx
elif choice == "4":
    xxx
else:
    xxx
print("感谢您的来电")
```



## 6 while循环

```python
print("开始")
while 条件:
	...
    ..
    ....
print('结束')

# 实例1：
print("开始")
num = True
while num:
	print("123")
    num = false
print('结束')

# 实例2:
num = 1
while num < 5:
    print("蜀国")
    num = num + 1
print("结束")

# 实例3:
while True:
    num = int(input("请输入要猜的数字:"))
    if num > 50:
        print("猜大了")
    elif num < 50:
        print("猜小了")
    else:
        print("对了")
        break
```



## 7 字符串格式化

```python
# 中括号中的数字代表format中的第n个元素，没有就默认0，1，2，3.....
text = "我的名字叫{0}，今年{1}岁了".format("蜡笔小新",5)
print(text) # 我的名字叫蜡笔小新，今年5岁了

tpl = "我的名字叫{}，今年{}岁了"
v1 = tpl.format("蜡笔小新",5)
v2 = tpl.format("灰太狼",32)

# Python3.6+之后才有的格式化
name = "蜡笔小新"
age = 5
text = f"我的名字{name},今年{age}岁"
print(text)
```



## 8. 运算符

- 算数运算符

```python
value = 9 % 2
print(value) # 1
```

- 比较运算符

```python
>
<
>=
<=
!=
==
```

- 成员运算，xx是否是xx

```python
text = "蜡笔小新的同年"
v1 = "蜡笔小新" in "蜡笔小新的同年" # ture
v2 = "灰太狼" in "蜡笔小新的同年"   # false
v3 = "蜡笔小新" in text           # ture

text = input("请输入你的评论:")
if "蜡笔小新" in text:
    print("评论包含蜡笔小新")
else:
    print("评论不包含蜡笔小新")
```

- 逻辑运算符

```python
v1 = user == "root" and pwd == "123"

'''
值 and 值
逻辑运算的结果取决于那个值，结果就等于那个值
v1 = 2 and 4
v2 = 0 and 2
v3 = 2 and 0
v4 = "" and 9
'''
v1 = 2 and 4
print(v1) # 4
```

# 基础概念

## 1 进制

计算机底层都是10101010101001（二进制）

```python
'''
二进制以0b开头
八进制以0o开头
十六进制以0x开头
'''
# 十进制转换成2，8，16
v1 = bin(238)
print(v1) # 0b11101110

v2 = oct(238)
print(v2) # "0o356"

v3 = hex(238)
print(v3) # "0xee"
# 2，8，16转换成十进制
dl = int("0b11101110",base=2)
d2 = int("0o356",base=8)
d3 = int("0xee",base=16)
```



![进制转换（2、8、10、16进制）_虚拟磁盘10进制转换方法-CSDN博客](https://i-blog.csdnimg.cn/blog_migrate/864f5ce4033cac6603cbd2087d760021.png)

## 2 计算机中的单位

- b (bit), 位

```python
0     #1位
1     #1位
100   #3位
```

- B(byte)，字节

```python
8位是一个字节
10110111            一个字节
10110111 10110111   两个字节
```

- KB(kilobyte)，千字节

```python
1024个字节就是1kb
10110111 10110111 10110111 10110111 ......., 1kb
1kb = 1024B = 1024 * 8b
```

- M(Megabyte),  兆.     G(Gigabyte),千兆

```python
1M = 1024KB
1G = 1024M
```

## 3 编码

编码，文字与二进制的对照表

### 3.1 ASCII编码

ASCII编码中总共有256个对应关系

![image-20260114102100270](assets/image-20260114102100270.png)

### 3.2 gbk和gbk2312

GB-2312,国家信息委员会制作

GBK，GB-2312的扩展，包含中日韩

### 3.3 unicode(万国码)

- ucs2, 用固定的2个字节表示二进制和文字的对应关系。2**16=65535
- ucs4，用固定的4个字节表示二进制和文字的对应关系  2**32=4294967296

### 3.4 UTF-8编码

对unicode进行压缩，用尽可能少的字节来表示数据

- utf-8中，一个文字用3个字节表示

### 3.5 Python

```python
name = "蜡笔小新"              # 字符串类型，unicode来存储（ucs4）
data = name.encode('utf-8')   # 字节类型， utf-8编码来存储
print(data)
```

在Python开发中，做文件存储或是文件传输时，不能直接用字符串，而是将字符串压缩成utf-8编码的字节，然后来传输和存储

```python
# 在文件中写入一个字符串
name = "蜡笔小新"
# 1.打开文件
file_object = open("vip.txt",mode="ab")
# 2.写入内容
file_object.write(name.encode('utf-8'))
# 3.关闭文件
file_object.close()
```

- 文件编码

  - 写文件。写了很多内容 -> 按照某种编码去存储文件（10101010）
  - 读文件。真正的内容读取出来，用同样的编码才能读取到文本内容

- Python解释器将代码读取到内存之后，是需要进行：

  - 语法分析&词法分析

    ```python  
    name = "蜡笔小新"     # 字符串处理，去unicode对应关系中找  01010101001
    age = b"xxxooaxa"    #字节，去utf-8对应关系找  0101001011
    ```


# 文件操作



## 1 快速写文件

- 写文件

```python
# 1.打开文件---------------------------------------------------------------------------------------
# - "unicom.txt"  文件路径
# - mode="wb"     写文件的模式打开,由于是wb模式：文件不存在，则创建文件；文件存在，则清空文件
file_object = open("unicom.txt", mode="wb")
# 2.写内容
name = "蜡笔小新"    # unicode
file_object.write(name.encode("utf-8"))
file_object.close()

# 例题
file_object = open("unicom.txt", mode="wb")

while True:
    name = input("用户名(Q/q退出):")
    if name.upper() == "Q":
        break
    pwd = input("密码:")
    text = "用户名：{} 密码：{} \n".format(name, pwd)
    file_object.write(text.encode("utf-8"))
file_object.close()
print("==========================用户登入===========================")
file_object = open("unicom.txt", mode="rb")
username = input("用户名(Q/q退出):")
userpwd = input("密码:")
is_success = False
text = "用户名：{} 密码：{} \n".format(username, userpwd)
for line in file_object:
    file_string = line.decode("utf-8")
    if username.upper() == "Q":
        break
    if file_string == text:
        is_success = False
if is_success:
    print("登入成功")
else:
    print("登入失败")
file_object.close()

# 2.追加 --------------------------------------------------------------------------------------------
# wb模式：文件不存在，则创建文件；文件存在，则打开文件,写内容永远写在文件尾部
file_object = open("unicom.txt", mode = "ab")
file_object.write(file_object.encode("utf-8"))
file_object.close()

# 3.读取内容 -----------------------------------------------------------------------------------------
file_object = open("unicom.txt", mode = "rb")
data = file_object.read()
# 破译
data_string = data.decode("utf-8")
print(data_string)

row_list = data_string.split("\n")
print(row_list)

file_object.close()

# 例题
file_object = open("unicom.txt", mode = "rb")
for line in file_object:
    data_text = line.decode("utf-8").strip()
    if data_text:
        data_list = data_text.split(",")
        print(data_list[1])
file_object.close()
```

## 2 with上下文

```python
file_object = open(...)

file_object.read()

file_object.close()  # 强调关闭文件

print("开始")
# 离开缩进时，自动关闭文件
with open("xxx.txt",mode="rb") as file_object :
    data = file_object.read()
    print(data)
```

## 3 打开文件的模式

- wb 写

```python
file_object = open("unicom.txt", mode="wb")

name = "蜡笔小新"    # unicode
file_object.write(name.encode("utf-8"))

file_object.close()
```

- w

```python
file_object = open("unicom.txt", mode="w", coding="utf-8")

name = "蜡笔小新"    # unicode
file_object.write(name)

file_object.close()
```

- ab 追加

```python
file_object = open("unicom.txt", mode="ab")

name = "蜡笔小新"    # unicode
file_object.write(name.encode("utf-8"))

file_object.close()
```

- a

```python
file_object = open("unicom.txt", mode="a", encoding="utf-8")

name = "蜡笔小新"    # unicode
file_object.write(name)

file_object.close()
```

- rb 读

```python
file_object = open("unicom.txt", mode="rb")

# 读出来是文件内部被压缩的utf-8编码数据
data = file_object.read()
# utf-8 -> unicode(字符串)
data_string = data.decode("utf-8")
print(data)

file_odject.close()
```

- r

```python
file_object = open("unicom.txt", mode="r", encoding="utf-8")

data = file_object.read()

file_object.close()
```

# 函数

## 1.初识函数

```python
# 函数像一大堆代码，给做一堆代码起个名字
def 函数名():
    print(123)
    print(456)
    ....
# 执行函数
函数名()
```

- 面向对象编程：按业务逻辑从上到下去打代码

```python
print("欢迎使用xx系统")

if cpu占有率 > 90%:
    发警报邮件-10行
    
if 硬盘使用率 > 90%:
    发警报邮件-10行
    
if 内容使用率 > 90%:
    发警报邮件-10行
```

```python
# 1.生成一副扑克牌
# 2.洗牌
# 3.给五个玩家发三张牌
# 4.玩家手中的牌大小比较
```



- 函数式编程：用函数来写代码

```python
def 发送文件():
	发警报邮件-10行

print("欢迎使用xx系统")

if cpu占有率 > 90%:
    发送文件()
    
if 硬盘使用率 > 90%:
    发送文件()
    
if 内容使用率 > 90%:
    发送文件()
```

函数应用场景：

- 反复用到重复代码时
- 业务逻辑太长，将代码进行拆分

## 2.Python代码发文件

- 注册邮箱 : 此处网易.163

- 配置 : 开启POP3/SMTP服务
- 获取授权码，通过代码发文件 : PTLjDSTUnrJKBrfv
- SMTP服务器 : smtp.163.com



- 代码发邮件

```python
# 1.将Python内置的模块导入
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 2.构建文件内容
msg = MIMEText("早上好", "html", "utf-8")
msg["From"] = formataddr(["蜡笔小新", "13202651172@163.com"]) # 自己的名字/自己的邮箱
msg['to'] = "2438012849@qq.com"                              # 目标邮箱
msg['Subject'] = "莫非成功"                                   # 主题

# 3.发送邮件
server = smtplib.SMTP_SSL("smtp.163.com")
server.login("13202651172@163.com", "PTLjDSTUnrJKBrfv")    # 账户/授权码
server.sendmail("13202651172@163.com", "2438012849@qq.com", msg.as_string()) # 自己的邮箱/目标邮箱/内容
server.quit()
```



### 案例

1.伪代码：监控系统

```python
def 发送文件():
	# 1.将Python内置的模块导入
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    # 2.构建文件内容
    msg = MIMEText("早上好", "html", "utf-8")
    msg["From"] = formataddr(["蜡笔小新", "13202651172@163.com"]) # 自己的名字/自己的邮箱
    msg['to'] = "2438012849@qq.com"                              # 目标邮箱
    msg['Subject'] = "莫非成功"                                   # 主题

    # 3.发送邮件
    server = smtplib.SMTP_SSL("smtp.163.com")
    server.login("13202651172@163.com", "PTLjDSTUnrJKBrfv")    # 账户/授权码
    server.sendmail("13202651172@163.com", "2438012849@qq.com", msg.as_string()) # 自己的邮箱/目标邮箱/内容
    server.quit()

print("欢迎使用xx系统")

if cpu占有率 > 90%:
    发送文件()
    
if 硬盘使用率 > 90%:
    发送文件()
    
if 内容使用率 > 90%:
    发送文件()
```

2.需求

```python
# 1.将Python内置的模块导入
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# 目前给3给账号发邮件(通过参数传递)
v1 = 2438012849@qq.com
v2 = 2438012848@qq.com
v3 = 2438012847@qq.com

def send_email(to_email):
    # 2.构建文件内容
    msg = MIMEText("早上好", "html", "utf-8")
    msg["From"] = formataddr(["蜡笔小新", "13202651172@163.com"]) # 自己的名字/自己的邮箱
    msg['to'] = to_email                                         # 目标邮箱
    msg['Subject'] = "莫非成功"                                   # 主题

    # 3.发送邮件
    server = smtplib.SMTP_SSL("smtp.163.com")
    server.login("13202651172@163.com", "PTLjDSTUnrJKBrfv")      # 账户/授权码
    server.sendmail("13202651172@163.com", to_email, msg.as_string()) # 自己的邮箱/目标邮箱/内容
    server.quit()
send_email(v1)
send_email(v2)
send_email(v3)
```



## 3.函数的参数

```python
def 函数名(形式参数1, 形式参数2, 形式参数3):
    函数内部代码
函数名(1, 2, 3)

# 例子
def my_func(a1, a2, a3):
    result = a1 + a2 + a3
    print(result)
# 位置传参
my_func(1, 2, 4)
# 关键字传参
my_func(a2 = 3, a3 = 2, a1 = 4)

# 例题：
# 统计a的个数
def sum_string(a1):
    sum = 0
    for item in a1:
        if item.upper() == "A":
            sum += 1
    print(sum)
sum_string("assdfadfda")
```

### 3.1 默认参数

```python
# 函数设置默认参数时，只能放在最后
def func(a1, a2=2, a3=3):
    pass
func(2)
```

### 3.2 动态参数

```python
# 动态参数*统一默认为元组
def func(*a1):
    print(a1)
func(1,2,3,4)
func(True,11,22,"xxxx"，[1,2,3])

# 动态参数**统一默认为字典
# dt = {"a1":1, "a2":2, "a3":3, "a4":4}
def func(**dt):
    print(dt)
func(a1=1,a2=2,a3=3,a4=4)

# 混合使用
def func(*a,**dt):
    print(dt)
func(11,22,33,a1=1,a2=2,a3=3,a4='root')
```

## 4.函数的返回值

- print，输出，可以在任何地方使用
- 函数的返回值

```python
def func(a1, a2):
    res = a1 + a2
    return res
# 1.执行func函数
# 2.将函数的返回值赋值给data
# 3.返回值可以是任意类型
data = func(100,200)

# 函数没有返回值，默认返回None
def func(a1, a2):
    res = a1 + a2

data = func(100, 200)

# 例题：
def sum_number(*a):
    items = 0
    for item in a:
        items += item
    return items
Sum = sum_number(1,2,3,4,5)
print(Sum)

# 例题：判断文件路径是否存在
import os
from fileinput import close


def check_file(file_path, file_name):
    # 判断路径是否存在
    res = os.path.exists(file_path)
    if not res:
        return
    data_list = []
    file_object = open(file_path, mode='r', encoding='utf-8')
    for line in file_object:
        line = line.strip()
        if file_name in line:
            data_list.append(line)
    file_object.close()
    return data_list
result = check_file("C:\Program Files", "W")
```

## 5.函数的调用

```python
def func():
    print(123)
func()         # 函数的调用一定是在内存中函数以及创建才能调用
```

数据类型中

- **可变类型**：列表、字典、集合
- **不可变类型**：字符串、整形、元组、布尔类型

# 6.函数参数传递的是内存地址

```python
v1 = "蜡笔小新"
v2 = v1         # 它们指向的是同一个内存地址


def func(a1):
    pass
v1 = "蜡笔小新"
func(v1)        # 函数在传递参数时，默认不会重新创建一个数据，在赋值给函数中的参数时，是指向同一块内存地址

def func(a1):
    a1.upper()
v1 = "lbxx"
func(v1)        # "lbxx"，字符串是不可改变类型，a1.upper()生成的是一个新的值
```

