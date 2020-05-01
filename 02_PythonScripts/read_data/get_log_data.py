# _*_ coding:utf-8 _*_


"""
@author: Isidore
@email: 616132717@qq.com
@file: get_log_data
@time: 2020/05/01 18:16
"""

"""
程序目的：获取非结构文本log中的数据
"""
file_data = '../dataset/traffic_log_for_dataivy'
fn = open(file_data, 'r')
content = fn.readlines()
print(content[:2])
fn.close()
