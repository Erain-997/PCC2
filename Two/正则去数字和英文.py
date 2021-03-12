import re
a="not 404 found 张三 99 深圳"
list = a.split()
print(list)
#re.findall 方法能够以列表的形式返回能匹配的子串
#小d表示取数字0-9，大D表示不要数字，也就是出了数字以外的内容返回
res = re.findall('\d+|[a-zA-Z]+',a)
print(res)
for i in res:
    if i in list:
        list.remove(i)
print(list)
###S.join(iterable) -> str
new=" ".join(list)
print(new)