import copy

# a={"a":1,"b":2,"c":3}
a=[1,2,3,4,5,["x","y"]]
b=a#赋值语句
c=copy.copy(a)#浅拷贝
d=copy.deepcopy(a)#深拷贝
print("a的地址",id(a))
print("b的地址",id(b))
print("c的地址",id(c))
print("d的地址",id(d))
print(a[5],id(a[5]))
print(b[5],id(b[5]))
print(c[5],id(c[5]))
print(d[5],id(d[5]))
a.append(6)
a[5].append("z")
a[2]=7
print("a=",a,id(a))
print("b=",b,id(b))
print("c=",c,id(c))
print("d=",d,id(d))
print(a[5],id(a[5]))
print("a的第3个元素",a[2],id(a[2]))
print("c的第3个元素",c[2],id(c[2]))
print(b[5],id(b[5]))
print(c[5],id(c[5]))
print(d[5],id(d[5]))
