# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@file: show_tuple.py
@time: 2018/11/11  17:47
"""

"""
程序目的：元组的操作，元组与列表的区别在于，list是可修改的，tuple是不可修改的
"""


class ShowTuple(object):
    def __init__(self):
        self.T1 = ()
        self.createTuple()  # 创建元组
        self.subTuple(self.T1)  # 元组分片
        self.tuple2List(self.T1)    # 元组与列表转换

    def createTuple(self):
        print('创建元组：')
        self.T1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(self.T1)
        print('**---------------------------**')
        print('\n')

    def subTuple(self, T1):
        print('元组分片：')
        l1 = self.T1[3:]
        print(l1)
        l2 = self.T1[1:-1:2]
        print(l2)
        print('**---------------------------**')
        print('\n')

    def tuple2List(self, T1):
        print('元组转换为列表：')
        l3 = list(self.T1)
        print(l3)
        print('**********')
        l3.append(100)
        print(l3)
        print(tuple(l3))
        print('**---------------------------**')
        print('\n')


if __name__ == '__main__':
    st = ShowTuple()
