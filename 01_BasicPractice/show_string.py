# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@file: show_string.py
@time: 2018/11/11  14:59
"""

"""
程序目的：
字符串方法的学习与练习
"""

S = ' ThIs is a PYTHON '


def strCase(S):
    # 字符串的大小写转换
    print("字符串的大小写转化方法")
    print('大小写转换：S.swapcase()=%s' % (S.swapcase()))
    print('首字母大写:S.title()=%s' % (S.title()))
    print("**_________________________________**")


def strFind(S):
    # 字符串的查找、替换
    print("字符串搜索:s.find('is')=%s" % (S.find('is')))
    print("字符串统计:s.count('s')=%s" % (S.count('s')))
    print("字符串替换:s.replace('IS','is')=%s" % (S.replace('IS', 'is')))
    print("字符串去空格:s.strip()=%s" % (S.strip()))
    print("**_________________________________**")


def strSplit(S):
    # 字符串的分割和组合
    print("字符串分割:s.split()=%s" % (S.split()))
    s1 = S.split()
    print('s1=%s' % s1)
    print("字符串的组合:s.join()=%s" % (' '.join(['this', 'is', 'a', 'python'])))
    print("字符串的组合:s.join()=%s" % ('#'.join(['this', 'is', 'a', 'python'])))
    print("**_________________________________**")


def strTest():
    # 字符串的测试
    s1 = 'abcd'
    print('s.isalpha()=%s' % (s1.isalpha()))
    print('s.isdigit()=%s' % (s1.isdigit()))
    print('s.isspace()=%s' % (s1.isspace()))
    print('s.islower()=%s' % (s1.islower()))
    print('s.isupper()=%s' % (s1.isupper()))
    print('s.istitle()=%s' % (s1.istitle()))


if __name__ == '__main__':
    strCase(S)
    strFind(S)
    strSplit(S)
    strTest()
