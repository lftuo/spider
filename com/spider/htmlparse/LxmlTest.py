#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/4 下午8:32
# @File : LxmlTest.py
# @Software : PyCharm
# lxml的xPath解析，需要熟悉xPath语法
from lxml import etree
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story"><b>Once upon a time there were three little sisters; and their names were 
<a href="http://www.github.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://www.github.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and 
<a href="http://www.github.com/tillie" class="sister" id="link3"><!-- Tillie -->Tillie</a>;
and they lived at the bottle of a well.</p>
<p class="story">...</p>
"""
# 自动补全代码
html = etree.HTML(html_str)
result = etree.tostring(html)
print result
print '\n'
# 直接读取html文件
html = etree.parse('index.html')
result = etree.tostring(html,pretty_print=True)
print result
# 利用xPath语法抽取其中的URL
html = etree.HTML(html_str)
urls = html.xpath(".//*[@class='sister']/@href")
print urls