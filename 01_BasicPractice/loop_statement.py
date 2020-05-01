# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@file: loop_statement.py
@time: 2018/11/11  23:57
"""

"""
程序目的：for循环，从1加到输入的数字
"""


def comulative(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


def main():
    while True:
        print('输入一个整数，计算从1累加到输入数字，退出计算输入exit')
        str_num = input('请输入一个整数：')
        if str_num == 'exit':
            break
        try:
            sum = comulative(int(str_num))
        except ValueError:
            print('退出计算请输入exit!')
            continue
        print('从1累加到%d的和是%d' % (int(str_num), sum))


if __name__ == '__main__':
    main()
