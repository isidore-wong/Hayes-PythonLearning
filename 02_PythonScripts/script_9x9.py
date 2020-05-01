# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@file: script_9x9.py
@time: 2018/11/12  0:52
"""

"""
程序目的：实现九九乘法表
"""


class PrintTable(object):
    # 打印九九乘法表
    def __init__(self):
        print('我们需要打印出的九九乘法表如下：')
        self.print9x9()


    def print9x9(self):
        for i in range(1, 10):
            for j in range(1, 10):
                if j <= i:
                    print('%d * %d = %d' % (j, i, i*j), end='\t')
                else:
                    break
            print('\n')
        print('\n')


if __name__ == '__main__':
    pt = PrintTable()
