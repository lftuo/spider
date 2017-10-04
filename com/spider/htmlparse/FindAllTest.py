#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/4 上午9:17
# @File : FindAllTest.py
# @Software : PyCharm
# find_all:搜索文档树
# find_all(name , attrs , recurisive , text , **kwargs )
from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')

# name 参数：查找所有字符串为'name'的标记，字符串被自动过滤。name参数值可以是字符串／正则表达式／列表／True／方法等
print '--------------- name ---------------'
# 字符串
print soup.find_all('b')
# 正则表达式
import re

for tag in soup.find_all(re.compile("^b")):
    print tag.name
# 列表
print soup.find_all(["a", "b"])
# True:可以匹配任意值，去掉字符串
for tag in soup.find_all(True):
    print tag.name


# 自定义方法
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')


print soup.find_all(hasClass_Id)
print '\n'
# kwargs参数：字符串／正则表达式／列表／True
print '--------------- kwargs --------------'
print soup.find_all(id="link2")
import re

print soup.find_all(href=re.compile("tillie"))
# 无论ID是何值，存在则输出
print soup.find_all(id=True)
# class是python关键字，需在前加'_'
print soup.find_all("a", class_="sister")
# 使用多个名字的参数，可以同时过滤tag的多个属性
print soup.find_all(href=re.compile("elsie"), id="link1")
# text：搜索文档中字符串内容：数值可以是字符串／正则表达式／列表／True／方法等
print '--------------- text ----------------'
print soup.find_all(text="Elsie")
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
print soup.find_all(text=re.compile("Dormouse"))
print soup.find_all("a", text="Elsie")
# limit：限制返回结果条数
print '-------------- limit ----------------'
print soup.find_all("a", limit=2)
# recursive：搜索tag的直接子节点：recursive=False
print soup.find_all("title")
print soup.find_all("title", recursive=False)
