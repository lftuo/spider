#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/5 上午10:55
# @File : Json4DumpAndDumpsTest.py
# @Software : PyCharm
# json存储时使用的dump&dumps方法
import json
str = [{"username":"七夜","age":24},(2,3),1]
# dumps生成一个字符串
json_str = json.dumps(str,ensure_ascii=False)
print json_str
# dump把python对象转换成JSON对象，并将JSON对象通过fp文件流写入文件中
with open('qiye.txt','w') as fp:
    json.dump(str,fp=fp,ensure_ascii=False)

# 解码过程是把json对象转换成python对象的过程：load & loads，方法与dump & dumps一样
new_str = json.loads(json_str)
print new_str
# 读取文件留信息，转换成json解码
with open('qiye.txt','r') as fp:
    print json.load(fp)