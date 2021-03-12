a=[[1,2],[3,4],[5,6]]
b=[j for i in a for j in i]
print(b)


import numpy
c=numpy.array(a).flatten().tolist()
d=numpy.array(a).flatten()
e=numpy.array(a)
print(e)
print(d)
print(c)

