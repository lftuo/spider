#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-2 18:42:33
# @File : BloomFilterTest.py
# @Software : IntelliJ IDEA
from pybloom import BloomFilter
f = BloomFilter(capacity=1000,error_rate=0.001)
print [f.add(x) for x in range(10)]
print 12 in f
print 4 in f
