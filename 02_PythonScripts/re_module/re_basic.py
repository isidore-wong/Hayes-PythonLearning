# _*_ coding:utf-8 _*_
import re

"""
@version: python 3.6
@author: Isidore
@file: re_basic.py
@time: 2018/11/13  22:52
"""

"""
程序目的：regular excepression  re模块的方法：
re.compile(pattern, flags=0):将字符串形式的正则表达式编译为pattern对象
re.search(string[,pos[,endpos]]):从string的任意位置开始匹配
re.match(string[,pos[,endpos]]):从string的开头开始匹配
re.findall(string[,pos[,endpos]]):从string的任意位置开始匹配，返回一个列表
re.finditer(string[,pos[,endpos]]):从string的任意位置开始匹配，返回一个迭代器
"""

s = 'I am python modules test for re modules'

print(re.search('am', s))
print("****")
print(re.search('am', s).group())
print("----------")
print(re.match('am', s))
print("**----**")
print(re.match('I am', s))
print(re.match('I am', s).group())
print(re.findall('modules', s))
print('--*******--')
print(re.finditer('modules', s))
for sre in re.finditer('modules', s):
    print(sre.group())


