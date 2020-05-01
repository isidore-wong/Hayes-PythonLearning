# _*_ coding:utf-8 _*_
from myLog import MyLog

"""
@version: python 3.6
@author: Isidore
@file: test_logging.py
@time: 2018/11/13  17:01
"""

"""
程序目的：
"""

if __name__ == '__main__':
    ml = MyLog()
    ml.debug('I am debug message')
    ml.info('I am info message')
    ml.warn('I am warn message')
    ml.error('I am error message')
    ml.critical('I am critical message')

