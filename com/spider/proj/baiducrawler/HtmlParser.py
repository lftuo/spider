#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/10/7 上午9:42
# @File : HtmlParser.py
# @Software : PyCharm
# @Email ： 909709223@qq.com
# html解析器
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页和内容
        :return: 返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的URL集合
        :param page_url:下载页面的URL
        :param soup: soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        # 抽取符合要求的a标记
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼成完整的网址
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取有效数据
        :param page_url: 下载页面的URL
        :param soup: soup
        :return: 返回有效的数据
        '''
        data = {}
        data['url'] = page_url
        # 解析'网络爬虫'标题主节点
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        # 获取tag中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode字符串返回
        data['summary'] = summary.get_text()

        return data
