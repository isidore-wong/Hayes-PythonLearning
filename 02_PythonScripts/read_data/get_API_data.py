# _*_ coding:utf-8 _*_
import requests
import json
import xml.etree.ElementTree as Etree

"""
@author: Isidore
@email: 616132717@qq.com
@file: get_API_data
@time: 2020/05/01 16:37
"""

"""
程序目的：通过API获取并解析数据
"""

address = '广州市珠江新城'
ak = 'E6ce7SusapsN04S61ltjdfrR1yamEGuw'
# 请求url，返回json格式的数据
# url_json = 'http://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s&callback=showLocation'
# res = requests.get(url_json % (address, ak))
# add_info = res.text
# add_json = json.loads(add_info)
# lat_lng = add_json['result']['location']
# # print(add_info)    # 返回的json信息
# print(lat_lng)

# 请求URL，返回XML格式的数据
url_xml = 'http://api.map.baidu.com/geocoding/v3/?address=%s&output=xml&ak=%s&callback=showLocation'
res = requests.get(url_xml % (address, ak))
add_info = res.text
root = Etree.fromstring(add_info)
lng = root[1][0][0].text
lat = root[1][0][1].text

# print(add_info)
print('lng: %s, lat: %s' % (lng, lat))