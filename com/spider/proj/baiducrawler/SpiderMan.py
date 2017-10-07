#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/10/7 下午8:02
# @File : SpiderMan.py
# @Software : PyCharm
# @Email ： 909709223@qq.com
# 爬虫调度器，调度～html下载／html解析／URL管理／数据输出／初始化各模块
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从URL管理器中去除新的URL
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url,html)
                # 将抽取的URL添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print "已经抓取%s个链接"%self.manager.old_url_size()
            except Exception,e:
                print "crawl failed"
        # 数据存储器将文件输出为指定格式
        self.output.out_put_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")