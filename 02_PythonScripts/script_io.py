# _*_ coding:utf-8 _*_
import os

"""
@version: python 3.6
@author: Isidore
@file: script_io.py
@time: 2018/11/12  0:53
"""

"""
程序目的：文件IO操作
"""


def operate_file(str):
    with open('file.txt', 'w') as fp:
        fp.write(str)

    with open('file.txt', 'r') as fp:
        for line in fp.readlines():
            print(line)


if __name__ == '__main__':
    str = input('请输入你要写入文件中的内容：')
    operate_file(str)
