# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@file: if_else.py
@time: 2018/11/11  22:43
"""

"""
程序目的：if...else...循环语句
检验输入的数字是否能够被7整除
"""


def is_even_num(num):
    if num % 7 == 0:
        print('%d可以被7整除' % num)
    else:
        print('%d不能被7整除' % num)


if __name__ == '__main__':
    num_str = input('请输入一个整数: ')
    try:
        num = int(num_str)
    except ValueError:
        print('输入有误！请输入一个整数：')
        exit()

    is_even_num(num)
