#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/12 下午8:45
# @File : sele_test.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"性感美女")
elem.send_keys(Keys.RETURN)
time.sleep(13)
assert u"性感美女." not in driver.page_source
driver.close()