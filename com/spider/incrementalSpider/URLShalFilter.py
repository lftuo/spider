#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-2 19:07:34
# @File : URLShalFilter.py
# @Software : IntelliJ IDEA
import hashlib
from scrapy.dupefilters import RFPDupeFilter
from w3lib.url import canonicalize_url


class URLShalFilter(RFPDupeFilter):
    """根据urlshal过滤"""
    def __init__(self,path = None):
        self.url_seen = set()
        RFPDupeFilter.__init__(self,path)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))
        url_shal = fp.hexdigest()
        if url_shal in self.url_seen:
            return True
        else:
            self.url_seen.add(url_shal)
