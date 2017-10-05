#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/5 下午3:35
# @File : Read2CSVbyDictlist.py
# @Software : PyCharm
# 读取csv文件到一个字典序列中，使用列名访问每一行数据
import csv

with open('qiye.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print row.get('Username'), row.get('Password')
