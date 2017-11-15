#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/15 下午9:43
# @File : implicit_wait.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# selenium的隐式等待
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://www.baidu.com")
nameElement = driver.find_element_by_id("name")
