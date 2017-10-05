#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/5 下午3:04
# @File : Write2CSVTest.py
# @Software : PyCharm
# 写csv测试
import csv

headers = ['ID', 'Username', 'Password', 'Age', 'Country']
rows = [("1001", "qiye", "qiye_pass", 24, "China"),
        ("1002", "Mary", "Mary_pass", 20, "USA"),
        ("1003", "Jack", "Jack_pass", 20, "USA")]
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# rows也可以是字典数据
rows = [{'ID': 1001, 'Username': 'qiye', 'Password': 'qiye_pass', 'Age': 24, 'Country': 'China'},
        {'ID': 1002, 'Username': 'Mary', 'Password': 'Mary_pass', 'Age': 20, 'Country': 'USA'},
        {'ID': 1003, 'Username': 'Jack', 'Password': 'Jack_pass', 'Age': 20, 'Country': 'USA'}]
with open('qiyedict.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
