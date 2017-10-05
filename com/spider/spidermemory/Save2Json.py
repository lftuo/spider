#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/4 下午9:04
# @File : Save2Json.py
# @Software : PyCharm
# 存储为json格式，解析盗墓笔记首页'http://seputu.com/'为例
import json
import requests
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; MAC OS)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers)
# print r.text
soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')# html.parsre
content=[]
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    #print h2
    if h2!=None:
        h2_title = h2.string #获取标题
        # print h2_title
        list=[]
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            # print href,box_title
            # 获取到了标题和链接，转存为json
            list.append({'href':href,'box_title':box_title})
        content.append({'title':h2_title,'content':list})
with open('qiye.json','wb') as fp:
    json.dump(content,fp=fp,ensure_ascii=False,indent=4)