# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@project:mycode 
@file: essentials.py
@time: 2018/10/30  15:38
"""

"""
程序目的：
python学习基础练习
"""

# list
a = []
b = [1, 2.0, 'hello', 5+1.0]

print(a)
print(b[0])
print(b[-1])
print(len(b))


c = b + b

b.append("world")
print("**_______________________________**")
print(b)

print(c)

print("**______________________________________________**")
b.reverse()
print(b)

b.pop()
print(b)

b.insert(1, 8)
print(b)

b.remove(8)
print(b)


# set
# 集合中不含有相同元素
s = {1, 2, 3, 4, 2}
print(s)

s.add(6)
print(s)

# 用{key:value}来生成Dictionary
d = {'cat': 'miao', 'dog': 'wang'}
print(d)

# 


