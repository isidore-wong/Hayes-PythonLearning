# _*_ coding:utf-8 _*_
import random
import logging

"""
@version: python 3.6
@author: Isidore
@file: script_probability.py
@time: 2018/11/12  0:53
"""

"""
程序目的：随机数猜测
"""


class GuessNum(object):
    def __init__(self):
        print('随机产生一个1-100的随机数：')
        self.num = random.randint(1, 101)
        self.guess(self.num)

    def guess(self, num):
        i = 0
        while True:
            print('****************************')
            str_num = int(input('请输入一个1-101的数字：'))
            i += 1
            try:
                if str_num < num:
                    print('你猜的数字太小,请继续.')
                    continue
                elif str_num > num:
                    print('你猜的数字太大,请继续.')
                    continue
                else:
                    print('bingo,你猜对了,总共猜了%d次' % i)
                    break
            except Exception as e:
                logging.exception(e)
                print('输入的内容必须是数字!')
                continue


if __name__ == '__main__':
    gn = GuessNum()
