# # 1.打开文件
# fp = open('C:/Users/86189/Desktop/study/python/AI应用/picture/text.txt', 'w+', encoding='utf-8')

# # 2.读取文件内容
# fp.write('我加点东西')
# # 关键：把文件指针移回开头，否则 read() 会读到空内容
# fp.seek(0)
# content = fp.read()
# print(content)

# # 3.关闭文件
# fp.close()

# with open('C:/Users/86189/Desktop/study/python/AI应用/picture/text.txt', 'a+', encoding='utf-8') as fp:
#     fp.write('我加些东西')
#     fp.seek(0)
#     content = fp.read()
#     print(content)

import json

user = {'name': '张三', 'age': 18}

with open('C:/Users/86189/Desktop/study/python/AI应用/picture/user.json', 'w', encoding='utf-8') as fp:
    json.dump(user, fp, ensure_ascii=False)