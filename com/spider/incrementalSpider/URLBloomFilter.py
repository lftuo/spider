#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-2 19:14:32
# @File : URLBloomFilter.py
# @Software : IntelliJ IDEA
import hashlib

from pybloom import ScalableBloomFilter
from scrapy.dupefilters import RFPDupeFilter
from w3lib.url import canonicalize_url


class URLBloomFilter(RFPDupeFilter):
    """根据urlhash_bloom过滤"""
    def __init__(self,path=None):
        self.urls_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))
        url_shal = fp.hexdigest()
        if url_shal in self.urls_sbf:
            return True
        else:
            self.urls_sbf.add(url_shal)