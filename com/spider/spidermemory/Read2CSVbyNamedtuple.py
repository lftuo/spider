#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/5 下午3:26
# @File : Read2CSVbyNamedtuple.py
# @Software : PyCharm
# 使用命名元组读取csv文件
from collections import namedtuple
import csv

with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print row.Username, row.Password
        print row
