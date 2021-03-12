a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
a.sort()
last=a[-1]
for i in range(len(a)-2,-1,-1):
    if last==a[i]:
        del a[i]
    else:
        last=a[i]
print(a)

b=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
b.sort()
c=[]
for i in b:
    if i not in c:
        c.append(i)
print(c)