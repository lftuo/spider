#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/10/7 下午7:39
# @File : DataOutput.py
# @Software : PyCharm
# @Email ： 909709223@qq.com
# 数据存储器，输出为html文件
import codecs


class DataOutput(object):
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def out_put_html(self):
        font = codecs.open('baike.html', 'w', encoding='utf-8')
        font.write("<html>")
        font.write("<body>")
        font.write("<table>")
        for data in self.datas:
            font.write("<tr>")
            font.write("<td>%s</td>" % data['url'])
            font.write("<td>%s</td>" % data['title'])
            font.write("<td>%s</td>" % data['summary'])
            font.write("</tr>")
            self.datas.remove(data)
        font.write("</table>")
        font.write("</body>")
        font.write("</html>")
        font.close()
