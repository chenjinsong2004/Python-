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

## 6.函数参数传递的是内存地址

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

## 8 作用域

### 8.1 作用域基础

- 作用域可以理解成就是一块内存，只要在这个区域就可以共享这个区域的数据
- 在Python中，执行函数，就会创建一个作用域，出了函数作用域会被销毁
- Python代码只要一运行，就会有一个全局作用域

```python
name = "蜡笔小新"              # 全局作用域
age = 5                       # 全局作用域
if True:
    email = "xxx@qq.com"      # 全局作用域
else:
    gender = "男"

for i in range(10):           # 全局作用域 i = 9
    pass
```

### 8.2 关于变量

```python
# 潜规则：定义全局变量用大写，多个单词用下划线连接
# 全局变量
USER_LIST = []

def register[]:
    while True:
        name == input(">>>")
        if name.upper == "Q":
			return
        USER_LIST.append(name)
        
def show_users[]:
    for item in USER_LIST:
        print(item)
        
def run():
	register()
    show_users()
run()
```

```python
NAME = "蜡笔小新"

def func():
    NAME = "哇塞"
    print(NAME)

print(NAME)      # "蜡笔小新"
func()           # "哇塞"
print(NAME)      # "蜡笔小新"
```

### 8.3 global关键字

global用于表示此变量不是新创建的数据，而是全局变量中的那个数据（地址指向相同）

```python
# 案例1
NAME = "蜡笔小新"

def func():
    global NAME
    NAME = "哇塞"
    print(NAME)

print(NAME)      # "蜡笔小新"
func()           # "哇塞"
print(NAME)      # "哇塞"

# 案例2
NAME = [11, 22]

def func():
    global NAME
    NAME = [33, 44]
    print(NAME)

print(NAME)      # [11, 22]
func()           # [33, 44]
print(NAME)      # [33, 44]

# 案例3
NAME = [11, 22]

def func():
    NAME.append(999)
    print(NAME)

print(NAME)      # [11, 22]
func()           # [11, 22, 999]
print(NAME)      # [11, 22, 999]
```

## 9.函数名就是变量名

```python
name = "蜡笔小新"              # 全局作用域
age = 5 

def func():
    print(123)
    print(456)
func = 123
print(func)                  # 123

# 案例2
def func():
	print(123)
    print(456)
v1 = func                    # v1 = 函数func
v2 = func()                  # v2 = None
v3 = v1()                    # v3 = None

# 案例3
def send_sms():
	print("发送短信报警")
    
def send_emali():
	print("发送邮箱报警")

def send_dingding():
	print("发送丁丁报警")

def send_wechat():
	print("发送微信报警")
    
func_list = [send_sms, send_emali, send_dingding, send_wechat]
for item in func_list:
    item()
    
# 案例4
def func():
    return 123
func_dict = {
    "11":func,
    "22":func,
    "33":func
}
func_object = func_dict.get("22")
if func_object == None:
    print("函数不存在")
else:
    func_object()

# 例题1
while True:
    select_user = input("1.登入；2.注册;3.查询:")
    if select_user.upper() == "Q":
        break
    def log_in():
        print("登入")
    def register():
        print("注册")
    def query():
        print("查询")
    select_dict = {"1":log_in, "2":register, "3":query}
    func_object = select_dict.get(select_user)
    if select_user in select_dict:
        func_object()
    else:
        print("输入错误,请重新输入")

# 例题2
import requests

while True:
    select_user = input("1.图片专区；2.NBA专区;3.短视频专区（Q/q退出）:")
    if select_user.upper() == "Q":
        break
    def download(Url, file_name):
        res = requests.get(
            url=Url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )
        file_object = open(file_name, mode='wb')
        file_object.write(res.content)
        file_object.close()
    def picture():
        image_dict = {
            "1": ("小姐姐", "https://ts1.tc.mm.bing.net/th/id/OIP-C.qOVNXup8kQ0DZg7RTVN3ZwHaE8?w=252&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2"),
            "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbn0"),
            "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzo0d"),
            "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
        }
        while True:
            for item in image_dict.keys():
                print(item, image_dict.get(item)[0], end="")
            select = input("  请选择（Q/q返回）:")
            if select.upper() == "Q":
                break
            image_select = image_dict.get(select)
            if select in image_dict:
                download(image_select[1], image_select[0] + ".png")
                print(image_select)
            else:
                print("输入错误,请重新输入")

    def nba():
        nba_dict = {
            "1": {
                "title": "威少奇才首秀三双",
                "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"
            },
            "2": {
                "title": "塔图姆三分准绝杀",
                "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"
            }
        }
        while True:
            for item in nba_dict.keys():
                print(item, nba_dict.get(item).get("title"))
            select = input("请选择你要的nba的序号（Q/q返回）:")
            if select.upper() == "Q":
                break
            nab_select = nba_dict.get(select)
            if select in nba_dict:
                download(nab_select.get("url"), nab_select.get("title") + "MP4")
                print(nab_select.get("title"),nab_select.get("url"))
            else:
                print("输入错误,请重新输入")

    def video():
        video_dict = {
            "1": {
                "title": "哪里来的乱劈风砍法蛮王",
                "url": "https://www.bilibili.com/video/BV1xSivBYEW5/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=579a303d7c799b451025d68c15b04a64"
            },
            "2": {
                "title": "你管这叫三星四费",
                "url": "https://www.bilibili.com/video/BV1BGBCBmE5v?spm_id_from=333.788.recommend_more_video.0&trackid=web_related_0.router-related-2206419-2kqqq.1768962350864.144&vd_source=579a303d7c799b451025d68c15b04a64"
            },
            "3": {
                "title": "天阶功法！校长发明了以绪塔尔转盗宗",
                "url": "https://www.bilibili.com/video/BV1ACkeBgEMc/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=579a303d7c799b451025d68c15b04a64"
            }
        }
        while True:
            for item in video_dict.keys():
                print(item, video_dict.get(item).get("title"))
            select = input("请选择你要的图片的序号（Q/q返回）:")
            if select.upper() == "Q":
                break
            video_select = video_dict.get(select)
            if select in video_dict:
                download(video_select.get("url"), video_select.get("title") + "MP4")
                print(video_select.get("title"), video_select.get("url"))
            else:
                print("输入错误,请重新输入")

    select_dict = {"1":picture, "2":nba, "3":video}
    func_object = select_dict.get(select_user)
    if select_user in select_dict:
        func_object()
    else:
        print("输入错误,请重新输入")
```

## 10 lambda表达式（匿名函数）

```python
def func():
    return 123

# func是函数名（变量）
# lamdba : 函数体，函数中写了123，内部自动执行一个return
func = lambda : 123
res = func()
print(res)            # 123
# ------------------------------------------------------------------
func = lambda a1,a2 : a1 + a2
res = func(100,200)
print(res)            # 300
#-------------------------------------------------------------------
func = lambda data_string : data_string.upper
res = func("root")
print(res)            # "ROOT"
#-------------------------------------------------------------------
func = lambda data_list : data_list[0]
res = func([1,2,3,4])
print(res)            # 1
#-------------------------------------------------------------------
func = lambda data_list : data_list.append(123)
value = func([1,2,3])
print(value)          # None
```

## 11 函数做参数

```python
def do():
    print("do")
def func(a1, a2):
    print(a1)
    a2()
func(11, do)
```

## 12.内置函数

### 12.1 第一组（计算）

- abs，绝对值

```python
data = abs(-10)
print(data)      # 10
```

- pow，次方

```python
data = pow(2, 5)
print(data)      # 2的5次方
```

- sum，求和

```python
num_list = [1,2,3,4,5]
res = sum(num_list)
print(res)       # 求和
```

- divmod，商和余数

```python
v1,v2 = divmod(92,10)
print(v1)        # 9
print(v2)        # 2
```

- round，保留几位小数点

```python
data = round(1.142423,2)
print(data)      # 1.14
```

### 12.2 第二组（）

- min，求最小值

```python
data = [11,22,33,44,-11,10]
res = min(data)
print(data)
```

- max，最大值

```python
data = [11,22,33,44,-11,10]
res = max(data)
print(data)
```

- all，是否所有元素都是True

```python
data = [1,-1,2,5]
v1 = all(data)
print(v1)         # True

data = [1,-1,2,0]
v1 = all(data)
print(v1)         # False

v1 = input("用户名：")
v2 = input("密码：")
is_valid = all([v1, v2])
if is_valid:
    print("都不为空")
else:
    print("用户名或密码为空")
```

### 12.3 第三组（进制转换）

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

# 例题
ip = "192.168.11.23"
ip_list = ip.split(".")
bin_str_list = []
for items in ip_list:
    items = int(items)
    bin_items = bin(items)
    bin_items = bin_items[2:].zfill(8)
    bin_str_list.append(bin_items)
str_list = ".".join(bin_str_list)
print(str_list)
```

### 12.4 第四组（unicode）

编码时Unicode，将文字和二进制做上对应

```python
# ord
v1 = ord("A")
print(v1)        # 65

# chr
v2 = chr(65)
print(v2)        # A

# 例题
import random

char_list = []
for i in range(6):
    num = random.randint(65, 90)
    char = chr(num)
    char_list.append(char)
print(char_list) #[]
code = "".join(char_list)
print(code)

```

### 12.5 第五组（类型转化）

- int
- str
- bool
- list
- dict
- set
- tuple
- float
- bytes

### 12.5 第六组（callable，enumerate，sorted）

- len
- print
- input
- open

```python
f = open("xxx",mode='r',encoding='utf-8')
data = f.read()
f.close
```

- range
- hash,计算哈希值

```python
data = hash("蜡笔小新")
print(data)           #-8054500727379162256
```

- type,查看数据类型

```py
def func(data):
    if type(data) == str:
        print(123)
    elif type(data) == list:
        print(456)
func([1,2,3,4])
```

- callable，是否可执行(后面是否可以加括号执行)

```python
name = "蜡笔小新"
v1 = callable(name)
print(v1)           #False

def func():
    print(333)
v2 = callable(name)
print(v2)           #True
```

- enumerate，循环过程中,自动提供自增的一列

```python
goods = ["飞机", "太极跑", "AK47"]

for idx, item in enumerate(goods, 1):        # 1表示从1开始计算
    msg = "{} {}".format(idx, item)
    print(msg)
```

- sorted，排序(不修改原数据，生成新列表)

```python
# 只对列表进行排序
data_list = (33,44,22,11,66,55)
new_data = sorted(data_list)
print(new_data)

# 例题
data_list = [
    '5 编译器和解释器.mp4',
    '17 今日作业.mp4',
    '9 Python解释器种类.mp4',
    '16 今日总结.mp4',
    '2 课堂笔记的创建.mp4',
    '15 Pycharm使用和破解（win系统）.mp4',
    '12 python解释器的安装（mac系统）.mp4',
    '13 python解释器的安装（win系统）.mp4',
    '8 Python介绍.mp4',
    '7 编程语言的分类.mp4',
    '3 常见计算机基本概念.mp4',
    '14 Pycharm使用和破解（mac系统）.mp4',
    '10 CPython解释器版本.mp4',
    '1 今日概要.mp4',
    '6 学习编程本质上的三件事.mp4',
    '18 作业答案和讲解.mp4',
    '4 编程语言.mp4',
    '11 环境搭建说明.mp4'
]
sorted_list = sorted(data_list, key=lambda x: int(x.split(' ')[0]))
print(sorted_list)
```

## 5 推导式

### 5.1列表推导式

```python
data_list = [1,2,3,4,5]
#---------------------------------------
data_list = [i for i in range(100)]            # 0-99

#---------------------------------------
data_list = [100 for i in range(100)]          # 100个100

#---------------------------------------
data_list = [100 + i for i in range(100)]      # 100-199

#---------------------------------------
data_list = [[1, 2] for i in range(100)]       # 100个[1, 2]

#---------------------------------------
data_list = [(i, i + 10) for i in range(100)]  # [(0,10),(1,11),...........(99,109)]

#---------------------------------------
data_list = ["工号-{}".format(i) for i in range(100)] # ["工号-0", "工号-1", "工号-2", ...........,"工号-99"]

#---------------------------------------
data_list = [i for i in range(10) if i > 6]     # [7,8,9]

#---------------------------------------
data_list = [i for i in range(100) if i > 6 and i < 10]     # [7,8,9]

# 案例1
data_list = [11, True, "蜡笔小新", [11,22], 33]
result = [i for i in data_list if type(i) == int]
print(result)

# 案例2
data_list = [
    '5 编译器和解释器.mp4',
    '17 今日作业.mp4',
    '9 Python解释器种类.mp4',
    '16 今日总结.mp4',
    '2 课堂笔记的创建.mp4',
    '15 Pycharm使用和破解（win系统）.mp4',
    '12 python解释器的安装（mac系统）.mp4',
    '13 python解释器的安装（win系统）.mp4',
    '8 Python介绍.mp4',
    '7 编程语言的分类.mp4',
    '3 常见计算机基本概念.mp4',
    '14 Pycharm使用和破解（mac系统）.mp4',
    '10 CPython解释器版本.mp4',
    '1 今日概要.mp4',
    '6 学习编程本质上的三件事.mp4',
    '18 作业答案和讲解.mp4',
    '4 编程语言.mp4',
    '11 环境搭建说明.mp4'
]
list_num = [item.split(" ")[0] for item in data_list]
print(list_num)
result = [int(item.split(" ")[0]) for item in data_list]
print(result)
```

### 5.2 字典推导式

```python
data = {i:(i, 100) for i in rang(10)}   # {"0":(0,100), "1":(1,100),......,"9":(9,100)}

# 例题1
text = "query=xx&_asf=www.sogou.com&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=847&sst0=1636790847260&sugsuv=1626278055911299&sugtime=1636790847260"

result = {item.split("=")[0] : item.split("=")[1] for item in text.split("&")}
```

## 6.关于pip.exe

下载视频时，用到pip去下载第三方包

pip是一个专门用于下载第三方包的工具

### 6.1 常见命令

- 安装

  ```python
  pip install 包名称
  ```

- 卸载

```
pip uninstall 包名称
```

- 将已安装的包写入文件中

```
pip freeze > requirements.txt
```

```
蜡笔小新在自己电脑上安装：
	pip install certifi==2020.12.5    # 前面是名称，后面是版本
批量安装：
	pip install -r requirements.txt
```

### 6.2 配置

![image-20260123090458688](assets/image-20260123090458688.png)

基于豆瓣去下载某第三方包

- 永久默认豆瓣

```py
pip config set global.index-url https://pypi.douban.com/simple/

# 切换成默认源
pip config unset global.index-url

# 以后就用这个就好了
pip install flask
```

### 6.3 源码安装

1.下载源码，然后解压

2.打开终端，进入下载好的目录

3.执行安装命令

```
python3.9 代码包 build
python3.9 代码包 install
```

### 6.4wheel包

- pip支持wheel

```python
pip install wheel
```

- 下载wheel包

![image-20260123093602143](assets/image-20260123093602143.png)

- 进入终端

```
pip3.12 install mysqlclient-2.2.7-cp312-cp312-win_amd64.whl
```

# 模块与包

- 模块就是指py文件，我们可以将某个功能按照某种维度划分

```
自定义
内置
第三方
```

- 包就是指文件夹

## 1.自定义模块和包

![image-20260123101859434](assets/image-20260123101859434.png)

### 1.1 快速上手

```python
import utills
import commons.pool

Choice = input("请输入")
res = utills.str_to_int(Choice)
if res == None:
    print("输入错误")
else:
    msg = "序号是：{}".format(res)
    print(msg)
```

### 1.2 关于模块与包的导入

- 运行文件所在的同级目录。【导入成功】
- 运行模块和包在python安装目录。【导入成功】

- 运行模块在其它地方

```python
import sys
# 自定义文件夹添加到sys.path
sys.path.append(r"C:\code")

# 导入C:\code下的文件
import 文件名
```

### 1.3 模块与包的导入方式

- import导入

```python
import utils
utils.u_f1()

import commons.pager
commons.pager.p_1()
```

- from导入

```python
from utils import u_f1
u_f1()

from commons.pager import p_1, p_2, p_3
p_1()

from commons import pager
pager.p_1
```

## 2.常见的内置模块

### 2.1 hashlib

对一个数据进行加密的模块，防止数据库泄露

```python
import hashlib

data = "admin"
obj = hashlib.md5()
obj.update(data.encode("utf-8"))
res = obj.hexdigest()
print(res)
```

MD5加密不可反解

```
admin   ->   21232f297a57a5a743894a0e4a801fc3
```

案例

```python
user_dict = {
    "lbxx":"21232f297a57a5a743894a0e4a801fc3"
}

user = input("用户名:")
pwd = input("密码:")

db_pwd = user_dict.get(user)
```

#### 2.1.1 加盐

```python
import hashlib

data = "admin"

salt = "uhgiuehig3huh458gh549g42958hg9h54"
obj = hashlib.md5(salt.encode("utf-8"))
obj.update(data.encode("utf-8"))
res = obj.hexdigest()
print(res)

# 例题
import hashlib

from python入门语法.day05.download import file_object


def md5(data_string):
    salt = "uhgiuehig3huh458gh549g42958hg9h54"
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(data_string.encode("utf-8"))
    res = obj.hexdigest()
    return res
def login():
    print("用户登入：")
    user = input("用户名:")
    pwd = input("密码:")
    encrypt_pwd = md5(pwd)
    is_success = False
    with open("db.txt", mode="r", encoding="utf-8") as file_object:
        for line in file_object:
            data_line = line.strip().split(",")
            if data_line[0] == user and data_line[1] == encrypt_pwd:
                is_success = True
                break
    if is_success:
        print("登入成功")
    else:
        print("登入失败")
def register():
    print("请注册：")
    user = input("用户名:")
    pwd = input("密码:")
    encrypt_pwd = md5(pwd)

    line = "{},{}\n".format(user, encrypt_pwd)
    with open("db.txt", mode="a", encoding="utf-8") as file_object:
        file_object.write(line)
def run():
    func_dict = {
        "1":login,
        "2":register
    }
    choice = input("1.登入  2.注册")
    func = func_dict.get(choice)
    if not func:
        print("输入错误")
        return
    func()
run()
```

### 2.2 random

```python
# 例题1 随机删除列表元素
import random

data_list = ['a', 'b', 'c', 'd', 'e']
idx = random.randint(0, len(data_list) - 1)
element = data_list.pop(idx)
print(element)
print(data_list)

# 例题2 生成验证码
import random

char_list = []
for item in range(1, 6):
    num = random.randint(65, 90)
    char = chr(num)
    char_list.append(char)
char = "".join(char_list)
print(char)

# 例题3 打乱0 - 99的数
import random

num_list = [i for i in range(0, 100)]
random.shuffle(num_list)
print(num_list)

# 例题4
import random

# 创建员工
user_list = ["工号-{}".format(i) for i in range(1, 301)]

# 奖项信息
data_list = [
    ("三等奖", 5),
    ("二等奖", 3),
    ("一等奖", 2),
    ("特等奖", 1),
]

# 抽奖
for item in data_list:
    input("点击回车继续抽奖")
    text = item[0]
    count = item[1]
    lucky_user = random.sample(user_list, count)
    for name in lucky_user:
        user_list.remove(name)
    user_string = ",".join(lucky_user)
    message = "获得{}的名单：{}".format(text, user_string)
    print(message)
```

###  2.3 json

本质上：是一种数据格式，字符串形式

用处：让不同编程语言实现数据传输

JSON格式：

- 外部整体大的字符串
- json字符串内部如果有字符串，一定需要用双引号
- json字符串中不会存在python中的元组格式

```python
info = {'k1':123, 'k2':(11,22,33,44)}

JSON格式:
    '{"k1":123, "k2":(11,22,33,44)}'
    
# python的数据类型转换成JSON格式的字符串
import json
info = {'k1': 123, 'k2': (11,22,33,44)}
res = json.dumps(info)                     # 序列化
print(res)

# JSON格式的字符串转换成python的数据类型
import json
data_string = '{"k1": 123, "k2": [11,22,33,44]}'
res = json.loads(data_string)              # 反序列化
print(res)
```

#### 2.3.1关于中文

```python
info = {"name":"蜡笔小新","age":5}
v1 = json.dumps(info, ensure_ascii=False)
print(v1)              # {"name": "蜡笔小新", "age": 5}
```

#### 2.3.2序列化

```python
import json
import decimal
data = decimal.Decimal("0.3")
res = float(data)
info = {"name":"蜡笔小新", "age":5, "f":True, "hobby":None, "data":res}
v1 = json.dumps(info, ensure_ascii=False)
print(v1)
```

### 2.4 time

```python
import time

# 获取当前的时间戳
v1 = time.time()
print(v1)

# 停止N秒继续运行
while True:
    print(1)
    time.sleep(1)
```

### 2.5 datatime

- time 时间戳

- datatime 格式

```python
# datetime -> 字符型
import datetime

v1 = datetime.datetime.now()
print(v1, type(v1))            # 2026-01-26 09:19:40.144894 <class 'datetime.datetime'>
string_data = v1.strftime("%Y-%m-%d %H:%M:%S")
print(string_data)
# 字符串 -> datetime ----------------------------------------------------------------
from datetime import datetime
text = "2004-12-1"
res = datetime.strptime(text, "%Y-%m-%d")
print(res, type(res))
```

综合练习  将用户名，加密后的密码与创建时间写入db.txt文件夹

```python
import datetime
import time
import hashlib

salt = "jghohh9348hg98h39hg989heqorg"

while True:
    user = input("请输入用户名:")
    if user.upper() == "Q":
        break
    pwd = input("请输入密码:")
    # 当前时间
    v1 = datetime.datetime.now()
    string_data = v1.strftime("%Y-%m-%d %H:%M:%S")
    # 加密
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(pwd.encode("utf-8"))
    res = obj.hexdigest()
    # 创建列表
    user_list = []
    with open("db.txt", mode="a", encoding="utf-8") as file_object:
        user_string = "{}-{}-{}".format(user, res, string_data)
        file_object.write(user_string)
        file_object.write("\n")
```

综合练习  将内容写入一个当前时间名的文件夹

```python
import datetime
import time

def run():
    while True:
        w = input("请输入内容：")
        if w.upper() == "Q":
            break
        v1 = datetime.datetime.now()
        string_time = v1.strftime("%Y-%m-%d %H-%M")
        with open("{}.txt".format(string_time), mode="a", encoding="utf-8") as file_object:
            file_object.write(w)

run()
```

#### 2.5.1 datetime类型的意义

```python
from datetime import datetime,timedelta

v1 = datetime.now()
res = v1 + timedelta(days=10, hours=20, minutes=122, seconds=2222)
print(res)
```

方便时间的加减

### 2.6 OS

- 路径的拼接

```python
Window系统:  C:\xx\xx\xxx
   Mac系统:  /user/xxx/xxx
 Linux系统:  /user/xxx/xxx
```

```python
import os
path = os.path.join("x1", "x2", "x3", "x4", "log.txt")
print(path)        # x1/x1/x3/x4/log.txt
```

- 找到上级目录

```python
import os

file_path = "x1/x2/x3/x4"

# 找到当前路径的上一级目录
v1 = os.path.dirname(file_path)
print(v1)
```

- abs 绝对路径

```python
# 绝对路径
	C:\phpStudy\phpStudy8.1\phpstudy_pro\WWW\assignment
# 相对路径
	如下图
```

![image-20260126103944587](assets/image-20260126103944587.png)

- 然后生成一个绝对路径

```python
import os
res = os.path.abspath("xx")
# 当前程序所在目录                                             相对目录
# C:\phpStudy\phpStudy8.1\phpstudy_pro\WWW\assignment\       xx
print(res)
```

- 判断路径是否存在

```python
import os

file_path = os.path.join('file', 'db.txt')
if os.path.exists(file_path):
    f = open(file_path, mode='r', encoding='utf-8')
    data = f.read()
else:
    print("路径不存在")
```

- 判断路径是否存在,不存在则创建

```python
import os

file_path = os.path.join('db', '2021', '11月份')
print(file_path)

os.makedirs(file_path)
```

- 删除文件、文件夹

```python
import os

file_path = os.path.join('db', '2021', '11月份', 'log.txt')
print(file_path)
os.remove(file_path)
```

```python
import os
import shutil

file_path = os.path.join('db', '2021', '11月份')
print(file_path)
shutil.rmtree(file_path)
```

- 判断是否是文件夹

```python
import os

file_path = os.path.join('db', '2021', '11月份')
res = os.path.isdir(file_path)
print(res)                         # True或False
```

- 景区订票系统

```python
import os
import shutil
import datetime
from random import choice

def history(user_file):
    if not os.path.exists(user_file):
        print("无历史记录")
        return
    print("=====立即记录=====")
    with open(user_file, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            print(line)

def booking(user_file):
    location = input("请输入景区名称:")
    count = input("订票数量:")
    ctime_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "{},{},{}\n".format(location,count,ctime_string)
    with open(user_file, mode='a', encoding='utf-8') as file_object:
        file_object.write(line)

def file_consist():
    file_db = os.path.join('db')
    if not os.path.exists(file_db):
        os.makedirs(file_db)

def run():
    file_consist()
    user = input("请输入用户名:")
    user_db = os.path.join('db', user + '.txt')
    if os.path.exists(user_db):
        print("欢迎回来，老用户")
    else:
        print("欢迎使用，新用户")


    func_dict = {"1":history, "2":booking}
    while True:
        print("1.订单查询；2.预定")
        Choice = input("(q/Q)")
        if Choice.upper() == "Q":
            break
        func = func_dict.get(Choice)
        if not func:
            print("输入错误，重新输入")
            continue
        if os.path.exists(user_db):
            history(user_db)
        else:
            booking(user_db)

run()
```

- 查找当前文件夹的文件与文件夹

```python
import os

data_list = os.listdir(r"C:\Users\86189\Desktop\css与html\第八天")
print(data_list)

# --------------------------------------------------------------------------

import os
#   当前路径  子文件夹列表   文件列表
for in_path, folder_list, name_list in os.walk(r"C:\Users\86189\Desktop\css与html\第八天"):
    for name in name_list:
        abs_path = os.path.join(in_path, name)
        print(abs_path)
```

- 精准查找

```python
import os

key = "练习"
for in_path, folder_list, name_list in os.walk(r"C:\Users\86189\Desktop\css与html\第八天"):
    for name in name_list:
        if key in name:
            abs_path = os.path.join(in_path, name)
            print(abs_path)
```

# 模块和面向对象

## 1 模块

### 1.1 自定义模块

- py文件或文件夹
- from、import
- sys.path【当前脚本+系统内置目录】
- 自己的模块名不要与内置模块名同名

主文件

```python
def run():
	print(123)
    
#Python内部会创建一个__name__ = "__main__"
#别人导入时会创建__name__ = "文件名"
if __name__ == '__main__':
    run()
```

防止别人一导入就执行，只有主动执行才可以

### 1.2内置模块



#### 1.2.1 shutil

- 删除文件夹

```python
import shutil

shutil.rmtree(r"C:\Users\86189\Desktop\css与html\第八天")
```

- 拷贝文件夹

```python
shutil.copytree("原文件夹", "目标文件夹路径")
```

- 拷贝文件

```python
shutil.copy("原文件夹", "目标文件夹路径\")
```

- 文件重命名

```python
import os
import shutil

if os.path.exists("x10"):
    shutil.move("x10", "x10.txt")
    
if os.path.exists("x1"):
    shutil.move("x1", "x100")
```

- 压缩和解压缩

```python
import shutil
#                  压缩包文件名        后缀名         压缩的文件夹路径
shutil.make_archive(base_name="116", format='zip', root_dir='ppp')
#                     压缩包文件名          要解压的路径         后缀名
shutil.unpack_archive(filename='116.zip', extract_dir='117', format='zip')
```

- 重命名

```python
import shutil
import os

folder_path = r"C:\Users\86189\PycharmProjects\python-learn\python入门语法\learning-python\练习"

for name in os.listdir(folder_path):
    ext = name.rsplit(".", maxsplit=1)[-1]
    if ext != "txt":
        continue
    new_name = name.replace("readme", "练习")
    old_file = os.path.join(folder_path, name)
    new_file = os.path.join(folder_path, new_name)
    # 重命名
    shutil.move(old_file, new_name)
```

#### 1.2.2 re正则表达式

- 正则表达式【与语言无关】
- Python中的re模块



什么是正则表达式？

```python
text = "楼主太厉害了,2438012849@qq.com谢谢楼主"

# 将字符串中的邮箱提取出来
import re

text = "楼主太厉害了,2438012849@qq.com谢谢楼主,电话13202651172"

# 将字符串中的邮箱提取出来
data_list = re.findall(r"1[3589]\d{9}", text)
email_list = re.findall(r"\w+@\w+\.\w+", text, re.ASCII)

print(data_list)
print(email_list)
```



##### 1.字符相关

- 固定文本

```python
import re

text = "你好lbxx，你好lbxxcjs"

data_list = re.findall("lbxx", text)

print(data_list)             # lbxx  lbxx
```

```python
import re

text = "你好3lbxxqpian，时间佛i额外加"

data_list = re.findall("q[pas]", text)
print(data_list)       # ['qp']
```

- 字符范围

```python
import re

text = "你好3lbxxqpian，时间佛i额外加"
data_list = re.findall("l[a-z]", text)
print(data_list)       # ['lb']
```

```python
import re

text = "你好3lbxxqpian，时间佛i额外加"
data_list = re.findall("t[0-9]]", text)
print(data_list)       # [']
```

- \d代表1个数字

```python
import re

text = "root-ad33min-adddd3-admin"
data_list = re.findall("d\d", text)
print(data_list)      # ['d3', 'd3', 'dm']
```

```python
import re

text = "root-ad33min-adddd3-admin"
data_list = re.findall("d\d+", text)        # 0个或n个
print(data_list)      # ['d33min', 'd3', 'dmin']
```

```python
import re

text = "root-ad33min-adddd3-admin"
data_list = re.findall("d\d*", text)        # 0个或n个
print(data_list)      # ['d33min', 'd3', 'dmin']
```

```python
import re

text = "root-ad33min-adddd3-admin"
data_list = re.findall("d\d{2,}", text)        # {n,}, 固定n+个
print(data_list)      # ['d33min', 'd3', 'dmin']
```

```python
import re

text = "root-ad33min-adddd3-admin"
data_list = re.findall("d\d{2,4}", text)        # {n,}, n个到n+2个
print(data_list)      # ['d33min', 'd3', 'dmin']
```

- \w字母、数字、下划线（汉字）只有有加号且不做任何限制就是贪婪模式

```python
import re

text = "你好3lbxxqpian，时间佛i额外叫"
data_list = re.findall("你\w+x", text)
print(data_list)       # ['你好3lbxx']

data_list2 = re.findall("你\w+?x", text)
print(data_list2)      # ['你好3lbx']
```

- "."代表除换行以外的所有字符

```python
import re

text = "你好3lbxxqpian，时间佛i额外叫q"
data_list = re.findall("l.q", text)     # l到q
print(data_list)       # ['lbxxq']
```

- /s空白符

```python
import re

text = "root admin ffdd dmin"
data_list = re.findall("a\w+\s\w+", text)    # \s表示空白
print(data_list)                       # ['admin ffdd']
```

##### 2.数量

- *，0或n
- +，1或n
- ？，0或1
- {n}，固定n个
- {n,}，n+个
- {n,m}，n~m个

注意，默认贪婪匹配

##### 3.分组

- 提取数区

```python
import re

text = "楼主太厉害了,2438012849@qq.com谢谢楼主,电话13202651172,13202652272"
data_list = re.findall("1320(0\d{6})", text)
print(data_list)                #['2651172', '2652272']
```

##### 练习题

1.正则QQ号

```python
[1-9]\d{4,12}       # 首位1-9，位数为4-12
```

2.身份证

```python
\d{17}[\dX]         # 取17位数，最后一位取数字或X
```

3.邮箱地址

```python
\w+@\w+\.+\w      # 此时  .  代表 .
\w+@\w+.       # 此时  .  代表任意字符

email_list = re.findall("\w+@\w+\.+\w+", text, re.ASCII)  # 加上re.ASCII就不会包含中文了
```

##### 4 re模块

- re.findall, 获取匹配成功的所有结果
- re.match, 从开始匹配，开头没匹配成功就不再向后看了，成功之后返回第一个对象

```python
import re

text = "大小逗2b最逗3b"

v1 = re.findall(r"逗\db", text)
print(v1)          # ['逗2b', '逗3b']

v2 = re.match(r"逗\db", text)
print(v2)          # None
if v2:
    content = v2.group()
    print(content)
```

- re.search, 浏览整个表达式，返回第一个对象

```python
import re

text = "大小逗2b最逗3b"

v2 = re.search(r"逗\db", text)
print(v2)          
if v2:
    content = v2.group()
    print(content)  # 逗2b
```

### 1.3 第三方模块

Pythno安装第三方模块的三种方法：

- pip
- 源码
- wheel包

#### 1.3.1requests模块

requests模块，让我们可以通过代码向某个地址发送请求，获取我们可以获取的结果

```
pip install requests
```

```python
import requests

requests.功能
```


##### 1.抓包

查看网络请求

- 地址
- 请求方式
- 传递数据

```python
import requests

# 返回所有数据
# 代码想去豆瓣发送请求并获取数据（窃取数据）
# 防范：1.IP限制 2.你是浏览器才给你返回 3.底层算法：JS算法（逆向算法）
res = requests.get(
    url="https://img1.doubanio.com/view/photo/m_ratio_poster/public/p2926391728.jpg",
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
)

# 原始的响应体
print(res.content)

text = res.content.decode('utf-8')
print(text)
```

##### 案例：号码搜索

```python
import requests
import json

# 返回所有数据
res = requests.get(
    url="https://num.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=75&cityCode=750&advancePayLower=0&sortType=1&goodsNet=4&searchCategory=3&qryType=02&channel=B2C&numNet=186&groupKey=4602051507&judgeType=1&_=1769646521654",
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
)

# 原始的响应体
# print(res.content)
content = res.text[20:-1]
data_dict = json.loads(content)
for num in data_dict['numArray']:
    print(num, type(num))
```

##### 案例：汽车之家

```python
import requests
import json
from bs4 import BeautifulSoup

# gbk编码
res = requests.get(
    url="https://www.autohome.com.cn/news/",
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
)

# 原始的响应体
# print(res.content)
data = res.content.decode('gbk')

# 代表整个HTML区域
soup_object = BeautifulSoup(data, "html.parser")

# 1.寻找到第一个id=auto-channel-lazyload-article的标签
new_area_object = soup_object.find(name='div', attrs={"id":"auto-channel-lazyload-article"})

# 2.在这一步的基础上，寻找他里面所有li标签
li_area_object_list = new_area_object.find_all(name='li')
print(len(li_area_object_list))

# 3.循环每一个li标签，获取它里面的内容
for li_object in li_area_object_list:
    # 在li标签寻找p标签
    p_object = li_object.find(name="p")
    if not p_object:
        continue
    # 获取p标签内部字符串
    print(p_object.text)
    print('=============')
```

#### 1.3.2 BeautifulSoup

```python
from bs4 import BeautifulSoup

soup_object = BeautifulSoup(text,"html.parser")

# 1.寻找到第一个
v1 = soup_object.find(name='div', attrs={"id":"comment"}) # 标签
v2 = v1.find_all(name="li")                 #[标签,标签,标签,标签]

# 2.寻找所有
v3 = soup_object.find_all(name='li', attrs={"id":"x1"}) # #[标签,标签,标签,标签]

# 获取某个标签<h1 id="hello" src="xx" name="lbxx">
v4 = soup_object.find(name='h1', attrs={"id":"hello"}) # 标签
print(v4.text)
print(v4.attrs["src"])
print(v4.attrs["name"])
```

##### 案例：获取汽车之家编辑博客

```python
import requests
import json
from bs4 import BeautifulSoup

# gbk编码
res = requests.get(
    url="https://www.autohome.com.cn/news/",
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
)

data = res.content.decode('gbk')
# 整个HTML字符串
soup_object = BeautifulSoup(data, "html.parser")

# 1.寻找editor-wrap的标签
new_area_object = soup_object.find(name='div', attrs={"class":"editor-wrap"})

# 2.在这一步的基础上，寻找他里面ul标签
ul_area_object_list = new_area_object.find(name='ul')

# 3.在这一步的基础上，寻找他里面所有li标签
li_area_object_list = ul_area_object_list.find_all(name='li')
print(len(li_area_object_list))

# 3.循环每一个li标签，获取它里面的内容
for li_object in li_area_object_list:
    # 在li标签寻找div标签
    div_object = li_object.find(name="div", attrs={"class":"editorname"})
    a_object = div_object.find(name="a")
    if not a_object:
        continue
    # 获取p标签内部字符串
    print(a_object.text)
    print('=============')
```

将图片下载下来

```python
import requests
import os

def download_image(url):
    url = "图片地址"
    
    res = requests.get(
        url=url,
        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
        }
    )
    # 判断file文件是否存在
    if os.path.exists(FILE_PAth):
        os.makedirs(FILE_PATH)
    # 目的是让文件名等于原本的图片名
    file_name = url.rsplit("/", maxsplit=1)[-1]
    file_path = os.path.join(FILE_PATH, file_name)
    with open('a1.jpg', mode='wb') as f:
        f.write(res.content)
        
def run():
    pass
        
if __name__ == '__main__':
    run()
```

### 2 面向对象的概念

- 内部包含了很多值和功能的包裹
- 归类，把同一类打包在一起



- 单元格，对象（值/边框/颜色）
- sheet，对象（名字/很多单元格）
- workbook，对象

#### 2.1 Excel模块

```
pip install openpyxl
```

```python
from openpyxl import load_workbook
import os
# 1.获取work book对象
work_book_object = load_workbook("文件路径")

# 2.读取所有sheet的名字
data_list = work_book_object.sheetnames

print(data_list)

# 3.获取所有sheet对象
v2 = work_book_object.worksheets
print(v2)

# 4.获取某个sheet对象
sheet_object1 = v2[0]
sheet_object2 = work_book_object["数据导出"]
```

- 获取单元格内容

```python
from openpyxl import load_workbook
import os
# 1.获取work book对象
work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

# 2.读取所有sheet的名字
sheet_object_list = work_book_object.worksheets

# 3.获取某个sheet对象
sheet_object = sheet_object_list[0]

# 4.读取sheet中的单元格对象
cell_object = sheet_object.cell(3,1)
cell_object2 = sheet_object["A3"]
row_list = sheet_object[1]

# 5.获取sheet单元格的文本
print(cell_object.value)
print(cell_object2.value)

# 读取某一行
for cell in row_list:
    print(cell.value)

# 读取所有行
for row in sheet_object.rows:
    row_text_list = []
    for cell_object in row:
        row_text_list.append(cell_object.value)
    print(row_text_list)

# 读取某一列
for row in sheet_object.rows:
    cell_object_0 = row[0]
    cell_object_1 = row[1]
    print(cell_object_0.value, cell_object_1.value)
```

- 合并单元格

```python
from openpyxl import load_workbook
import os
# 1.获取work book对象
work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

# 2.读取所有sheet的名字
sheet_object_list = work_book_object.worksheets

# 3.获取某个sheet对象
sheet_object = sheet_object_list[1]

cell_3_object = sheet_object.cell(2,1)
print(cell_3_object)
print(cell_3_object.value)
```

- 判断单元格是否合并

```python
from openpyxl import load_workbook
import os
# 1.获取work book对象
work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

# 2.读取所有sheet的名字
sheet_object_list = work_book_object.worksheets

# 3.获取某一个sheet对象
sheet_object = sheet_object_list[2]

# 4.获取合并的单元格（原始内容）
# for row in sheet_object.rows:
#     text_list = []
#     for cell in row:
#         text_list.append(cell.value)
#     print(text_list)

# 4.获取合并的单元格, 如果是被合并的单元格值默认等于 -
for row in sheet_object.rows:
    text_list = []
    for cell in row:
        if type(cell) == MergedCell:
            text_list.append("-")
        elif type(cell) == Cell:
            # 判断如果cell是Cell对象、MergedCell
            text_list.append(cell.value)
        else:
            text_list.append("不认识")

    print(text_list)
```

- 读取被合并单元格的真实内容

```python
from openpyxl import load_workbook
from openpyxl.cell.cell import Cell, MergedCell

# 1.获取work book对象
work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

# 2.读取所有sheet的名字
sheet_object_list = work_book_object.worksheets

# 3.获取某个sheet对象
sheet_object = sheet_object_list[1]

def get_merged_text(coordinate, sheet_obj):
    # 获取到所有被合并的单元格
    for item in sheet_obj.merged_cells:
        if coordinate in item:
            return item.start_cell.value
        
for row in sheet_object.rows:
    text_list = []
    for cell in row:
        if type(cell) == MergedCell:
            text = get_merged_text(cell.coordinate, sheet_object)
            text_list.append(text)
        elif type(cell) == Cell:
            # 判断如果cell是Cell对象、MergedCell
            text_list.append(cell.value)
        else:
            text_list.append("不认识")

    print(text_list)
```

- 从第n行开始读取

```python
from openpyxl import load_workbook
from openpyxl.cell.cell import Cell, MergedCell
# 1.获取work book对象
work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

# 2.读取所有sheet的名字
sheet_object_list = work_book_object.worksheets

# 3.获取某个sheet对象
sheet_object = sheet_object_list[0]

# 读取第n行
for row in sheet_object.iter_rows(min_row=2):
    print(row[0].value)
```

##### 1.读 

```python
from openpyxl import load_workbook

work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

sheet_object_list = work_book_object.worksheets

sheet_object = sheet_object_list[0]

for row_list in sheet_object.iter_rows(min_row=2):
    row_text = []
    row_text.append(row_list[0].value)
    row_text.append(row_list[3].value)
    row_text.append(row_list[4].value)
    row_text.append(row_list[6].value)
    print(row_text)
```

```python
from openpyxl import load_workbook
import os

folder_path = os.path.join('files', '营收报表')

result = {}

# 1.循环所有的文件
for name in os.listdir(folder_path):
    if not name.startswith("2020"):
        continue

    title = name.rsplit('.', maxsplit=1)[0]
    excel_file_path = os.path.join(folder_path, name)
    # print(title, excel_file_path)

    # 2.打开excel文件
    work_book_object = load_workbook(excel_file_path)

    # 3.获取excel中所有sheet对象
    file_dict = {}
    for sheet_object in work_book_object.worksheets:
        total_count = 0
        for row_list in sheet_object.iter_rows(min_row=2):
            count = row_list[1].value
            if not count:
                continue
            total_count += count
        file_dict[sheet_object.title] = total_count

    # print(title, file_dict)
    result[title] = file_dict

print(result)

```

##### 2.写

- 修改

 ```
 - 读取，所有的内存读取到内存
 - 在内存中修改
 - 保存
 ```

```python
from openpyxl import load_workbook

work_book_object = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

sheet_object = work_book_object.worksheets[0]

cell_object = sheet_object.cell(1,1)

cell_object.value = "序号"

# 将内存中的数据写入文件
work_book_object.save(r"C:\Users\86189\Desktop\Book.xlsx")
```



- 新建

 ```python
 - 读取空内容
 - 在内存中修改操作
 - 保存
 ```

```python
from openpyxl.workbook import Workbook

# 创建Workbook
work_book_object = Workbook()

sheet_object = work_book_object.worksheets[0]

cell_object = sheet_object.cell(1,1)

cell_object.value = "你好"

# 将内存中的数据写入文件,并创建
work_book_object.save(r"C:\Users\86189\Desktop\p2.xlsx")
```

- 创建sheet

```python
from openpyxl.workbook import Workbook

# 默认会生成一个sheet
work_book_object = Workbook()

# 2.默认sheet修改名称
sheet0 = work_book_object.worksheets[0]
sheet0.title = "数据集"
c0 = sheet0.cell(1, 2)
c0.value = "数据传输"

sheet1 = work_book_object.create_sheet("上海", 1)
c1 = sheet1.cell(1,2)
c1.value = '老北京'

sheet2 = work_book_object.create_sheet("北京", 2)
c2 = sheet2.cell(1, 2)
c2.value = "哈哈哈"

# 将内存中的数据写入文件
work_book_object.save(r"C:\Users\86189\Desktop\p2.xlsx")
```

- 删除sheet

```python
import os
from openpyxl import load_workbook

# 获取work book对象
file_path = os.path.join("files", "p1.txt")
wb = load_workbook(file_path)

del wb["用户列表"]

wb.save(file_path)
```

- 循环写入

```python
from openpyxl.styles import Alignment
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# 默认会生成一个sheet
wb = Workbook()

# 2.默认sheet修改名称
sheet0 = wb.worksheets[0]
# 3. 操作
name_list = ['a','b','c','d','e']
for col, text in enumerate(name_list, 1):       # enumerate 枚举
    cell = sheet0.cell(1, col)
    cell.value = text
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True) # wrap_text 自动换行

# 将内存中的数据写入文件
wb.save(r"C:\Users\86189\Desktop\p2.xlsx")
```

- 边框样式与字体

```python
from openpyxl.styles import Alignment, Border, Side, Font
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# 默认会生成一个sheet
wb = Workbook()

# 2.默认sheet修改名称
sheet0 = wb.worksheets[0]
# 3. 操作
cell = sheet0.cell(1,1)
cell.value = "中国人"
cell.font = Font(color="FF0000", size=40, name="微软雅黑")
cell.border = Border(top=Side(style="thin", color="0000FF"),
                     right=Side(style="thin", color="0000FF"),
                     left=Side(style="thin", color="0000FF"),
                     bottom=Side(style="thin", color="0000FF")
                     )

# 将内存中的数据写入文件
wb.save(r"C:\Users\86189\Desktop\p2.xlsx")
```

- 行高和宽

```python
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# 默认会生成一个sheet
wb = Workbook()

# 2.默认sheet修改名称
sheet0 = wb.worksheets[0]
# 3. 操作
sheet0.row_dimensions[1].height = 50
sheet0.row_dimensions[2].height = 50    # 高

sheet0.column_dimensions["A"].height = 80  # 宽

cell = sheet0.cell(1,1)
cell.value = "中国人"
cell.font = Font(color="FF0000", size=20, name="微软雅黑")

# 将内存中的数据写入文件
wb.save(r"C:\Users\86189\Desktop\p2.xlsx")
```

- 背景色填充

```python
from openpyxl.styles import Alignment, Border, Side, Font, GradientFill, PatternFill, Color
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# 默认会生成一个sheet
wb = Workbook()

# 2.默认sheet修改名称
sheet0 = wb.worksheets[0]
# 3. 操作
cell = sheet0.cell(1,1)
cell.value = "中国人"
cell.fill = PatternFill("solid", start_color="F4A460")

# 将内存中的数据写入文件
wb.save(r"C:\Users\86189\Desktop\p2.xlsx")
```

- 合并单元格

```python
from openpyxl import load_workbook

wb = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

sheet = wb.worksheets[0]

cell = sheet.cell(2, 3)
cell.value = "我是中国人"
# 合并单元格，从D2到F8
sheet.merge_cells("D2:F8")
wb.save(r"C:\Users\86189\Desktop\Book.xlsx")
```

- 写入公式

  ```python
  from openpyxl import load_workbook
  from openpyxl.styles import Alignment
  wb = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")
  
  sheet = wb.worksheets[1]
  
  sheet["A1"] = 10
  sheet["A2"] = 20
  
  sheet["B1"] = 2
  sheet["B2"] = 6
  
  # 写入公式
  sheet["C1"] = "=A1*B1"   # 20
  sheet["C2"] = "=A2*B2"   # 120
  wb.save(r"C:\Users\86189\Desktop\Book.xlsx")
  ```

- 删除与插入表格数据

  ```python
  from openpyxl import load_workbook
  
  wb = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")
  sheet_object = wb.worksheets[0]
  
  # 删除 idx表示从哪个地方开始，amount表示往后删除几个
  sheet_object.delete_rows(idx=5,amount=10)
  sheet_object.delete_cols(idx=5,amount=10)
  # 插入
  sheet_object.insert_rows(5,8)
  sheet_object.insert_colsa(5,8)
  
  wb.save(r"C:\Users\86189\Desktop\Book.xlsx")
  ```

- 追加

  ```python
  from openpyxl import load_workbook
  from openpyxl.styles import Alignment
  from openpyxl.workbook import Workbook
  import os
  def write_excel(user, pwd):
      wb = load_workbook(r"C:\Users\86189\Desktop\p2.xlsx")
  
      sheet = wb.worksheets[0]
  
      first_row_data = sheet.cell(1,1).value
      if not first_row_data:
          row_index = 1
      else:
          row_index = sheet.max_row + 1
      sheet.cell(row_index,1).value = user
      sheet.cell(row_index, 2).value = pwd
      wb.save(r"C:\Users\86189\Desktop\p2.xlsx")
  
  def run():
      while True:
          user = input("用户名:")
          pwd = input("密码:")
          write_excel(user, pwd)
  if __name__ == '__main__':
      run()
  ```

  



###### 练习题

- 将文件内容填入表格
- 添加表头，包含用户名，密码，邮箱
- 给表头加上背景色，字体颜色，边框

```python
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Side, Font, GradientFill, PatternFill, Color
from openpyxl.styles.builtins import styles

# 定位到Book.xlsx
wb = load_workbook(r"C:\Users\86189\Desktop\Book.xlsx")

# 定位到Book.xlsx中的第一个sheet
sheet_object = wb.worksheets[0]
border = Border(top=Side(style="thin", color="0000FF"),
                 right=Side(style="thin", color="0000FF"),
                 left=Side(style="thin", color="0000FF"),
                 bottom=Side(style="thin", color="0000FF")
                 )

# 设置宽度
sheet_object.column_dimensions["A"].width = 20
sheet_object.column_dimensions["B"].width = 20
sheet_object.column_dimensions["C"].width = 20

# 以只读的方式打开文件
with open("db.txt", mode="r", encoding="utf-8") as file_db:
    row = 1
    # 循环文件中的内容
    for line in file_db:
        row += 1
        column = 0
        text = line.split(",")
        for item in text:
            column += 1
            # 定位到sheet中的格子
            cell_object = sheet_object.cell(row, column)
            cell_object.border = border
            cell_object.value = item

# 大表头
# 定位第一行   第一列
cell = sheet_object.cell(1, 1)
cell.value = "中国联通"
# 设置字体  字号
cell.font = Font(color="FF0000", size=25, name="微软雅黑")
# 水平垂直对齐
cell.alignment = Alignment(horizontal="center", vertical="center")
#合并单元格
sheet_object.merge_cells("A1:C1")
# 设置行高
sheet_object.row_dimensions[1].height = 50
            
# 添加表头
head_list = ["用户名", "密码", "邮箱"]
column = 0
for item in head_list:
    column += 1
    cell_object = sheet_object.cell(1, column)
    # 给表头加上背景色，字体颜色，边框
    cell_object.font = Font(color="FF0000", size=10, name="微软雅黑")
    cell_object.fill = PatternFill(patternType="solid", start_color="F4A460")
    cell_object.border = border
    cell_object.value = item
wb.save(r"C:\Users\86189\Desktop\Book.xlsx")
```

#### 1.3.2 Word格式

```python
pip install python-docx
```

- .docx,本质上是一个压缩包
- ..docx，底层存储是基于xml格式，python-docx本站上就是xml格式文件

##### 1.读

- 段落对象

- 读取文本

  ```python
  import docx
  
  doc = docx.Document(r"C:\Users\86189\Desktop\2023105010126-陈劲松.docx")
  
  # 段落对象
  p1 = doc.paragraphs[1]
  print(p1.text)
  
  # 获取所有（文本）
  for p in doc.paragraphs:
      print(p.style.name,"--------", p.text)
  
  # 获取段落中所有的runs
  print(p1.runs)
  ```

问题：图片（难）和表格（简+难）无法获取

- 获取图片地址

- word文件的处理与解压

  ```python
  import re
  import docx
  from docx import ImagePart
  
  doc = docx.Document(r"C:\Users\86189\PycharmProjects\python-learn\python入门语法\learning-python\练习\2023105010126-陈劲松.docx")
  
  # 段落对象
  p1 = doc.paragraphs[1]
  print(p1.text)
  
  image_rel_dict = {}
  
  # 获取图片id和图片路径
  for item in doc.part.rels.values():
      if type(item.target_part) == ImagePart:
          # print(item.rId, item.target_part.partname)
          image_rel_dict[item.rId] = item.target_part.partname
  
  for p in doc.paragraphs:
      # print(p.style.name,"--------", p.text)
      # print(p._p.xml)
      if "Graphic" in p._p.xml:
          # 正则表达式获取图片id
          image_id = re.findall(r'<a:blip r:embed="(\w+)"/>', p._p.xml)[0]
          image_path = image_rel_dict[image_id]
          print(image_path)
      else:
          print(p.text)
  ```

- word文件的处理与解压

  ```python
  import os
  import shutil
  
  # 重命名
  file_path = os.path.join("练习", "2023105010126-陈劲松.docx")
  zip_file_path = os.path.join("练习", "demo2.zip")
  
  shutil.copy(file_path, zip_file_path)
  
  # 解压zip文件
  target_folder = os.path.join("练习", "demo2")
  
  shutil.unpack_archive(zip_file_path, target_folder, format='zip')
  ```

- 文本和表格

  ```python
  import docx
  from docx.oxml.table import CT_Tbl
  from docx.oxml.text.paragraph import CT_P
  from docx.table import Table
  from docx.text.paragraph import Paragraph
  
  doc = docx.Document(r"C:\Users\86189\PycharmProjects\python-learn\python入门语法\learning-python\练习\2023105010126-陈劲松.docx")
  
  for p in doc.paragraphs:
      print(p.style.name, "------", p.text)
  
  for t in doc.tables:
      print(t)
  # 循环中间格式数据
  body = doc.element.body
  for child in body.iterchildren():
      if type(child) == CT_Tbl:
          table_obj = Table(child, body)
          print("表格", table_obj)
      elif type(child) == CT_P:
          para_obj = Paragraph(child, body)
          print("表格", para_obj)
  ```

  

##### 2.写入

- 追加，样式

```python
import docx

doc = docx.Document()


p1 = doc.add_paragraph(text="蜡笔小新", style="Heading 1")
# 在段落后面追加
p1.add_run("5岁").font.size = Pt(26)

p2 = doc.add_paragraph(text="中国联通", style="Heading 2")

doc.save('保存的地址')
```



## 2.面向对象

- Python语言
  - 面向过程【不推荐】
  - 函数式【推荐】
  - 面向对象，目的：了解、看懂、研究源码



```python
def func():
    功能代码
    
def something():
    功能代码
    
def run():
    功能代码
    func()
    something()
    
if __name__ == "__main__":
    run()
```



```python
class 类的名字:
    def func(self):
    	功能代码
    
	def something(self):
    	功能代码
    
	def run(self):
        功能代码
```

### 2.1初始面向对象

```python
def send_email(to_email):
    msg = "给{}发送一封邮件".format(to_email)
    print(msg)
    
send_email("2438012849@qq.com")
```



面向对象实现

- 定义类和方法

```python
# 类名
class Message:
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
    
# 根据类名实例化对象
obj = Message()

# 调用方法， 对象.类名(),启动第一个self参数不需要我们传递参数
# - self，是python内部传递，默认会将调用此方法的对象传递进行。obj
# - to_email = "2438012849@qq.com"
obj.send_email("2438012849@qq.com")
```



```python
# 类名
class Message:
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_dingding(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_wechat(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
msg = Message()
msg.send_email("x1")
msg.send_dingdin("x2")
msg.send_wechat("x3")
```



### 2.2 对象是啥

#### **示例1**

```python
class Message:
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_dingding(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_wechat(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
# 实例化Message类的对象
# 1.与它的类关联
# 2.一块内存，可以存放数据
obj = Message()

# self=obj对象  to_email="x1"
obj.send_email("x1")
obj.send_dingding("x2")
```

#### **示例2**

```python
class Message:
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_dingding(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_wechat(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
# 实例化Message类的对象
# 1.与它的类关联
# 2.一块内存，可以存放数据
obj = Message()

obj.company = "联通"
obj.number = 10000

print(obj.company)  # "联通"
print(obj.number)   # "10000"
```

#### **示例3**

```python
class Message:
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
        
    def send_dingding(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
        
    def send_wechat(self, to_email):
    	msg = "给{}发送一封邮件".format(to_email)
    	print(msg)
# 实例化Message类的对象
# 1.与它的类关联
# 2.一块内存，可以存放数据
obj = Message()

obj.company = "联通"
obj.number = 10000

obj.send_email("蜡笔小新")
```

#### **示例4**

```python
class Message:
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
        
    def send_dingding(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
        
    def send_wechat(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
# 实例化Message类的对象
# 1.与它的类关联
# 2.一块内存，可以存放数据
obj = Message()

obj.company = "联通"
obj.number = 10000

obj.send_email("蜡笔小新")

new = Message()
new.company = "移动"
new.number = 100

new.send_email("一拳超人")
```

#### **示例5（重要）**

```python
class Message:
    # 特殊发法,python内部会自动调用,用于实例化对象
    def __init__(self, city):
        self.company = "联通"
        self.city = city
    
    # 在类里定义方法send_email
    def send_email(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
        
    def send_dingding(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
        
    def send_wechat(self, to_email):
    	msg = "给{}的{}发送一封邮件".format(self.company, to_email)
    	print(msg)
        
# 1.创建空对象和空对象和类关联起来
# 2.自动执行__init__方法   obj1.__init__("江西")
obj1 = Message("江西")
obj2 = Messsage("广东")  # obj2.__init__("江西")

obj1.send_email("蜡笔小新")
```

#### **小结**

- 在面向对象中self本质上是一个参数，当前对象是谁调用的，self就指调用的实例化的对象
- 在面向对象 `__init__`发法根据类实例化对象时会自动调用
- 一般情况下，把函数放到类+self参数 = > 方法



#### 案列：用户注册

```python
user_list = []

while True:
    user = input("用户名：")
    if user.upper() == "Q":
        break
    pwd = input("密码：")
    
    info = {"username":user, "password":pwd}
    user_list.append(info)
    
for item in user_list:
    msg = "{} = {}".format(item['username'], item['password'])
    print(msg)
```

```python
class Userinfo():
    def __init__(self, a1, a2):
        self.username = a1
        self.password = a2

user_list = []

while True:
    user = input("用户名：")
    if user.upper() == "Q":
        break
    pwd = input("密码：")
    
    # 实例化对象
    obj = Userinfo(user, pwd)
    user_list.append(obj)
    
for item in user_list:
    msg = "{} = {}".format(item.username, item.password)
    print(msg)
```

#### 案例：警匪游戏

```python
class Police:
    # 警察类
    def __init__(self, name, age, hit_points):
        self.name = name
        self.age = age
        self.hit_points = hit_points
        
        
    def catch(self):
        # 抓小偷
        self.hit_points = self.hit_points + 100
        
    def smoking(self):
        self.hit_points = self.hit_points - 50
        
    def shoot(self, user):
        user.hit_points = user.hit_points - 100
        self.hit_points = self.hit_points - 10
        
p1 = Police("蜡笔小新", 5, 55)
print(p1.hit_points)   # 55
p1.catch()
print(p1.hit_points)   # 155

p2 = Police("一拳超人", 22, 90000)
p2.shoot(p1)
print(p2.hit_points)
print(p1.hit_points)

p3 = Police("普通人", 21, 100)
p3.catch()
p3.smoking()
print(p3.hit_points)     # 150

```



### 2.3 面向对象三大特性



#### 2.3.1 封装

将数据打包在对象中

```python
class Userinfo:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
obj1 = Userinfo("蜡笔小新", 5, "2438012849@qq.com")
```



- 归类，将同一类型的函数，汇总在一个类中：

```python
class Message:
    def email():
        pass
    
    def wechat():
		pass
    
    def dingding():
        pass
    
class fileHandler:
    def txt(self):
        pass
    
    def excel(self):
        pass
    
    def word(self):
        pass
```



#### 2.3.2 继承

子承父业

把公共部分的功能提取到父类中

```python
class Foo:
    pass

class Son(Foo):
    pass
```

```python
class Base:
    def show(self):
        print("123")
        
class F1(Base):
    def do(self):
        pass
    
class F2(Base):
    def exec(self):
        pass
```



##### 实例1

```python
class Base:
    def show(self):
        print("show")
        
class Son(Base):
    def do(self):
        print("do")
        
s1 = Son()

# 1.当前对象是哪个类创建的，优先去哪个类找
s1.do()   # print("do")
s1.show() # 这里的self参数还是s1
```



 ##### 实例2

```python
class Base:
    def do(self):
        print("base.do")
        
class Son(Base):
    def do(self):
        print("do")
        
    def show(self):
        print("show")
        self.do()
        
s1 = Son()
s1.show()
"""
show
do
"""
```



##### 2.3.3 多态

python语言中默认支持多态（多种形态，多种类型）

```python
def func(arg):
    arg.send()
    
# 默认多态
class F1:
    def send(self):
        pass
    
class F2:
    def send(self):
        pass
    
obj1 = F1()
obj2 = F2()
func(obj1)
func(obj2)
```

```java
// 例如其它语言需要标注类型
public void func(String v1){
    
}
func("蜡笔小新")
```



面向对象的三大类型：封装、继承、多态



# 前端开发

## 1 快速开发网站

```python
pip install flack
```

```python
from flask import Flask

app = Flask(__name__)

# 创建了网站 /show/info 和函数 index 的对应关系
@app.route("/show/info")
def index():
    return "中国联通"

if __name__ == "__main__":
    # 让它运行起来
    app.run()
```

- 添加样式

```python
浏览器可以识别标签+数据，列如：
	<h1>中国</h1>                         -> 加大加粗
    <span style='color:red;'>联通</span>  -> 浏览器看见字体变红色
```

- Flack框架支持字符串写入文件里

```python
from flask import Flask, render_template

app = Flask(__name__)

# 创建了网站 /show/info 和函数 index 的对应关系
@app.route("/show/info")
def index():
    # 默认去当前目录的template中找
    return render_template("index.html")

if __name__ == "__main__":
    # 让它运行起来
    app.run()
```

## 2.浏览器能识别的标签




### 2.1 编码

```html
<meta charset="UTF-8">
```

### 2.2 title

```html
<head>
    <meta charset="UTF-8">
    <title>蜡笔小新</title>
</head>
```

### 2.3 标题

```html
<h1>1级标题</h1>
<h2>2级标题</h2>
<h3>3级标题</h3>
<h4>4级标题</h4>
```

### 2.4 div和span

```html
# 独占一行，块级标签
<div>内容</div>
<h1>标题</h1>
<input type="text">

# 自己有多大占多少，行内标签
<span>asdfa</span>
<a></a>
<img src="" />
```

### 2.5 超链接

```html
# 当前页面打开
<a href="跳转网站的网址">点击跳转</a>

# 在新的Tab页面打开
<a href="跳转网站的网址" target="_blank">
	<img src="图片地址" style="width:100px">
</a>
```

### 2.6 图片

```html
<img src="图片地址" />
```

设置图片宽高

```html
<img src="图片地址" style="height:10%; width:20%" />
<img src="图片地址" style="height:100px; width:200px" />
```

### 2.7 列表

```html
<h1>
    运营商列表
</h1>
<ul>
    <li>中国联通</li>
    <li>中国移动</li>
    <li>中国电信</li>
</ul>
```

### 2.8 表格

```html
<table border="1">
    <thead>
    	<tr><th>ID</th> <th>姓名</th> <th>年龄</th></tr>
    </thead>
    <tbody>
    	<tr><td>10</td> <td>蜡笔小新</td> <td>5</td></tr>
        <tr><td>11</td> <td>一拳超人</td> <td>22</td></tr>
    </tbody>
</table>
```

### 2.9 input系列

```html
# 文本框
<input type="text">
# 密码框
<input type="password">
# 文件传输
<input type="file">
# 单选框
<input type="radio" name="n1">男
<input type="radio" name="n1">女
# 多选框
<input type="checkbox">篮球
<input type="checkbox">足球
<input type="checkbox">下棋
# 按钮
<input type="button" value="提交">  -- 普通按钮
<input type="submit" value="提交">  -- 提交表单
```

### 2.10 下拉框

```html
# 单选
<select>
    <option>北京</option>
    <option>上海</option>
    <option>深圳</option>
</select>
# 多选
<select multiple>
    <option>北京</option>
    <option>上海</option>
    <option>深圳</option>
</select>
```

### 2.11 多行文本

```html
<textarea></textarea>
```

### 知识点补充

- 网络请求

  - GET请求【URL/表单提交】

    - 现象：GET请求、跳转、向后台传输数据会拼接在URL上

      ```
      http://www.sogou.com/web?query=安卓&age=19&name=xx
      ```

  - POST请求【表单提交】
    - 现象：提交数据不在URL中，而是在请求体中



### 案例 用户注册

页面上的数据要提交到后台：

- 需要from标签包裹要提交的数据
  - 提交方式：method="get"
  - 提交地址：action="要提交的地址"
  - 在form里必须有submit标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>用户注册</h1>
    <form method="post" action="/post/reg">
        <div>
        用户名:<input type="text" name="user">
        </div>
        <div>
            密码:<input type="password" name="pass">
        </div>
        <div>
        性别:<input type="radio" name="n" value='1'>男  <input type="radio" name="n" value='2'>女
    	</div>
        <input type="button" value="button提交">
        <input type="submit" value="submit提交">
    </form>


</body>
</html>
```

```python
from flask import Flask, render_template, request

app = Flask(__name__)

# 创建了网站 /register 和函数 index 的对应关系
@app.route("/register", methods=['GET'])
def index():
    # 默认去当前目录的template中找
    return render_template("index.html")

@app.route("/do/reg")
def do_register():
    # 1.接收用户通过GET形式发送过来的数据
    print(request.args)
    # 2.给用户返回结果
    return "注册成功"

@app.route("/post/reg")
def post_register():
    # 1.接收用户通过POST形式发送过来的数据
    print(request.form)
    # 2.给用户返回结果
    return "注册成功"

if __name__ == "__main__":
    # 让它运行起来
    app.run()
```

## 3.css样式



### 3.1快速了解

```html
<img src="..." style="height:100px" />
<div style="color:red;">中国联通</div>
```



### 3.2 css应用方法



#### **1.在标签上使用**

```html
<img src="..." style="height:100px" />
<div style="color:red;">中国联通</div>
```



#### **2.在head标签中使用**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            color:red;
        }
    </style>
</head>
<body>
    <h1 class='c1'>用户注册</h1>
    <form method="post" action="/post/reg">
        <div>
        用户名:<input type="text" name="user">
        </div>
        <div>
            密码:<input type="password" name="pass">
        </div>
        <input type="button" value="button提交">
        <input type="submit" value="submit提交">
    </form>
</body>
</html>
```



#### **3.写在文件中**

```css
.c1{
    hight:100px;
}
.c2{
    color:red;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="commend.css">
</head>
<body>
    <h1 class='c1'>用户注册</h1>
    <form method="post" action="/post/reg">
        <div>
        用户名:<input type="text" name="user">
        </div>
        <div>
            密码:<input type="password" name="pass">
        </div>
        <input type="button" value="button提交">
        <input type="submit" value="submit提交">
    </form>
</body>
</html>
```



#### 案例：flask中的应用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>用户注册</h1>
    <form method="post" action="/post/reg">
        <div>
        用户名:<input type="text" name="user">
        </div>
        <div>
            密码:<input type="password" name="pass">
        </div>
        <div>
        性别:<input type="radio" name="n" value='1'>男  <input type="radio" name="n" value='2'>女
    	</div>
        <input type="button" value="button提交">
        <input type="submit" value="submit提交">
    </form>


</body>
</html>
```

```python
from flask import Flask, render_template, request

app = Flask(__name__)

# 创建了网站 /register 和函数 index 的对应关系
@app.route("/register", methods=['GET'])
def index():
    # 默认去当前目录的template中找
    return render_template("index.html")

@app.route("/do/reg")
def do_register():
    # 1.接收用户通过GET形式发送过来的数据
    print(request.args)
    # 2.给用户返回结果
    return "注册成功"

@app.route("/post/reg")
def post_register():
    # 1.接收用户通过POST形式发送过来的数据
    print(request.form)
    # 2.给用户返回结果
    return "注册成功"

if __name__ == "__main__":
    # 让它运行起来
    app.run()
```

### 3.3 选择器

- ID选择器

```html
#c1{
	
}

<div id='c1'>
    lbxx
</div>
```

- 类选择器(常用)

```html
.c1{

}

<div class='c1'>xxx<div>
```

- 标签选择器

```html
div{

}

<div>
    xxx
</div>
```

- 属性选择器

```html
input[type='text']{
	border:1px;
}
.v1[xx='234']{
	color:gold;
}

<input type="text">
<input type="password">

<div class="v1" xx="234">
    属性选择器
</div>
```

- 子类选择器

```html
.yy li{
	color:pink;
}

<div class="yy">
    <ul>
        <li>变成pink色</li>
    </ul>
    <a>不变色</a>
</div>
```

关于多样式覆盖问题，如果样式有重复，取首个

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            color: red;
        }
        .c2 {
            height: 50px;
        }
    </style>
</head>
<body>
    <div class="c1 c2">
        中国联通
    </div>
</body>
</html>
```

### 3.4 样式

#### 1 高度和宽度

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            height:100px;
         	width:200px;	
        }
        .c2 {
            height: 50px;
            width:50%;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>


</body>
</html>
```

注意事项：

- 宽度支持百分比，高度不支持
- 行内标签：默认无效
- 块级标签：默认有效（多余的空白区域也不给你用）

#### 2 块级和行内标签

- css样式：标签 --> display: inline-block      将两个标签中和一下

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            display: inline-block;
            height: 50px;
            width:50%;
        }
        .c2 {
            height: 50px;
            width:50%;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>
	<span class="c1">
    	哈哈
    </span>
    <div style="display: inline;">
        可以修改，行内同理
    </div>
</body>
</html>
```

#### 3 字体

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            color:green;
            font-size:44px;
            font-weight:700;
            font-family:Microsoft Yahei
        }
        .c2 {
            height: 50px;
            width:50%;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>
	
</body>
</html>
```



#### 4 文字的对齐方式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            height: 50px;
            width:50px;
            color:green;
            border:1px solid red;
            text-alige:center;
            line-heiget:50px;
        }
        .c2 {
            height: 50px;
            width:50%;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>
	
</body>
</html>
```



#### 5 浮动

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
    <span>左边</span>
	<span style="float:right;">右边</span>
</body>
</html>
```

div默认是块级标签，如果浮动起来，会变成类似行内标签，但会脱离文档流



#### 6 内边距

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            height: 50px;
            width:50px;
            color:green;
            border:1px solid red;
            padding-top:10px;
            padding-left:10px;
            padding-right:10px;
            padding-bottom:10px;
        }
        .c2 {
            height: 50px;
            width:50%;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>
	
</body>
</html>
```



#### 7 外边距

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1 {
            height: 50px;
            width:50px;
            color:green;
            border:1px solid red;
            margin:10px 10px 20px 10px;
        }
        .c2 {
            height: 50px;
            width:50%;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>
	
</body>
</html>
```

#### 8 hover

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1:hover {
            height: 50px;
            width:50px;
            color:green;
            border:1px solid red;
            margin:10px 10px 20px 10px;
        }
    </style>
</head>
<body>
    <div class="c1">
        中国
    </div>
	
</body>
</html>
```

#### 8 after

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .area:after {
            content:"";
            display:block;
            clear:both;
            visibility:hidden;
        }
        .item{
            float:left;
        }
    </style>
</head>
<body>
    <div class="area">
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
    </div>
	
</body>
</html>
```

#### 9 position

##### 1 fixed

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .back{
            position: fixed;
            width:60px;
            height:60px;
            border: 1px solid red;
            right: 10px;
            bottom: 50px;
        }
    </style>
</head>
<body>
    
    <div class="back">
        
    </div>
	
</body>
</html>
```

案例：对话框

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
        }
        .dialog{
            position:fixed;
            height:300px;
            width:500px;
            background-color:red;
            
            left: 400px;
            top: 200px;
            margin:0 auto;
            z-index:1000;
        }
        .mask{
            background-color:black;
            position:fixed;
            left:0;
            right:0;
            top:0;
            bottom:0;
            opacity:0.7;
            z-index:999;
        }
    </style>
</head>
<body>
    <div style="height:1000px;"></div>
    <div class="mask"></div>
	<div class="dialog"></div>
</body>
</html>
```

## 4 BootStrap

是别人已经帮我们写好的css样式，，如果我们想使用要下载BootStrap

- 下载BootStrap

- 使用

  - 在页面上引入BootStrap
  - 编写HTML时，按照BootStrap的规定来编写+自定制

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <-- 引入bootstrap文件 -->
      <link rel="stylesheet" href="static/plugins/bootstrap框架/css/bootstrap.min.css">
  </head>
  <body>
      <input type="button" value="提交" class="btn btn-primary">
  	<input type="button" value="提交" class="btn btn-success">
  </body>
  </html>
  ```

### 4.1 导航栏

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="static/plugins/bootstrap框架/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: antiquewhite;">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Dropdown
                </a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Another action</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
                </li>
                <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                </li>
            </ul>
            <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            </div>
        </div>
    </nav>
</body>
</html>
```

## 5 JavaScript

### 5.1 代码位置

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
	<script type="">
    	// 编写Javascript代码
    </script>
</head>
<body>
    <script></script>
</body>
</html>
```

### 5.2 变量

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
	
</head>
<body>
    <script type="text/javascript">
    	var name = '蜡笔小新'
        console.log(name);
    </script>
</body>
</html>
```

### 5.3 字符串类型

```js
// 声明
var name = "蜡笔小新";
var name = String("蜡笔小新")
```

```js
// 常见功能
var name = "中国联通"

var v1 = name.length;
var v2 = name[0];
var v3 = name.trim();
var v4 = name.substring(0,2); //前取后不取
```

### 案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
	<script type="">
    	// 编写Javascript代码
    </script>
</head>
<body>
    <span id="txt">欢迎蜡笔小新到来</span>
    <script>
        function show(){
            //获取到内容
            var tag = document.getElementById("txt");
            var dataString = tag.innerText;

            var firstChar = dataString[0];
            var otherString = dataString.substring(1,dataString.length)
            var newText = otherString + firstChar;
            // 写入页面
            tag.innerText = newText
        }
        // 每秒执行一次show的函数
        setInterval(show, 1000);
    </script>
</body>
</html>
```

### 5.4 数组

```js
var v1 = [11,22,33,44];
var v2 = Array([11,22,33,44]);
```

```js
var v1 = [11,22,33,44];

v1[1]
v1[0] = "蜡笔小新";

v1.push("联通");  // 尾部追加
v1.unshift("联通") // 头部追加
v1.splice(索引位置,0,元素)；
v1.splice(1,0,"中国") // [11,"中国",22,33,44]

v1.pop() //尾部删除
v1.shift() // 头部删除
v1.splice(2,1);  // 索引为2的元素删除[11,22,44]
```

```js
var v1 = [11,22,33,44];
for(var i=0; i<v1; i++){
    
}
```

#### 案例 动态数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
    <ul id="city">
        
    </ul>
    <script>
		var cityList = ["北京","上海","深圳"];
        for(var idx in cityList){
            var text = cityList[idx]
            
            //创建 <li>标签
            var tag = document.creatElement("li")
            // 在li标签里写入内容
            tag.innerText = text;
            
            // 添加id = city那个标签的里面。DOM
            var patentTag = document.gatElementById("city");
            parentTag.appendChild(tag);
        }
    </script>
</body>
</html>
```

### 5.5 对象（字典）

```js
info = {
    name:"蜡笔小新",
    age:18
}
```

```js
info.name = "lbxx"
info['age']
for(var key in info){
    // key=name/age
}
```

#### 案例：动态表格 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>年龄</th>
            </tr>
        </thead>
        <tbody id="body">

        </tbody>
    </table>
    <script type="text/javascript">
        var info = {id:1, name:"蜡笔小新", age:5};
        var tr = document.createElement('tr');
        for(var key in info){
            var text = info[key];
            var td = document.createElement('td')
            td.innerText = text;
            tr.append(td)
        }
        var bodyTag = document.getElementById('body')
        bodyTag.appendChild(tr)
    </script>
</body>
</html>
```



### 5.6 条件语句

```js
if (条件){
    
}else{
    
}

if (1=1){
    
}else{
    
}
```

```js
if(条件){
    
}else if(条件){
    
}else if(条件){
    
}else{
    
}
```

### 5.7 函数

```python
def func():
    函数内容....
func()
```

```js
function func(){
    函数内容....
}
func()
```

## 3.DOM

DOM就是一个模块，可以对HTML页面中的标签进行操作

```javascript
// 根据ID获取标签
var tag = document.getElementById("xx");

// 获取标签文本
tag.innerText

// 修改标签中的文本
tag.innerText = "哈哈哈哈";
```

```javascript
// 创建标签
var tag = document.createElement("div");

// 标签内容
tag.innerText = "哈哈哈哈"
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
    <ul id="city">
        
    </ul>
    <script>
		var tag = document.getElementById("city");
        
        // <li>北京</li>
        var newTag = document.createElementById("li");
        newTag.innerText = "北京";
        tag.appendChild(newTag);
    </script>
</body>
</html>
```

## 4.jQuery

jQuery是一个JavaScript第三方模块

- 基于jQuery，开发功能
- 现成的工具 列如：JavaScript的动态效果

### 4.1用jQuery寻找标签

- ID选择器

```html
<body>
    <h1 id="txt"> 中国联通</h1>

    <script src="jQuery/jquery-4.0.0.js"></script>
    <script>
        $("#txt").text("广西联通");
        // document.getElementById('txt').innerText = "广西联通"
    </script>
</body>
```

- 样式选择器

```html
<body>
    <h1 class="txt"> 中国联通</h1>

    <script src="jQuery/jquery-4.0.0.js"></script>
    <script>
        $(".txt").text("广西联通");
    </script>
</body>
```

- 标签选择器

```html
<body>
    <h1 class="txt"> 中国联通</h1>

    <script src="jQuery/jquery-4.0.0.js"></script>
    <script>
        $("h1").text("广西联通");
    </script>
</body>
```

- 多选择器

```html
<body>
    <h1 class="txt1"> 中国联通</h1>
	<h2 class="txt2"> 中国联通</h2>
    <script src="jQuery/jquery-4.0.0.js"></script>
    <script>
        $("h1,#txt2").text("广西联通");
    </script>
</body>
```

- 属性选择器

```html
<input type='text' name="n1" />
<input type='text' name="n1" />
<input type='text' name="n2" />
<script src="jQuery/jquery-4.0.0.js"></script>
<script>
        $("input[name='n1']");
</script>
```



### 4.2 间接寻找

- 找到上一个兄弟

```html
<body>
    <div>
        <div>北京</div>
        <div id='c1'>上海</div>
        <div>深圳</div>
    </div>

    <script src="jQuery/jquery-4.0.0.js"></script>
    <script>
        $("#c1").prev();  //找到上一个
        $("#c1").next();  //找到下一个
        $("#c1").next().next();  //找到下一个
        $("#c1").siblings(); //找到所有
    </script>
</body>
```

- 找父子

```html
<body>
    <div id='head'>
        <div>北京</div>
        <div id='c1'>上海</div>
        <div>深圳</div>
    </div>

    <script src="jQuery/jquery-4.0.0.js"></script>
    <script>
        $("#c1").parent();          //找到父级
        $("#c1").parent().parent(); //找到父级的父级
        $("#head").children();      //找到所有的孩子
        $("#head").children("#c1"); //找到所有的孩子
        $("#head").find("#c1");     //找到所有的子孙带有“c1”id的
    </script>
</body>
```

### 案例：菜单切换

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .menus{
            width: 200px;
            height: 800px;
            border: 1px solid red;
        }
        .menus .header{
            background-color: aqua;
            padding: 10px 5px;
            cursor: pointer;
        }
        .menus .content a{
            display: block;
            padding: 5px 5px;
            border-bottom: 1px dotted #dddddd;
        }
        .hide{
            display: none;
        }

    </style>
</head>
<body>
    <div class="menus">
        <div class="item">
            <div class="header" onclick="clickMe(this)">上海</div>
            <div class="content hide">
                <a>1区</a>
                <a>2区</a>
                <a>3区</a>
                <a>4区</a>
            </div>
        </div>
        <div class="item">
            <div class="header" onclick="clickMe(this)">b北京</div>
            <div class="content hide">
                <a>1区</a>
                <a>2区</a>
                <a>3区</a>
                <a>4区</a>
            </div>
        </div>
    </div>
    <script src="static/jQuery/jquery-4.0.0.js"></script>
    <script>
        function clickMe(self){
            $(self).next().removeClass("hide")

            $(self).parent().siblings().find(".content").addClass("hide")

            // var hasHide = $(self).next().hasClass("hide")
            // if(hasHide){
            //     $(self).next().removeClass("hide")
            // }else{
            //      $(self).next().addClass("hide")
            // }  
        }
    </script>
</body>
</html>
```

### 4.3操作样式

- addClass
- removeClass
- hasClass

### 4.4 值的操作

```html
<div id='c1'>
    内容
</div>
```

```javascript
$("#c1").text()
$("#c1").text("休息")  //获取文本内容
```



```html
<input type='text' id='c2' />
```

```javascript
$("#c2").val()           // 获取用户输入的值
$("#c2").val("哈哈哈")    // 设置值
```

### 案例：动态创建数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <input type="text" id="txtUser" placeholder="用户名">
    <input type="text" id="txtEmail" placeholder="邮箱">
    <input type="button" value="提交" onclick="getInfo()">
    <ul id="view">

    </ul>
    <script src="static/jQuery/jquery-4.0.0.js"></script>
    <script>
        function getInfo(){
            // 1.获取用户名和密码
            var username = $("#txtUser").val();
            var email = $("#txtEmail").val();

            var dataString = username + "-" + email

            // 2.创建li标签
            var newLi = $("<li>").text(dataString);
            
            $("#view").append(newLi);
        }
    </script>
</body>
</html>
```



### 4.5 事件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <ul>
        <li>百度</li>
        <li>蜡笔小新</li>
    </ul>
    <script src="static/jQuery/jquery-4.0.0.js"></script>
    <script>
        $(function(){
            // 当页面框架加载完成之后，自动执行
        })
        
        $("li").click(function(){
            // 点击li标签时，执行这个函数
            var text = $(this).text()
            console.log(text)
        })
    </script>
</body>
</html>
```

在jQuery中删除标签

```html
<div id='c1'>
    内容
</div>
<script>
	$("#c1").remove()
</script>
```

### 4.6 表格

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>操作</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>蜡笔小新</td>
                <td>
                    <input type="button" value="删除" class="delete">
                </td>
            </tr>
            <tr>
                <td>2</td>
                <td>超人</td>
                <td>
                    <input type="button" value="删除" class="delete">
                </td>
            </tr>
        </tbody>
    </table>
    <script src="static/jQuery/jquery-4.0.0.js"></script>
    <script>
        $(function(){
            //找到所有class=delete的标签
            $(".delete").click(function(){
                $(this).parent().parent().remove()
            })
        })
    </script>
</body>
</html>
```



## 5 前端整合

- HTML
- CSS
- JaveScript
- BootStrap(动态效果依赖jQuery)



# MySQL

- Python相关：基础、函数、数据类型、面向、模块
- 前端开发：HTML、CSS、JavaScript、jQuery【静态页面】

```
Java+前端；  Python+前端；  Go+前端；  ->  【动态页面】
```

直观：

- 静态：写死了，页面永远长一个样子
- 动态：页面上的数据可以实时修改和展示

## 1.初识网站

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/plugins/bootstrap3.4.1/css/bootstrap.css">
    <title>Document</title>
    <style>
        .navbar {
            border-radius: 0%;
        }
    </style>
</head>

<body>

    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-9" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-9">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Home</a></li>
                    <li><a href="#">Link</a></li>
                    <li><a href="#">Link</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">One more separated link</a></li>
                        </ul>
                    </li>
                </ul>
                
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">登录</a></li>
                    <li><a href="#">注册</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">蜡笔小新 <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">个人资料</a></li>
                            <li><a href="#">我的账户</a></li>
                            <li><a href="#">修改密码</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">注销</a></li>
                        </ul>
                    </li>
                </ul>
                
            </div><!-- /.navbar-collapse -->

        </div><!-- /.container-fluid -->
    </nav>


    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-2.2.4.min.js"></script>
    <script src="static/plugins/bootstrap3.4.1/js/bootstrap.js"></script>

</body>

</html>
```

### 1.1 Flask

```python
# 1. 从flask库导入核心类Flask（创建应用）和render_template（渲染HTML模板）
from flask import Flask, render_template

# 2. 创建Flask应用实例，__name__是Python内置变量，代表当前脚本的模块名，Flask会用它定位模板/静态文件
app = Flask(__name__)

# 3. 定义路由：当用户访问 http://localhost:5000/index 时，执行下面的index函数
@app.route("/index")
def index():
    # 4. 渲染templates目录下的index.html文件并返回给浏览器
    return render_template("index.html")

# 5. 只有直接运行该脚本时，才启动Flask开发服务器
if __name__ == '__main__':
    # 6. 启动服务器，默认地址是127.0.0.1，端口5000
    app.run()
```



## 2.MySQL安装

### 1.补丁

```
vcredist_x64.exe              dxwebsetup.exe
```



### 2.配置文件

- 创建在C:\Program Files\MySQL\MySQL Server 8.0目录下，名字是my.ini
- 修改配置文件需要停掉服务，重启MySQL

```
[mysqld]

# port
port=3306

# set basedir to your installation path
basedir=C:\\Program Files\\MySQL\\MySQL Server 8.0

# set datadir to the location of your data directory
datadir=C:\\Program Files\\MySQL\\MySQL Server 8.0\\data
```



### 3.初始化

- 以管理员权限运行命令行

```
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqld.exe" --initialize-insecure
```

- 执行初始化后在MySQL Server 8.0中生成data文件，表示初始化成功



## 3.启动MySQL

- 临时启动

```
C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqld.exe
```

- 制作成Windows服务，服务来进行开启与关闭

```
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqld.exe" --install mysql80
```



##　４.连接测试

- 用MySQL自动工具连接MySQL并发送指令

```
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -h 127.0.0.1 -P 3306 -u root -p
```

## 5 数据库指令

- 修改密码

```mysql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
```

- 然后执行刷新权限

```mysql
FLUSH PRIVILEGES;
```

- 查看已有文件夹

```mysql
show databases;
```

- 创建数据库（文件夹）

```mysql
create database 数据库名称 default charset utf8 collate utf8_general_ci;
```

- 删除数据库(文件夹)

```mysql
drop database 已有数据库名称;
```

- 进入数据库(文件夹)

```mysql
use 数据库名称;
```

- 查看当前数据库的数据表（文件）

```mysql
show tables;
```

- 创建表

```mysql
create table 表名称(
	列名称 类型,
	列名称 类型,
	列名称 类型
)default charset=utf8;
```

```mysql
create table tbl(
	id int,           
	name varchar(16) not null,  -- 不允许为空
	age int null                -- 应许为空
)default charset=utf8;
```

```mysql
create table tbl(
	id int primary key,         -- 主键不可为空           
	name varchar(16) not null,  
	age int default 3           -- 不赋值，默认为3    
)default charset=utf8;
```

```mysql
create table tbl(
	id int auto_increment primary key,   -- 内部维护，自增           
	name varchar(16) not null,  
	age int  
)default charset=utf8;
```

标准表的创建

```mysql
create table tbl(
	id int auto_increment primary key,          
	name varchar(16),  
	age int  
)default charset=utf8;
```

- 新增表数据

```mysql
insert into 表名 (列名，列名) values (值,值), (值,值);
```

- 删除表数据

```mysql
delete from 表名 where 条件;
delete from tbl where id = 3;
```

- 修改数据

```mysql
update 表名 set 列=值,列=值;
update 表名 set 列=值 where 条件;
update tbl set age=18 where id > 5;
```

- 查询数据

```mysql
select * from 表名称;
select 列名称,列名称 from 表名称;
select 列名称,列名称 from 表名称 where 条件;
```

- 查看表结构

```mysql
desc 表名称;
```

- 删除表

```mysql
drop table 表名称;
```



- 退出

```mysql
exit;
```



- 在MySQL和我们平时认知不同的概念

| MySQL  | 认知   |
| ------ | ------ |
| 数据库 | 文件夹 |
| 数据表 | 文件   |

常用数据类型

- tinginy

```mysql
有符号，取值范围：-128~127
无符号，取值范围：0~255
```

```mysql
create table tbl(
	id int auto_increment primary key,          
	name varchar(16),  
	age tinyint unsigned               -- 无符号
)default charset=utf8;
```

```mysql
create table tbl(
	id int auto_increment primary key,          
	name varchar(16),  
	age tinyint                        -- 有符号
)default charset=utf8;
```

- int

```mysql
int             表示有符号
int unsigned    表示无符号
```

- bigint

```
int的加强版
```

```mysql
# 创建表
create table tb2(
	id int not null auto_increment primary key,          
	salary int,  
	age tinyint                        
)default charset=utf8;

# 插入数据
insert into tb2(salary,age) values(10000,18);
insert into tb2(salary,age) values(10000,28);
insert into tb2(salary,age) values(10000,38),(40000,40);

# 查看表中的数据
select * from tb2;
```

- float
- double
- decimal

```mysql
# m(8)是数字总个数，d(2)是小数点后的个数，m最大值是65，d的最大值是30
create table tb2(
	id int not null auto_increment primary key,          
	salary decimal(8,2),                          
)default charset=utf8;
```

- char

```mysql
定长字符串，最大255个字符
char(11) 固定用11个字符串存储，没有11也按照11存储
create table tb4(
	id int not null auto_increment primary key,          
	mobile char(11),                          
)default charset=utf8;
```

- varchar

```mysql
变长字符串    最大字节/3
varchar(11) 小于11按照实际字符串大小来存储
create table tb4(
	id int not null auto_increment primary key,          
	mobile varchar(11),                          
)default charset=utf8;
```

- text

```mysql
text用于保存变长字符串，最多2**16-1个字符，用于新闻和长文本
create table tb5(
	id int not null auto_increment primary key,          
	mobile varchar(11),    
    content text
)default charset=utf8;
```

- mediumtext

```
2**24-1
```

- longtext

```
2**32-1
```

- datatime

```
yyyy-mm-dd HH:MM:SS
```

- date

```
yyyy-mm-dd
```

练习题：

```mysql
create table tb7(
	id int not null auto_increment primary key, 
    name varchar(64) not null,
	password varchar(64) not null,    
    email varchar(64) not null,
    age tinyint,
    salary decimal(10,2),
    ctime datetime
)default charset=utf8;

insert into tb7(name,password,email,age,salary,ctime) values("蜡笔小新","123","xx@qq.com",5,6465.4,"2026-3-15 10:04:55");
```

## 6 案例：员工管理

### 6.1 创建表结构

```mysql
create database unicom default charset utf8 collate utf8_general_ci;

use unicom;

create table admin(
	id int not null auto_increment primary key,
    username varchar(16) not null,
    password varchar(64) not null,
    mobile char(11) not null
)default charset=utf8;
```

### 6.2 Python操作MySQL

安装模块

```
pip install pymysql
```

```python
import pymysql

# 1 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2 发送指令
cursor.execute("insert into admin(username,password,mobile) values('lbxx','123','13284756623')")
conn.commit()                                    # 执行 conn.commit()，就是点击 “保存”，把草稿箱里的操作真正生效到数据库中

# 3 关闭
cursor.close()
conn.close()
```

#### 1 创建数据库

```python
import pymysql

while True:
    user = input("用户名:")
    if user.upper() == 'Q':
        break
    pwd = input("密码:")
    mobile = input("手机号:")

    # 1 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)# 创建游标对象（执行SQL的工具），指定返回结果为字典格式

    # 2 发送指令
    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql,[user, pwd, mobile])
    conn.commit()

    # 3 关闭
    cursor.close()
    conn.close()
```

#### 2 查询数据

```python
import pymysql


# 1 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2 发送指令
sql = "select * from admin"
cursor.execute(sql)
# 3. 获取所有查询结果（核心：fetchall()的作用）
data_list = cursor.fetchall()
for row_dict in data_list:
    print(row_dict)

# 4 关闭
cursor.close()
conn.close()
```

#### 3 删除数据

```python
import pymysql


# 1 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2 发送指令
sql = "delect from admin where id=%s, [3, ]"
cursor.execute(sql)
conn.commit()
# 3 关闭
cursor.close()
conn.close()
```

#### 4 修改数据

```python
import pymysql


# 1 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2 发送指令
sql = "update admin set mobile=%s where id=%s, ['24435324623', 1]"
cursor.execute(sql)
conn.commit()
# 3 关闭
cursor.close()
conn.close()
```

#### 5 HTML与数据库与python结合

```python
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    username = request.form.get("user")
    password = request.form.get("pwd")
    mobile = request.form.get("mobile")

    # 1 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2 发送指令
    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql,[username, password, mobile])
    conn.commit()

    # 3 关闭
    cursor.close()
    conn.close()


    return "添加成功"

if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post" action="/index">
        <input type="text" name="user" placeholder="用户名">
        <input type="text" name="pwd" placeholder="密码">
        <input type="text" name="mobile" placeholder="手机号">
        <input type="submit" value="提交">
    </form>
</body>
</html>
```



# Django

- Python知识点：函数、面向对象
- 前端开发：HTML、JavaScript、JQuery、BootStrap
- MySQL数据库
- Flask，短小精悍 + 第三方组件
- Django，内部以集成很多组件 + 第三方组件

## 1.安装django

```
pip install django
```

```
C:\python
	- pyhton.exe
	- Scripts
		- pip.exe
		- django-admin.exe
    - Lib
    	- 内置模块
    	- site-package
    		- openpyxl
    		- python-docx
    		- flask
    		- django
```

## 2.创建项目

- 打开终端
- 进入某个目录

```
C:\Users\86189\Desktop\study
```

- 执行命令创建目录   命令行创建是准确的

```
"C:\python\Scripts\django-admin.exe" startproject 项目名称
```

- 创建数据表

```
python manage.py migrate
```



默认项目文件介绍

```
djangostudy
	- manage.py    【项目的管理、启动、创建app、数据管理】  【不要动】  【常常用】
	- djangostudy   
		- __init__.py
		- setting.py          【项目配置】           【常常修改】
		- urls.py             【url和函数的对应关系】  【常常修改】
		- asgi.py             【接收网络请求】    【不要动】
		- wsgi.py             【接收网络请求】    【不要动】
```

## 3.App

```
- 项目
	- app，用户管理  【表结构、函数、HTML模板、CSS】
	- app，订单管理  【表结构、函数、HTML模板、CSS】
	- app，后台管理  【表结构、函数、HTML模板、CSS】
	- app，网站     【表结构、函数、HTML模板、CSS】
	- app，API     【表结构、函数、HTML模板、CSS】
```

### 3.1创建应用

- 需要先进入这个项目子文件夹，再执行命令

```
python manage.py startapp app01
```



## 4.快速上手

- 确保app已经注册 【setting.py】

![image-20260317110017599](assets/image-20260317110017599.png)

- 编写URL和视图函数的对应关系【urls.py】

![image-20260317110403972](assets/image-20260317110403972.png)

- 编写视图函数

![image-20260317110707763](assets/image-20260317110707763.png)

- 启动django项目

  - 命令行启动

  ```
  python manage.py runserver4.1 页面
  ```


### 4.1 页面

```
- url  -> 函数
- 函数
```

![image-20260318084326917](assets/image-20260318084326917.png)

### 4.2 templates目录

![image-20260318085831589](assets/image-20260318085831589.png)

### 4.3 静态文件

在开发过程中一般将：

- 图片
- CSS
- JS

当作静态文件处理



#### 4.3.1 static

在app目录下创建static

![image-20260318094218796](assets/image-20260318094218796.png)

#### 4.3.2 引用静态文件

![image-20260318094523285](assets/image-20260318094523285.png)

## 5 模板语法

本质上：在HTML中写一些占位符，有数据对这些占位符进行替换和处理



## 新闻

![image-20260318113604687](assets/image-20260318113604687.png)

![image-20260318113627541](assets/image-20260318113627541.png)

![image-20260318113642357](assets/image-20260318113642357.png)

## 6.请求和响应

![image-20260319084321241](assets/image-20260319084321241.png)

### 6.1登入验证

![image-20260319084514575](assets/image-20260319084514575.png)

## 7.数据库操作

- MySQL数据库+pymysql

```python
import pymysql

# 1 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2 发送指令
cursor.execute("insert into admin(username,password,mobile) values('lbxx','123','13284756623')")
conn.commit()                                    # 执行 conn.commit()，就是点击 “保存”，把草稿箱里的操作真正生效到数据库中

# 3 关闭
cursor.close()
conn.close()
```

- Django开发操作数据库更简单，内部提供了ORM框架

### 7.1安装第三方模块

```
pip install mysqlclient
```

### 7.2 ORM

ORM可以帮我们做两件事

- 创建、修改、删除数据库中的表
- 操作表中的数据

#### 1.创建数据库

- 启动MySQL服务
- 自带工具创建数据库

```mysql
create database 数据库名称 default charset utf8 collate utf8_general_ci;
```

#### 2.django连接数据库

```mysql
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "gd_day15",
        "USER": "root",
        "PASSWORD": "root123",
        "HOST": "127.0.0.1",
        "PORT": 3306,
    }
}
```

#### 3.django操作表

- 创建models.py

```mysql
python manage.py startapp myapp
```

- 创建表
- 删除表
- 修改表

在models.py文件中：

```python
from django.db import models

# Create your models here.

# 类名代表数据库中的表名，类下面的字段名代表数据库中的列名
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.ImageField()

"""
create table app01_userinfo(
    name varchar(32),
    password varchar(64),
    age int
)
"""
```

在cmd操作面板执行命令

```python
# 安装 Pillow 库（如果你确实需要存储图片）
python -m pip install Pillow

# makemigrations = 写草稿（记录模型变更），migrate = 执行草稿（真正创建 / 修改数据库表）
python manage.py makemigrations
python manage.py migrate

# 1. 生成迁移文件（检测模型变更）
python manage.py makemigrations app01

# 2. 执行迁移，同步到数据库
python manage.py migrate app01
```

注意：app需要提前注册

![image-20260319095029443](assets/image-20260319095029443.png)

在表中新增列时，由于已经存在的列表中可能存在数据，所有新增列必须要指定对应数据

- 手动输入一个指

- 在models.py中设置默认值

```python
size = models.IntegerField(default=2)
```

- 在models.py中设置应许为空

```python
data = models.IntegerField(null=True, blank=True)
```



#### 4.django操作表中的数据

- 在views.py中添加

```python
表名称.objects.create(列名称="销售部", .....)
```

- 在views.py中删除

```python
表名称.objects.filter(筛选条件).delete()
表名称.objects.filter(id=2).delete()

表名称.objects.all().delete()
```

- 在views.py中获取数据

```python
# data_list = [对象, 对象, 对象]  QUerySet类型
data_list = 表名称.objects.all()
for obj in data_list:
    print(obj.id, obj.name, obj.age)
    
# 获取指定数据
data_list1 = 表名称.objects.filter(id=1)
```

- 在views.py中更新数据

```python
表名称.objects.filter(筛选条件).updata(password=555)

表名称.objects.all().updata(password=555)
```

### 员工管理系统

#### 1.新建项目

```
C:\python\Scripts\django-admin.exe" startproject djangoEmployee
```

```
python manage.py startapp app01
```

![image-20260321095135908](assets/image-20260321095135908.png)

#### 2.设计表结构

```python
from django.db import models

# Create your models here.
class Department(models.Model):
    # 部门表
    id = models.BigAutoField(verbose_name='ID', primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=32)

class UserInfo(models.Model):
    # 部门表
    name = models.CharField(verbose_name='名字', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=32)
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
```

#### 3.MySQL生成表

```
create database gd_day16 default charset utf8 collate utf8_general_ci;
```

![image-20260321110447217](assets/image-20260321110447217.png)

- django命令生成数据表

```
python manage.py makemigrations
python manage.py migrate
```

#### 4.静态文件管理

![image-20260322090624158](assets/image-20260322090624158.png)

#### 5.部门管理

- urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
]
```

- views.py处理

```python
from django.shortcuts import render, redirect
from app01 import models
# Create your views here.
def depart_list(request):

    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {"depart_list": queryset})

def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    # 获取用户输入信息
    title = request.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向会部门列表
    return redirect("/depart/list/")

def depart_delete(request):
    # http://127.0.0.1:8000/depart/delete/?nid=1
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")

def depart_edit(request, nid):
    # 根据id，获取他的数据[obj, ]
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        print(row_object.id, row_object.title)
        return render(request, 'depart_edit.html', {"row_object":row_object})
    
    # 获取用户提交的标题
    title = request.POST.get("title")
    # 根据id找数据库的数据进行更新
    models.Department.objects.filter(id=nid).update(title=title)
    # 重定向
    return redirect("/depart/list/")
```

- 部门列表

```html
<!-- 核心作用是加载 Django 内置的 static 模板标签库，让你能在 HTML 模板中便捷、规范地引用项目里的静态文件 -->
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap3.4.1/css/bootstrap.css' %}">
</head>

<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li><a href="/depart/list">部门管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">登入</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">蜡笔小新· <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">个人资料</a></li>
                            <li><a href="#">我的信息</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">注销</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>

    <div class="container">
        <div>
            <!-- 在新页面打开 target="_blank" -->
            <a class="btn btn-primary" href="/depart/add/" style="margin-bottom:10px" target="_blank">新建部门</a>
        </div>

        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                部门列表
            </div>

            <!-- Table -->
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>名称</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in depart_list %}
                        <tr>
                            <th scope="row">{{obj.id}}</th>
                            <td>{{obj.title}}</td>
                            <td>
                                <a class="btn btn-primary btn-xs" href="/depart/{{obj.id}}/edit/">编辑</a>
                                <a class="btn btn-danger btn-xs" href="/depart/delete/?nid={{obj.id}}">删除</a>
                            </td>
                        </tr>
                    {% endfor %}
                    
                    
                </tbody>
            </table>
        </div>
    </div>
    <script src="{% static 'js/jquery-4.0.0.js' %}"></script>
    <script src="{% static 'plugins/bootstrap3.4.1/js/bootstrap.js' %}"></script>
</body>

</html>
```

- 部门添加

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap3.4.1/css/bootstrap.css' %}">
</head>

<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li><a href="/depart/list">部门管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">登入</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">蜡笔小新· <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">个人资料</a></li>
                            <li><a href="#">我的信息</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">注销</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>

    <div class="container" style="border: 1px solid rgb(214, 214, 214);">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">新建部门</h3>
            </div>
        </div>
        <form class="form-horizontal" method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="inputEmail3" class="col-sm-2 control-label">标题</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" placeholder="标题" name="title">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <button type="submit" class="btn btn-primary">保存</button>
                </div>
            </div>
        </form>
    </div>

    <script src="{% static 'js/jquery-4.0.0.js' %}"></script>
    <script src="{% static 'plugins/bootstrap3.4.1/js/bootstrap.js' %}"></script>
</body>

</html>
```

- 部门修改

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap3.4.1/css/bootstrap.css' %}">
</head>

<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li><a href="/depart/list">部门管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">登入</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">蜡笔小新· <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">个人资料</a></li>
                            <li><a href="#">我的信息</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">注销</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>

    <div class="container" style="border: 1px solid rgb(214, 214, 214);">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">修改部门</h3>
            </div>
        </div>
        <form class="form-horizontal" method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="inputEmail3" class="col-sm-2 control-label">标题</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" placeholder="标题" name="title" value="{{row_object.title}}">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <button type="submit" class="btn btn-primary">保存</button>
                </div>
            </div>
        </form>
    </div>

    <script src="{% static 'js/jquery-4.0.0.js' %}"></script>
    <script src="{% static 'plugins/bootstrap3.4.1/js/bootstrap.js' %}"></script>
</body>

</html>
```

#### 6.模板继承

```
{% block 块名 %} 和 {% endblock 块名 %} 是一对标签，用来在模板中「预留一个可被替换 / 填充的区域」。
```

定义模板：layout.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap3.4.1/css/bootstrap.css' %}">
    {% block css %}  {% endblock %}
</head>
<body>
    <h1>标题</h1>
    <div>
        {% block content %}  {% endblock %}
    </div>
    <h1>底部</h1>
    <script src="{% static 'js/jquery-4.0.0.js' %}"></script>
    <script src="{% static 'plugins/bootstrap3.4.1/js/bootstrap.js' %}"></script>
    {% block js %}  {% endblock %}
</body>
</html>
```

续程模板

```html
{% extends "layout.html" %}

{% block css %} 
	<link rel="stylesheet" href="{% static '写这个页面专门需要的.css' %}">
{% endblock %}

{% block content %}
  <h1>首页</h1>
{% endblock %}

{% block js %} 
	<script src="{% static '写这个页面专门需要的.js' %}"></script>
{% endblock %}
```

#### 7. 用户管理

新建用户：

- 原始方式思路：不采纳（麻烦）

```
- 用户提交数据没有校验
- 如果重新错误，页面上应该有错误提示
- 页面上每一个字段都要写一遍，麻烦
- 关联数据还要手动获取，并循环展示在页面
```

- Django小组件
  - Form组件（小简便）
  - ModelForm组件（最简便）


```
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| id          | bigint        | NO   | PRI | NULL    | auto_increment |
| name        | varchar(16)   | NO   |     | NULL    |                |
| password    | varchar(32)   | NO   |     | NULL    |                |
| age         | int           | NO   |     | NULL    |                |
| account     | decimal(10,2) | NO   |     | NULL    |                |
| create_time | date          | NO   |     | NULL    |                |
| gender      | smallint      | NO   |     | NULL    |                |
| depart_id   | bigint        | NO   | MUL | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
```

- views.py

```python
def user_add(request):
    if request.method == "GET":
        context = {
            'gender_choice': models.UserInfo.gender_choice,
            'department': models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)
    
    # 获取用户提交数据
    user = request.POST.get('name')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    depart = request.POST.get('depart')
    gender = request.POST.get('gender')

    # 添加到数据库中
    models.UserInfo.objects.create(name=user,age=age,account=account,create_time=create_time,depart_id=depart,gender=gender)
    return redirect('/user/list')
```

- user_list.html

```html
{% extends "layout.html" %}

{% block content %}
    <div>
        <!-- 在新页面打开 target="_blank" -->
        <a class="btn btn-primary" href="#" style="margin-bottom:10px" target="_blank">新建用户</a>
    </div>

    <div class="panel panel-default">
        <!-- Default panel contents -->
        <div class="panel-heading">
            <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
            部门列表
        </div>

        <!-- Table -->
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>名字</th>
                    <th>年龄</th>
                    <th>工资</th>
                    <th>入职时间</th>
                    <th>部门</th>
                    <th>性别</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
                {% for obj in user_list %}
                    <tr>
                        <th scope="row">{{obj.id}}</th>
                        <td>{{obj.name}}</td>
                        <td>{{obj.age}}</td>
                        <td>{{obj.account}}</td>
                        <!-- 特殊的三个，要用一些手段 -->
                        <td>{{obj.create_time}}</td>
                        <td>{{obj.depart.title}}</td>
                        <td>{{obj.get_gender_display}}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="#/">编辑</a>
                            <a class="btn btn-danger btn-xs" href="#">删除</a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

- user_add

```html
{% extends "layout.html" %}

{% block content %}
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">新建用户</h3>
        </div>
    </div>
    <form class="form-horizontal" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">名字</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" placeholder="名字" name="name">
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">年龄</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" placeholder="年龄" name="age">
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">工资</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" placeholder="工资" name="account">
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">入职时间</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" placeholder="入职时间" name="create_time">
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">部门</label>
            <div class="col-sm-10">
                <select class="form-control" name="depart">
                    {% for item in department %}
                      <option value="{{item.id}}">{{item.title}}</option>
                    {% endfor %}
                </select>
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">性别</label>
            <div class="col-sm-10">
                <select class="form-control" name="gender">
                    {% for item in gender_choice %}
                      <option value="{{item.0}}">{{item.1}}</option>
                    {% endfor %}
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-primary">提交</button>
            </div>
        </div>
    </form>
{% endblock content %}
```

##### 7.1 初始Form

1.views.py

```python
class MyForm(Forms):
    # 还是要手动添加
    user = form.charField(widget=forms.Input)
    pwd = form.charField(widget=forms.Input)
    email = form.charField(widget=forms.Input)

def user_add(request):
    if request.method == "GET":
        form = MyFrom()
        return render(request, 'user_add.html', {"from", from})
```

2.user_add.html

```html
<form class="form-horizontal" method="post">
	{% csrf_token %}
    <!-- 可以循环并且自动生成input形式 -->
    {% for item in form %}
    	{{ item }}
    {% endfor %}
	<!-- <input type="text" class="form-control" placeholder="标题" name="title"> -->

</form>
```

##### 7.2.ModelFrom

1.models.py

```python
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
```

2.views.py

```python
# 用户 ModelForm 表单类
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "age", "account", "gender", "depart"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

# 用户 ModelForm 添加视图
def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})
    form = UserModelForm(data=request.POST)
    # 校验
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    else:
        return render(request, 'user_model_form_add.html', {"form": form})
```

3.user_model_form_add.html

```html
{% extends "layout.html" %}

{% block content %}
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">新建用户</h3>
        </div>
    </div>
    <form class="form-horizontal" method="post">
        {% csrf_token %}
        {% for item in form %}
          <div class="form-group">
            <label for="inputEmail3" class="col-sm-2 control-label">{{item.label}}</label>
            {{item}}
            <span>{{item.errors.0}}</span>
            <!-- <div class="col-sm-10">
                <input type="text" class="form-control" placeholder="{{item.label}}" name="name">
            </div> -->
        </div>
        {% endfor %}
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-primary">提交</button>
            </div>
        </div>
    </form>
{% endblock content %}
```

##### 7.4编辑用户

- views.py

```python
def user_edit(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form':form})
    
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form':form})
```

- user_edit.html

```html
{% extends "layout.html" %}

{% block content %}
  <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">编辑用户</h3>
        </div>
    </div>
    <form class="form-horizontal" method="post">
    {% csrf_token %}
    {% for item in form %}
    <div class="form-group {% if item.errors %}has-error{% endif %}">
        <label class="col-sm-2 control-label">{{ item.label }}</label>
        <div class="col-sm-10">
            {{ item }}
            
            {% if item.errors %}
                <span class="text-danger">{{ item.errors.0 }}</span>
            {% endif %}
        </div>
    </div>
    {% endfor %}
    <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
            <button type="submit" class="btn btn-primary">提交</button>
        </div>
    </div>
</form>
{% endblock content %}
```

##### 7.5 删除用户

- views.py

```python
def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')
```

#### 8.靓号管理

##### **8.1表结构**

- models.py

```python
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
```

自己创建一些数据：

```sql
insert into app01_mobileinfo(mobile,price,level,status)values('1111111111',19,1,1);
```

##### **8.2 靓号列表**

- views.py

```py
def pretty_list(request):
    if request.method == "GET":
        queryset = models.MobileInfo.objects.all().order_by("-level")
        return render(request, 'pretty_list.html', {'queryset':queryset})
```

##### **8.3 靓号添加**

- views.py

```python
class PrettyModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$'),'手机号格式错误']
    )
    class Meta:
        model = models.MobileInfo
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

def pretty_add(request):
    if request.method == "GET":
        form = PrettyModelForm
        return render(request, 'pretty_add.html', {"form":form})
     # 用户POST提交数据，数据校验
    form = PrettyModelForm(data=request.POST)
    # 校验
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    else:
        return render(request, 'pretty_add.html', {"form": form})
```

##### **8.4 靓号编辑**

- 与用户编辑相似



##### **8.5 靓号搜索**

```python
models.PrettyNum.object.fileter(mobile="13224543663",id=1)

data_dict = {"mobile":"13224543663", "id":1}
models.PrettyNum.object.fileter(mobile="**data_dict")
```

```python
models.PrettyNum.object.fileter(id=1)      #等于1
models.PrettyNum.object.fileter(id__gt=1)  #大于1
models.PrettyNum.object.fileter(id__gte=1)  #大于等于1
models.PrettyNum.object.fileter(id__lt=1)  #小于1
models.PrettyNum.object.fileter(id__lte=1)  #小于等于1
```

```python
models.PrettyNum.object.fileter(mobile_startswith="132")   # 筛选出以132为开头
models.PrettyNum.object.fileter(mobile_endswith="132")   # 筛选出以132为结尾
models.PrettyNum.object.fileter(mobile_contains="132")   # 筛选出包含132的
```

- pretty_list.html

```html
<form method="get">
        <div class="input-group" style="float: right;width: 300px;">

            <input type="text" name="q" class="form-control" placeholder="寻找......" _mstplaceholder="164775" _msthash="653">
            <span class="input-group-btn">
                <button class="btn btn-default" type="submit" _msttexthash="10084152" _msthash="654">走！</button>
            </span>

        </div>
    </form>
```

- views.py

```python
def pretty_list(request):
    # 1. 获取搜索参数
    value = request.GET.get('q')
    # 2. 构建查询条件
    if value:
        queryset = models.MobileInfo.objects.filter(mobile__contains=value).order_by("-level")
    else:
        queryset = models.MobileInfo.objects.all().order_by("-level")
    # 3. 统一返回
    return render(request, 'pretty_list.html', {'queryset': queryset})
```

##### 8.6 分页

```python
# 第一页
queryset = models.PrettyNum.object.all()[0:10]

# 第二页
queryset = models.PrettyNum.object.all()[10:20]

# 第三页
queryset = models.PrettyNum.object.all()[20:30]

# 符合条件的数据有多少条
data = models.PrettyNum.object.all().count()
```

views.py

```python
def pretty_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["mobile_contains"] = search_data

    # 根据用户想要的页面计算出数据
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page - 1) * 10
    end = page * 10

    total_count = models.MobileInfo.objects.filter(**data_dict).order_by("-level").count()
    queryset = models.MobileInfo.objects.filter(**data_dict).order_by("-level")[start:end]
    
    # 计算出总页码
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1

    # 计算出前5页和后5页
    plus = 5
    if total_page_count <= 2 * plus + 1:
        # 数据库数据少，都没达到11页就用这个
        start_page = 1
        end_page = total_page_count
    else:
        if page <= plus:
            start_page = 1
            end_page = 2*plus
        else:
            if (page + plus) > total_page_count:
                start_page = page - plus
                end_page = page
            else:
                start_page = page - plus
                end_page = page + plus
        
    # 页码
    page_str_list = []

    page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))

    # 上一页
    if page > 1:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(page-1)
        page_str_list.append(prev)

    

    for i in range(start_page, end_page + 1):
        if i == page:
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
        else:
             ele = '<li><a href="?page={}">{}</a></li>'.format(i,i)
        page_str_list.append(ele)

    # 下一页
    if page < total_page_count:
        prev = '<li><a href="?page={}">下一页</a></li>'.format(page+1)
        page_str_list.append(prev)
    else:
        prev = '<li><a href="?page={}">下一页</a></li>'.format(total_page_count)

    page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page_count))

    page_string = mark_safe("".join(page_str_list))

    
    
    return render(
        request,
        'pretty_list.html',
        {
            "queryset":queryset,
            "search_data":search_data,
            "page_string":page_string,
        }
    )
```

pagination.py

```python
from django.utils.safestring import mark_safe
import copy
from django.http.request import QueryDict
"""
在views.py中
    # 根据自己的情况筛选数据
    queryset = models.MobileInfo.objects.all()
    # 实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
            "queryset":page_object.page_queryset,  # 分完页的数据
            "page_string":page_object.html(), # 生成页码
        }
    return render(request, 'pretty_list.html', context)

在HTML页面中
    {% for obj in queryset %}
        {{obj.xx}}
    {% endfor %}
    </li>
      {{page_string}}
    <li>
"""
class Pagination(object):
    def __init__(self, request, queryset, page_size = 10, page_param="page", plus=5):
        """
        request: 请求对象
        queryset: 符合条件的数据
        page_size: 每页多少条数据
        page_param: 在URL中传递获取分页参数
        plus: 显示当前页的前后几页
        """
        page = int(request.GET.get(page_param, 1))

        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
    
        # 计算出总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1

        self.total_page_count = total_page_count
        self.plus = plus


    def html(self):
        
        # 计算出前5页和后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库数据少，都没达到11页就用这个
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2*self.plus
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.page - self.plus
                    end_page = self.page
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
            
        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])

        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(),i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(),i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))
        
        page_string = mark_safe("".join(page_str_list))

        return page_string
```

#### 9.ModelForm和BootStrap

- ModelForm可以帮助我们生成HTML标签

```python
class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_lenth=3, labal="用户名")
    
    class Meta:
        model = models.UserInfo
        fields = ["name", "password"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
            else:
            	field.widget.attrs = {"class":"form-control"}

```

```html
{{form.name}}   普通input框
{{form.password}}   普通input框
```

#### 10.管理员操作

#### 11.用户登入

- 什么是cookie和session

```
http://127.0.0.1:8000/admin/list
https://127.0.0.1:8000/admin/list
```

- cookie，随机字符串
- session，用户信息

想要登录才能访问，在函数开头加：

```python
def index(request):
    info  = request.session.get("info")
        if not info:
            return redirect("/login/")
```

views.py : 登录逻辑

```python
def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    
    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password']).first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", '用户名或密码错误')
            return render(request, 'login.html', {'form':form})
        
        request.session['info'] = {'id':admin_object.id, 'name':admin_object.username}
        return redirect("/admin/list/")
    return render(request, 'login.html', {'form':form})
```

##### 11.1.中间件

- 定义中间件

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
# from django.http import HttpResponse

class M1(MiddlewareMixin):

    def process_request(self, request):
        print('M1 进来了')

    def process_response(self, request, response):
        print('M1 走了')
        return HttpResponse("无权访问")
    
class M2(MiddlewareMixin):

    def process_request(self, request):
        print('M2 进来了')

    def process_response(self, request, response):
        print('M2 走了')
        return response
```

- 应用中间件

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app01.middleware.auth.M1',
    'app01.middleware.auth.M2',
]
```

- 在中间件的process_request方法

```python
# 如果方法中没有返回值，继续向后走
# 如果有返回值 HttpResponse、render、redirect，则不再继续向后执行
```

##### 11.2 中间件实现登录校验

- 编写中间件

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

class AuthMiddleware(MiddlewareMixin):

    # 读取当前访问的用户session信息
    def process_request(self, request):

        if request.path_info == '/login/':
            return None

        info_dict = request.session.get('info')
        print(info_dict)
        if info_dict:
            return None
    # 如果没有登录过，返回登录页面
        return redirect('/login/')
    
def process_response(self, request, response):
        return response
```

- 应用中间件

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app01.middleware.auth.AuthMiddleware',
]
```

#### 12.图片验证码

##### 12.1 生成图片

```
pip install pillo
```

```python
from PIL import Image, ImageDraw, ImageFont
import random

# 随机验证码文本（数字+大小写字母）
def generate_random_captcha(length=4):
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789"
    return ''.join(random.choices(chars, k=length))

# 生成高难度干扰验证码图片
def generate_complex_captcha(code):
    # 画布大小
    width, height = 220, 80
    # 随机浅色背景
    bg_color = (random.randint(230, 255), random.randint(230, 255), random.randint(230, 255))
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # ✅ Windows专属字体 永远不报错
    try:
        # 调用Windows自带原生字体，效果最好
        font = ImageFont.truetype("arial.ttf", 45)
    except:
        # 找不到就自动降级兜底
        font = ImageFont.load_default(size=45)

    # 1. 画随机干扰背景噪点
    for _ in range(800):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(random.randint(0, 180), random.randint(0, 180), random.randint(0, 180)))

    # 2. 画干扰斜线条
    for _ in range(8):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1,y1), (x2,y2)], fill=(random.randint(50,150),random.randint(50,150),random.randint(50,150)), width=2)

    # 3. 逐个画字符：随机颜色、随机旋转、随机偏移
    offset = 30
    for char in code:
        # 随机深色文字
        text_color = (random.randint(10, 80), random.randint(10, 80), random.randint(10, 80))
        # 随机上下偏移
        y_offset = random.randint(-8, 8)
        # 随机倾斜位置
        draw.text((offset, 12 + y_offset), char, font=font, fill=text_color)
        offset += 48

    # 4. 增加随机曲线干扰
    import math
    for i in range(width):
        y = int(35 + 12 * math.sin(i * 0.04))
        draw.point((i, y), fill=(100,100,100))

    return img
```

account.py

```python
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
```

中间键

```python
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
```



#### 13.Ajax请求

浏览器向网站发送请求时：URL和表单的形式提交

- GET
- POST

特点：页面刷新



除此之外，也可以基于Ajax向后台发送请求

- 依赖jQuery
- 编写ajax代码

```javascript
$.ajax({
    url:"发送的地址",
    type:"post",
    data:{
        n1:123,
        n2:456
    },
    success:function(res){
        console.log(res);
    }
})
```

##### 13.1 post请求

```python
{% extends "layout.html" %}

{% block content %}
<h1>任务管理</h1>

<h3>实例</h3>
<input type="button" class="btn" value="点击" onclick="clickMe()">
{% endblock content %}

{% block js %}
<script>
    function clickMe() {
        console.log("点击了按钮")
        $.ajax({
            url: "/task/ajax/",
            type: "post",
            data: {
                n1: 123,
                n2: 456
            },
            success: function (res) {
                console.log(res);
            }
        })
    }
</script>
{% endblock js %}
```

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def task_list(request):

    return render(request, 'task_list.html')

@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse("成功了")
```

##### 13.2 ajax请求返回值

```html
{% extends "layout.html" %}

{% block content %}
<h1>任务管理</h1>

<h3>实例</h3>
<input type="button" class="btn" value="点击" onclick="clickMe()">
{% endblock content %}

{% block js %}
<script>
    function clickMe() {
        console.log("点击了按钮")
        $.ajax({
            url: "/task/ajax/",
            type: "post",
            data: {
                n1: 123,
                n2: 456
            },
            dataType:'JSON',
            success: function (res) {
                console.log(res);
                console.log(res.data)
                console.log(res.statues)
            }
        })
    }
</script>
{% endblock js %}
```

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def task_list(request):

    return render(request, 'task_list.html')

@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    data_dict = {'statue': True, 'data': [11, 22, 33, 44]}
    # 把字典转成 JSON 字符串
    json_string = json.dumps(data_dict)
    return HttpResponse(json_string)
```

##### 13.3 绑定事件

```html
<script>
    $(function () {
        // 框架加载完后自动执行
        bindBtnEvent();
    })

    function bindBtnEvent() {
        $("#btn1").click(function () {
            $.ajax({
            url: "/task/ajax/",
            type: "post",
            data: {
                n1: 123,
                n2: 456
            },
            dataType: 'JSON',
            success: function (res) {
                console.log(res);
                console.log(res.data)
                console.log(res.statues)
            }
        })
        })
    }
</script>
```

##### 13.4 订单

models.py

```python
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
```

order_list.html

```html
{% extends "layout.html" %}

{% block content %}
<div>
    <input id="btnAdd" type="button" value="新建订单" class="btn btn-primary">
</div>

<div class="panel panel-default">
    <!-- Default panel contents -->
    <div class="panel-heading">
        <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
        部门列表

    </div>

    <!-- Table -->
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>订单号</th>
                <th>名称</th>
                <th>价格</th>
                <th>状态</th>
                <th>管理员</th>
                <th>操作</th>
            </tr>
        </thead>
        <tbody>
            {% for obj in queryset %}
            <tr uid="{{obj.id}}">
                <th scope="row">{{obj.id}}</th>
                <td>{{obj.oid}}</td>
                <td>{{obj.title}}</td>
                <td>{{obj.price}}</td>
                <td>{{obj.get_status_display}}</td>
                <td>{{obj.admin}}</td>
                <td>
                    <input uid="{{obj.id}}" type="button" class="btn btn-primary btn-xs btn-edit" value="编辑">
                    <input uid="{{obj.id}}" type="button" value="删除" class="btn btn-danger btn-xs btn-delete">
                </td>
            </tr>

            {% endfor %}
        </tbody>
    </table>
</div>

<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="myModalLabel">Modal title</h4>
            </div>
            <div class="modal-body">
                <form class="form-horizontal" id="formAdd">
                    {% for field in form %}
                    <div class="form-group" style="margin-bottom: 15px; position: relative;">
                        <label class="col-md-2 control-label">{{field.label}}</label>
                        <div class="col-md-10" style="margin-top: 10px;">
                            {{field}}
                            <span style="color: red; position: absolute;" class="error-msg"></span>
                        </div>
                    </div>
                    {% endfor %}
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                <button id="btnSave" type="button" class="btn btn-primary">提交</button>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="alert alert-danger alert-dismissible fade in" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="结束" _mstaria-label="59709"
                    _msthash="785"><span aria-hidden="true" _msttexthash="19565" _msthash="786">×</span></button>
                <h4 _msttexthash="36649691" _msthash="787">是否确定删除</h4>
                <p _msttexthash="168849421" _msthash="788">删除所有关联数据都会删除，不可恢复</p>
                <p>
                    <button id="btnConfirmDelete" type="button" class="btn btn-danger" _msttexthash="20828418"
                        _msthash="789">确定</button>
                    <button type="button" class="btn btn-default" _msttexthash="16411707" _msthash="790"
                        data-dismiss="modal">取消</button>
                </p>
            </div>
        </div>
    </div>
</div>
<!-- 分页 -->
<nav aria-label="Page navigation">
    <ul class="pagination">
        <li>
            <a href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
        {{page_string}}
        <li>
            <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    </ul>
</nav>
{% endblock content %}

{% block js %}
<script>
    var DELETE_ID;
    var EDIT_ID;
    $(function () {
        bindBtnAddEvent();
        bindBtnSaveEvent();
        bindBtnDeleteEvent();
        bindBtnConfirmDeleteEvent();
        bindBtnEditEvent();
    })
    function bindBtnAddEvent() {
        $("#btnAdd").click(function () {
            // 将正在编辑的id设置为空
            EDIT_ID = undefined
            // 清空对话框数据
            $("#formAdd")[0].reset()
            // 设置对话框的标题
            $("#myModalLabel").text("新建")
            // 点击新建按钮，显示对话框
            $("#myModal").modal('show')
        })
    }

    function bindBtnSaveEvent() {
        $("#btnSave").click(function () {
            // 清除错误信息
            $(".error-msg").empty();
            if (EDIT_ID) {
                doEdit()
            } else {
                doAdd()
            }

        })
    }

    function doEdit() {
        // 向后台发送请求
        $.ajax({
            url: "/order/edit/?uid=" + EDIT_ID,
            type: "post",
            data: $("#formAdd").serialize(),
            dataType: "JSON",
            success: function (res) {
                console.log(res);
                if (res.status) {
                    alert("修改成功");
                    // 清空表单
                    $("#formAdd")[0].reset();
                    // 关闭对话框
                    $('#myModal').modal('hide');
                    // 刷新页面
                    location.reload();
                } else {
                    if (res.tips) {
                        alert(res.tips)
                    } else {
                        $.each(res.error, function (name, errorList) {
                            // 找到同级的下一个标签，并添加内容
                            $("#id_" + name).next().text(errorList[0])
                            // $("#id_" + name)
                            //     .closest(".col-md-10")  // 找到外层 div
                            //     .find(".error-msg")      // 找里面的错误提示 span
                            //     .text(errorList[0]);
                        })
                    }

                }
            }
        })
    }

    function doAdd() {
        // 向后台发送请求
        $.ajax({
            url: "/order/add/",
            type: "post",
            data: $("#formAdd").serialize(),
            dataType: "JSON",
            success: function (res) {
                console.log(res);
                if (res.status) {
                    alert("创建成功");
                    // 清空表单
                    $("#formAdd")[0].reset();
                    // 关闭对话框
                    $('#myModal').modal('hide');
                    // 刷新页面
                    location.reload();
                } else {
                    $.each(res.error, function (name, errorList) {
                        // 找到同级的下一个标签，并添加内容
                        $("#id_" + name).next().text(errorList[0])
                    })
                }
            }
        })
    }

    function bindBtnDeleteEvent() {
        $(".btn-delete").click(function () {
            // alert("删除")
            $("#deleteModal").modal('show')
            // 获取ID
            DELETE_ID = $(this).attr("uid");
        })
    }

    function bindBtnConfirmDeleteEvent() {
        $("#btnConfirmDelete").click(function () {
            // 将全局变量中要删除的数据发送到后台
            $.ajax({
                url: "/order/delete/",
                type: "GET",
                data: { uid: DELETE_ID },
                dataType: "JSON",
                success: function (res) {
                    if (res.status) {
                        // alert("删除成功")
                        // 隐藏删除框
                        // $("#deleteModal").modal('hide')

                        // $("tr[uid='"+ DELETE_ID +"']").remove()

                        location.reload();

                        DELETE_ID = 0
                    } else {
                        alert("删除失败")
                    }
                }
            })
        })
    }

    function bindBtnEditEvent() {
        $(".btn-edit").click(function () {
            var uid = $(this).attr("uid")
            EDIT_ID = uid
            $("#formAdd")[0].reset()
            // 获取当前行的数据
            $.ajax({
                url: "/order/detail/",
                type: "get",
                data: {
                    uid: uid
                },
                dataType: "JSON",
                success: function (res) {
                    if (res.status) {
                        $.each(res.data, function (name, value) {
                            $("#id_" + name).val(value)
                        })
                        $("#myModalLabel").text("编辑")
                        $("#myModal").modal('show')
                    } else {
                        alert(res.error)
                    }
                }
            })
        })
    }
</script>
{% endblock js %}
```



##### 13.5 图表

- highchart，国外

- echarts，国内

[快速上手 - 使用手册 - Apache ECharts](https://echarts.apache.org/handbook/zh/get-started/)

##　知识点回顾

### 1.1 基础入门

- 编码

```
编码基础知识：utf-8、unicode、gbk、ascil
默认解释器代码：
	- Python2: ascii
	- Python3: utf-8 
```

- 输入和输出

```
print()
input(),用户输入的永远是字符串类型

data = input("请输入序号：")
print(data)
```

- 变量

```
规范：字母、数组、下划线；数字不能开头
```

- 异常处理

```python
data = input("请输入：")
res = int(data)
print(res)
```

```python
try:
    data = input("请输入:")
    res = int(data)
	print(res)
except Exception as e:
    print("出差了")
print("结束")
```

- 循环中for/while内部都可以break、continue
- 字符串格式化

```
data = "我是{}，姓名是{}".format("xx",12)
data = "我是{1}，姓名是{0}".format(12,"xx")
```

- 运算符

```
- 逻辑运算符
	- 常见操作,最终结果：True\False
		if 1>10 and 9<8:
			pass
        else:
        	pass
    - 非传统
    	data = 值1 and 值2
    	v1 = 5 and 9
    	v2 = 0 and 10
```

### 1.2 数据类型

- 字符串类型

```
- 不可变类型
- 常见方法：strip\split\replace\join
	v1 = "root"
	data = v1.upper()
	print(v1)
	print(data)
```

- 列表类型

```
- 可变类型
- 常见方法：append\insert\pop\remove
- 公共：索引、切片、循环
	v1 = [11,22,33,44,55]
	v1[0]
	v1[1:3] - 前取后不取
- 列表推导式
	data = [ i for i in range(10) ]
	data = [ i for i in range(10) if i<5 ]
```

- 字典类型

```
- 可变类型
- 字典的键是有要求：可哈希类型，目前不可哈希类型：list\dict\set
- 常见功能：keys,values,items,get
	data={}
	v1 = data.get("k1")
```

- 其它数据类型

```
其它类型转布尔类型，那些为False：空、0、None
其它类型转自己类型时，自己的类名()
	int("123")
```

### 1.3 函数

- 定义

```python
def func():
    pass
func()
```

- 参数

```python
def func(v1, v2):
    pass

def func(v1, v2=None):
    pass

def func(*arg, **kwarges):
    pass
```

- 返回值

```python
- 没有返回值，默认返回None
	def func(v1,v2):
        print(999)
- 一个返回值
	def func(v1,v2):
        return 123
    res = func(1,2)
    print(res) # 123
    
- 多个返回值
	def func(v1,v2):
        return 123,45,11
    res = func(1,2)
    print(res) # (123,45,11)
- 解包
    def func(v1,v2):
        return 123,45,11
    v1,v2,v3 = func(1,2)
    print(v1) # 123
```

```python
v1,v2 = [11,22]
v1,v2,v3 = (11,2,2)
```

- laambda表达式(匿名函数)

```python
def func(arg):
	return arg + 100
func = lambda arg:arg+100

v1 = func(100)
print(v1) # 200
```

- 内置函数

```python
max/min/all/any/help/hex/oct/bin...

open,文件操作。
    open("xx.log", mode='r')
    data = f.read()
    f.close
```

- 文件操作

```
- 模式：r/w/a;  rb/wb/ab
- 打开或关闭
	with open("xx.log", mode='r') as f:
		f.read
```

### 1.4 模块

- 分类

```
- 自定义模块：自己写文件/文件夹
- 内置模块：time/datetime/json/hashlib/random/re等
- 第三方模块：openpyxl/requests/bs4/flask/django等
```

- 自定义模块

```
- sys.path, Python内部导入模块时，根据目录去寻找
- 导入模块：
	import xxx
	from xxx import xxx
```

- 内置模块

```
- 时间部分： time/datetime/字符串类型
- random: 随机生成数字
- hashlib: 加密(md5加密、md5加密+加盐)
- json
	- JSON格式的字符串：内部字符串双引号、内部[]
	- json.dumps
	- json.loads
	- dumps 转字符串，loads 变对象，dump 写文件，load 读文件
	
- re和正则
	- 正则：\d  \w ; 贪婪匹配
	- re.search/re.match/         re.findall
```

- 第三方模块

```
- 安装第三方模块: pip,源码,wheel
- 常见的第三方模块：
	- requests → 上网下载网页
	- bs4 → 从网页里提取数据
	- openpyxl → 操作 Excel
	- python-docx → 操作 Word
	- flask/django  (flask简洁;django功能强大)
```

### 1.5 面向对象

```
- 面向对象的三大特性：封装、继承、多态
```



### 1.6 MySOL数据库

```
- 数据库
- 表
- 数据行
```

```mysql
show databases;
use 数据库;

show tables;
desc 表名;

select * from 表;
insert into 表(列,列,列)values(...)
update 表 set 列=值
delete from 表 where 条件
```

Python连接并操作MySQL

- pymysql

```
pip install pymysql
```

- mysqlclient [django内部]

```
pip install mysqlclient
```



当使用Python代码去操作MySQL时，一定要防止SQL注入问题

```python
# SQL语句不要用字符串格式拼接
import pymysql


# 1 连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root123", database='unicom', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2 发送指令
# 不能这样写
# sql = "select * from admin where id > %s".format(2)
# cursor.execute(sql)

cursor.execute("select * from admin where id > %s",[2,])
# 3. 获取所有查询结果（核心：fetchall()的作用）
data_list = cursor.fetchall()
for row_dict in data_list:
    print(row_dict)

# 4 关闭
cursor.close()
conn.close()
```



### 1.7 前端开发

- html

```
- 块级和行内标签
	块级：div  p  h1~h6  ul  ol  li  table  tr  form
	行内：span  a  b  strong  i  em  u  label  input  img （设置宽高无效）
	
- Form表单 
	<form method="post" action="地址">
		<input ....>
		
		
		<input type="submit" ....>
	</form>
	
- 关于a标签
	<a href="www.baidu.com">百度</a>
```

- css

```
- 位置
	- 标签<div style="xxx">
	- style代码块
		<style>
			div{}
			#v1{}
			.v2{}
		</style>
- 选择器
	div{}
	#v1{}
	.v2{}
	div[xx='11']{}
	
- 样式
	color; background-color; padding; margin;
	float:left; 脱离文档流  clear:both;  :after
```

- JavaScript和jQuery

```
- 本质上：找标签；操作标签

- 找标签
	$("#x1")
	$(".x1")
	$("div")

- 操作标签
	$("#x1").text("")          <div id="x1">dd</div>
	$("#x1").text("xxx")       <div id="x1">xxx</div>
	
	$("#x1").val("xxx")        <input id="x1" />
	
	$("#x1").attr("uu")        <div id="x1" uu="123">xxx</div>
	$("#x1").attr("uu","999")  <div id="x1" uu="999">xxx</div>
	
	$("#x1").empty()           清空内容
	$("#x1").remove()          删除标签
```

- BootStrap

```
- 响应式布局，根据屏幕的宽度调整布局
- 栅格，12分
- 常见的样式
	- container  /  container-fluid
	- 面板
	- 按钮
	- 表单
	- 表格
	- 对话框
```

- 第三方插件

```
- 插件一般包含:css, JavaScript
	- 引入css,js(依赖jQuery)
```

### 1.8 Django

- 安装

```
pip install django
```

```
python安装目录下:
	- lib/site-packages/django源码包
	- Scripts/django-admin.exe
```

- 创建Django项目

```
>>>django-admin startproject 项目名
```

- 创建APP

```
>>>cd 项目目录
>>>python manage.py startapp app名称
```

- 注册APP

```
- 找到 settings.py 下的 INSTALLED_APPS 列表，把你的 app 名加进去（'你取的名字.apps.App01Config'）
- 如果不注册，models.py生成数据库行为不执行
- 如果不注册，模板文件、静态文件，不会去app目录下找
```

- static目录, 静态文件目录
- templates目录，模板文件目录（HTML）
- 表结构设计 app01/models.py下执行

```python
from django.db import models

class UserInfo(models.Model):
    v1 = models.CharField(max_length=32)
    ...
    ..
```

```
>>>python manage.py makemigretions
>>>python manage.py migrate
```

- urls.py中编写路由

```python
from django.urls import path
from app01.views import views
urlpatterns = [
    # 管理员列表
    path('myadmin/list/', views.admin_list),
    path('myadmin/add/', views.admin_add),
    path('myadmin/<int:nid>/edit/', views.admin_edit),
    path('myadmin/<int:nid>/delete/', views.delete_edit),
    path('myadmin/<int:nid>/reset/', views.admin_reset),
]
```

- 视图函数

```python
def admin_list(request):
    ...
    
- 默认参数request，包含请求相关的所有数据
	request.method
    request.GET
    request.POST
    request.FILES  上传文件
    request.path_info  获取当前请求的url
    	- http://127.0.0.1:8000/depart/add/ -> /depart/add/
        
- 返回值
	return HttpResponse("字符串")
	return JSONResponse({"k1":123,"k2":456})
	return JSONResponse([1,2,3,4],safe=False)
	return render(request, "xxx.html", {值})
	return redirect('http://127.0.0.1:8000/depart/add/')
```

- 数据库的ORM操作

```python
# 增加
models.类.objects.create(name="蜡笔小新"，age=19)
models.类.objects.create(**{'name'="蜡笔小新"，'age'=19})

obj = models.类(name="蜡笔小新"，age=19)
obj.save()

obj_list = [
    models.类(name="蜡笔小新"，age=19),
    models.类(name="蜡笔小新"，age=19),
    models.类(name="蜡笔小新"，age=19),
    models.类(name="蜡笔小新"，age=19),
    models.类(name="蜡笔小新"，age=19),
]
models.类.objects.bulk_create(obj_list,batch_size=10)
```

```python
# 查询
querset = models.类.objects.filter(name="蜡笔小新", age=5)          # [obj,obj,..] 或 []
querset = models.类.objects.create(**{'name'="蜡笔小新"，'age'=19})

obj = models.类.objects.filter(name="蜡笔小新", age=5).first() # obj  /  None

querset = models.类.objects.filter(age=5)
querset = models.类.objects.filter(age__gt=5)
querset = models.类.objects.filter(age__gte=5)
querset = models.类.objects.filter(age__lt=5)
querset = models.类.objects.filter(age__lte=5)

querset = models.类.objects.exclude(id=5)  # id != 5

querset = models.类.objects.filter(age__lte=5).order_by("id") # 从大到小
querset = models.类.objects.filter(age__lte=5)[0:10]          # 取前10条数据
```

```python
# 更新
queryset = models.类.objects.filter(id=2).update(age=33,name="蜡笔小新")
# 删除
models.类.objects.filter(id=2).delete()
```

- Form和ModelForm组件

```
- 自动生成HTML标签
- 对用户数据进行校验
	- 自动保存到数据库（ModelForm）
- 错误信息
```

```python
from django import forms

class UserForm(forms.Form):
    xx = form.CharField(..)
    
class UserModelsForm(forms.ModelForm):
    class Meta:
        model = models.类
        fields = "__all__"
```

```python
form = UserModelForm(data=request.POST,instance=对象)
if form.is_valid():
    form.cleaned_data
else:
    form.errors
```

- 关于POST提交CSRF认证

```
<form method="post">
	{% csrf_token %}
	...
</form>
```

如果想要免除csrf认证

```python
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def order_add(request):
    pass
```

- Cookie和Session

```
cookie, 本质上保存在浏览器端的键值对
session,保存服务器端(django是将session默认存储到数据库中)

def order_add(request):
	request.session['xx'] = 123
	
def logout(request):
	request.session.clear()
```

- 中间件

```
- 类 process_request / process_response
- 注册中间件找到setting.py中的MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app01.middleware.auth.AuthMiddleware',
]
- django请求到达之后，自动执行相应方法

- process_request
	- 没有返回值就返回None，继续向后执行
	- 返回redirect/render/HttpResponse/JsonReponse，拦截请求后不再继续向后
```

- 图片验证码

```
pip install pillow
```

```
- 创建图片并在图片上写文字
- 字体文件
- 自定义模块 check_code
```

- 分页组件

```
自定义，会调用就好
```

## 2.文件上传

- upload.py

```python
def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')
    # print(request.POST)
    # print(request.FILES)
    file_object = request.FILES.get("avatar")
    print(file_object.name)
	# 循环从 file_object 里分块读取数据
    with open(file_object.name, "wb") as f:
        for chunk in file_object.chunks():
            f.write(chunk)
    return HttpResponse("成功操作")
```

### 案例：批量上传数据

views.py

```python
def depart_multi(request):
    # 批量上传
    # 获取用户上传的文件对象
    file_object = request.FILES.get('exc')

    # 直接打开Excel并读取内容
    
    wb = load_workbook(file_object)
    sheet = wb.worksheets[0]

    cell = sheet.cell(1,1)
    # print(cell.value)

    for row in sheet.iter_rows(min_row=2):
        text = row[0].value
        print(text)
        exists = models.Department.objects.filter(title=text).exists()
        if not exists:
            models.Department.objects.create(title=text)

    return HttpResponse('上传文件')
```

### 案例：混合数据（Form）

form生成HTML标签

表单验证

form.cleaned_data 获取数据+文件对象

- upload.py(手动)

```python
def upload_form(request):
    title = "form上传"
    form = UpForm()
    if request.method == "GET":
        return render(request, 'upload_form.html', {"form":form, "title":title})
    
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        image_object = form.cleaned_data.get('img')
        db_file_path = os.path.join("static", "img", image_object.name)
        file_path = os.path.join("app01", db_file_path)
        with open(file_path, "wb") as f:
            for chunk in image_object.chunks():
                f.write(chunk)

        # 将数据文件写入数据库
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            img=db_file_path,
        )
        return HttpResponse("...")
    return render(request, 'upload_form.html', {"form":form, "title":title})
```

注意：所有的静态文件都是放在static目录，media用于用户上传数据的目录

### 2.1 启用media

在urls.py中进行配置

```python
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name="media"),
]
```

在setting.py中进行配置：

```
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 根目录下的media文件夹
```

#### 定义ModelForm

- upload.py（自动）

```python
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm

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
```

### 2.2 图片展示

```html
<img src="/media/{{obj.img}}" style="height: 80px">
```



## 总结

![image-20260505085310411](assets/image-20260505085310411.png)

![image-20260505085144638](assets/image-20260505085144638.png)
