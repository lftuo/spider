#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-2 18:52:44
# @File : ScalableBloomFilter.py
# @Software : IntelliJ IDEA
from pybloom import ScalableBloomFilter
sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
count = 10000
for i in range(0,count):
    sbf.add(i)
print 10001 in sbf
print 4 in sbf