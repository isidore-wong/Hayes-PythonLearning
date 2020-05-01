# _*_ coding:utf-8 _*_
import logging

"""
@version: python 3.6
@author: Isidore
@file: test_mylog.py
@time: 2018/11/13  15:05
"""

"""
程序目的：
"""


class TestLogging(object):
    def __init__(self):
        log_format = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
        log_filename = './testLog.txt'

        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            filename=log_filename,
            filemode='w'
        )

        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warning message')
        logging.error('error message')
        logging.critical('critical message')


if __name__ == '__main__':
    t1 = TestLogging()
