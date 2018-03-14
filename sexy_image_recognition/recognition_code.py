import sys
import os
import _io
from collections import namedtuple

Al = namedtuple("Al","a b c d")

d = []
al = Al(3,4,5,'6')
cl = Al(2,5,6,7)
d.append(al)
d.append(cl)
print(d)
print(d[1].d)
print(al)
print(isinstance(al,tuple))
bl = al._replace(a=6)
print(bl)
al = bl
print(al)


list = []
a = [2,3,5]
b = [3,4,5]
# print(a[-])
list.append(a)
list.append(b)
print(list)
list.append(3)
print(list)
list[1].append(4)
print(list)
print(len(list))

d = 2
if d == None:
    print('ssss')

if d==2:
    print('ssss')
elif d <= 4:
    print('ssss')

# e = sum('1','7')
print(e)#sum函数的参数鼻血是可迭代的是list,tuple等
