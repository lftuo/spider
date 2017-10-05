#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/5 下午3:44
# @File : Save2CSVbyLxml.py
# @Software : PyCharm
# 使用lxml解析http://seputu.com/首页，并存储为csv
from lxml import etree
import requests
import re
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; MAC OS)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com', headers=headers)
# print r.text
# 使用lxml解析网页
html = etree.HTML(r.text)
div_mulus = html.xpath('.//*[@class="mulu"]')  # 先找到所有的div class=mulu标记

rows = []
for div_mulu in div_mulus:
    # 找到div_h2标记
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            # 找到href属性
            href = a.xpath('./@href')[0]
            # 找到title属性
            box_title = a.xpath('./@title')[0].encode('utf-8')
            # print href,box_title
            parttern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = parttern.search(box_title)
            if match != None:
                date = match.group(1).encode('utf-8')
                real_title = match.group(2).encode('utf-8')
                #print real_title
                content = (h2_title,real_title,href,date)
                # print content
                rows.append(content)
headers = ['title','real_title','href','date']
with open('qiye.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)