#!/usr/bin/python
# -*- coding:utf8 -*-
# 自定义cookie的值并发送
import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; MAC OS)'
headers = {'User-Agent':user_agent}
cookies = dict(name='lftuo',age='18')
r = requests.get('http://www.baidu.com',headers = headers,cookies = cookies)
print r.text