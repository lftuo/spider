#!/usr/bin/python
# -*- coding:utf8 -*-
# 重定向与历史信息：设置allow_redirects=true，则允许重定向，可查看历史信息，即访问成功之前的所有请求跳转信息；设置为false，则禁止重定向
# eg：requests.get('http://www.github.com',allow_redirects=True)
import requests

r = requests.get('http://www.github.com', allow_redirects=True)
print r.url
print r.status_code
print r.history
