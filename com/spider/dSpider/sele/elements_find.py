#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/14 下午9:42
# @File : elements_find.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('file:// /Users/tuotuo/PycharmProjects/spider/com/spider/dSpider/sele/login_test.html')
login_form = driver.find_element_by_id('loginForm')
print login_form
username = driver.find_element_by_name('username')
print username