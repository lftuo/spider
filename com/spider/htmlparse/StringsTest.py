#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/4 上午8:53
# @File : StringsTest.py
# @Software : PyCharm
# .string&.string&.stripped_strings 用法
import bs4
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
# 打印注解
print '------------ comment ------------'
if type(soup.a.string) == bs4.element.Comment:
    print soup.a.string
print '\n'
# 打印直接子节点
print '----------- .contents -----------'
print soup.head.contents
print '\n'
# 以列表方式获取
print '---------- contents[] -----------'
print len(soup.head.contents)
print soup.head.contents[0].string
print '\n'
# .strings方法：tag中包含的所有字符串都打印
print '----------- .strings ------------'
for string in soup.strings:
    print (repr(string))
print '\n'
# .stripped_strings用法：去掉输出字符串中的空格及换行
print '------- .stripped_strings -------'
for string in soup.stripped_strings:
    print (repr(string))
