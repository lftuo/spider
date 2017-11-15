#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/15 下午9:31
# @File : explicit_wait.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# selenium的显式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"head"))
    )
finally:
    driver.quit()