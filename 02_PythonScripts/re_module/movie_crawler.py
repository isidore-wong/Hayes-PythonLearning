# _*_ coding:utf-8 _*_
import re
import urllib.request

"""
@version: python 3.6
@author: Isidore
@file: movie_crawler.py
@time: 2018/11/13  23:23
"""

"""
程序目的：用urllib和re爬取影院的电影播放名单
"""


class CrawlerMeihua(object):
    ''' 获取当前页面的信息 '''
    def __init__(self):
        self.url = 'http://zhishi.meihua.info/'
        self.timeout = 5
        self.fileName = './biaoti.txt'
        self.get_info()

    def get_info(self):
        response = urllib.request.urlopen(self.url, timeout=self.timeout)
        title_list = re.findall('article-title')



if __name__ == '__main__':
    tm = CrawlerMeihua()
