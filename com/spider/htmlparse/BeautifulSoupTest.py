#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/3 下午9:27
# @File : BeautifulSoupTest.py
# @Software : PyCharm
# BeautifulSoup的使用，解析html_str
import lxml
from bs4 import BeautifulSoup

html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story"><b>Once upon a time there were three little sisters; and their names were 
<a href="http://www.github.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://www.github.com/lacie" class="sister" id="link2"><!-- Elsie --></a> and 
<a href="http://www.github.com/tillie" class="sister" id="link3"><!-- Elsie -->Tillie</a>;
and they lived at the bottle of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')
print soup.prettify()
print "------title-------"
print soup.name
print soup.title

print "------  p  -------"
print soup.p

print "------  a  -------"
print soup.a

# tag修改标签属性，<title>修改为</mytitle>
soup.title.name = 'mytitle'
print soup.title
print soup.mytitle
