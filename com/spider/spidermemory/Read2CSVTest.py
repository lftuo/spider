#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/5 下午3:18
# @File : Read2CSVTest.py
# @Software : PyCharm
# 读取csv文件
import csv

with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print headers
    for row in f_csv:
        print row