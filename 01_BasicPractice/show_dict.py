# _*_ coding:utf-8 _*_


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@file: show_dict.py3
@time: 2018/11/11  17:48
"""

"""
程序目的：
"""


class ShowDict(object):
    def __init__(self):
        self.spiderMan = self.createDict()  # 创建字典
        self.insertDict(self.spiderMan)  # 插入元素
        self.modifyDict(self.spiderMan)  # 修改元素
        self.operationDict(self.spiderMan)  # 字典操作

    def createDict(self):
        print('创建字典')
        spiderMan = {
            'name': 'Peter Parker',
            'sex': 'male',
            'Nation': 'Americ',
            'college': 'MIT',
        }
        self.showDict(spiderMan)
        return spiderMan

    def showDict(sel, spiderMan):
        print(spiderMan)
        print('**---------------------------**')
        print('\n')

    def insertDict(self, spiderMan):
        print('插入元素:')
        spiderMan['age'] = 31
        self.showDict(spiderMan)
        print('**---------------------------**')
        print('\n')

    def modifyDict(self, spiderMan):
        print('修改字典元素：')
        spiderMan['college'] = 'Empire State University'
        self.showDict(spiderMan)
        print('**---------------------------**')
        print('\n')

    def operationDict(self, spiderMan):
        print('字典的其他操作方法：')
        print('显示所有键和所以键的值：')
        keys_list = spiderMan.keys()
        print(keys_list)
        print('***********')
        values_list = spiderMan.values()
        print(values_list)
        print('***********')
        items_list = spiderMan.items()
        print(items_list)
        print('**********')

        print('从字典中取出某个特定键的对应值:')
        college = spiderMan.get('college')
        print('college = %s' % college)


if __name__ == '__main__':
    sd = ShowDict()
