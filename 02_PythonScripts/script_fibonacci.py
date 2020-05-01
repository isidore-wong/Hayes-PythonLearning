# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@file: script_fibonacci.py
@time: 2018/11/12  0:52
"""

"""
程序目的：实现斐波那契数列
"""


class Fibonacci(object):
    def __init__(self):
        self.f_list = [0, 1]    # 设置斐波那契数列的初始列表
        self.main()

    def main(self):
        list_len = input('请输入斐波那契数列的长度(3-50)：')
        self.check_len(list_len)
        while len(self.f_list) < int(list_len):
            self.f_list.append(self.f_list[-1] + self.f_list[-2])
        print('我们所获得到的斐波那契数列为：\n %s' % self.f_list)

    def check_len(self, lenth):
        # 检验输入的数据是否符合要求
        len_list = map(str, range(3, 51))
        if lenth in len_list:
            print('输入长度符合标准，程序继续运行')
        else:
            print('请输入3-50的整数')
            exit()


if __name__ == '__main__':
    fn = Fibonacci()
