# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@file: show_list.py
@time: 2018/11/11  17:46
"""

"""
程序目的：list的基本操作方法
"""


class ShowList(object):
    def __init__(self):
        self.L1 = []
        self.L2 = []

        self.createList()  # 创建列表
        self.insertData()  # 插入数据
        self.appendData()  # 追加数据
        self.deleteData()  # 删除数据
        self.sublist()  # 列表分片

    def createList(self):
        print('创建列表:')
        print("L1 = list('abcdefg')")
        self.L1 = list('abcdefg')
        print('L2 = []')
        for i in range(1, 10):
            self.L2.append(i)
        print('L1 = ')
        print(self.L1)
        print('L2 = ')
        print(self.L2)
        print('**---------------------------**')
        print('\n')

    def insertData(self):
        print('list列表插入数据')
        self.L1.insert(3, 100)
        print('向L1的第3个位置插入数字100:')
        print(self.L1)
        print('向L2第10个位置插入Python')
        self.L2.insert(10, 'Python')
        print(self.L2)
        print('**---------------------------**')
        print('\n')

    def appendData(self):
        print('向list中追加数据')
        print('向L1中追加列表[1, 2, 3]')
        self.L1.append([1, 2, 3])
        print(self.L1)
        print('**---------------------------**')
        print('\n')

    def deleteData(self):
        print('删除list中的数据，使用pop方法')
        l3 = self.L1.pop()  # 默认删除列表中的最后一个元素
        print(l3)    # 输出默认删除的元素
        print(self.L1)  # 输出删除后的列表
        print('**---------------------------**')
        print('\n')

    def sublist(self):
        print('列表分片')
        print('取L1的第3-last one组成新的列表')
        l4 = self.L1[2:]
        print(l4)


if __name__ == '__main__':
    print('list的演示: \n')
    ShowList()
