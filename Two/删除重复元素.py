a=[1,2,4,2,4,5,6,5,7,8,9,0]
b=[]
for i in a:
    if i not in b :
        b.append(i)
b.sort()
print(b)

c=set(a)#返回的是字典
c=list(c)
print(c)

