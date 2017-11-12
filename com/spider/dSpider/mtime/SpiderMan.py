#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/9 下午10:55
# @File : SpiderMan.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# 爬虫调度器
import time

from com.spider.dSpider.mtime.DataOutput import DataOutput
from com.spider.dSpider.mtime.HtmlDownloader import HtmlDownloader
from com.spider.dSpider.mtime.HtmlParser import HtmlParser


class SpiderMan(object):

    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(root_url,content)
        # 构造一个获取评分和票房链接
        for url in urls:
            print url
            try:
                t = time.strftime("%Y%m%d%H%M%S3282",time.localtime())
                # 构造一个链接
                rank_url = 'http://service.library.mtime.com/Movie.api?' \
                           'Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&' \
                           'Ajax_CallBackMethod=GetMovieOverviewRating&' \
                           'Ajax_CrossDomain=1&' \
                           'Ajax_RequestUrl=%s&' \
                           't=%s&' \
                           'Ajax_CallBackArgument0=%s'%(url[0],t,url[1])
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url,rank_content)
                self.output.store_data(data)
            except Exception,e:
                print "crawl failed"

if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Beijing')