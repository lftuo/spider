#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/10/7 上午8:59
# @File : HtmlDownloader.py
# @Software : PyCharm
# @Email ： 909709223@qq.com
# Html下载器
import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None
