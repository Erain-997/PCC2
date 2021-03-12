s= "python"
print(s[::-1])

l=list(s)
l.reverse()
print(l)
print("".join(l))


a=[[1,2],[3,4],[5,6]]
b=[j for i in a for j in i]
print(b)

e="dd1"
f="ddff"
if e in f:
    print("111")