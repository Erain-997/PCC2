# list=[1,2,3,4,5,4,5]
# it = iter(list)
# print(next(it))
# print(next(it))
#
# import sys
# def fibonacci (n):
#     a,b,couter = 0,1,0
#     while True:
#         if (couter>n):
#             return
#         yield a
#         a,b = b,b+a
#         couter +=1
# f = fibonacci(5)
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

import os
path = os.getcwd()
str = "11"

if os.path.exists(path):
    file = os.listdir()
    print(file)
for i in file:
    if os.path.isfile(os.path.join(path,i)):
        if i.find(str) == 0:
            print(os.path.join(path,i))



t=(1,2)
copy_t = tuple(t)
print(t is copy_t)#元组无法复制。 原因是元组是不可变的。 如果运行tuple(tuple_name)将返回自己。


class A:
    def hello(self):
        print("hello")
    def world(self):
        print("world")
def other(a=1):
    print(a)
monkey = A()
monkey.hello = monkey.world
monkey.hello()
monkey.world = other
monkey.world()


def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
        print(type(kwargs))
func(a=1,b=2,c=7)

print(r'\n')

l=[1,2]
l.pop(l,1)

