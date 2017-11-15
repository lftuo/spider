#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/15 下午7:14
# @File : login_selenium.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
from selenium import webdriver

# 1.初始化FireFox驱动
dirver = webdriver.Firefox()
dirver.get("file:// /Users/tuotuo/PycharmProjects/spider/com/spider/dSpider/sele/login.html")
# 2.获取用户名和密码的输入框，和登录按钮
username = dirver.find_element_by_name('username')
password = dirver.find_element_by_xpath(".//*[@id='loginForm']/input[2]")
login_button = dirver.find_element_by_xpath("//input[@type='submit']")
# 3.使用send_keys方法输入用户名和密码，使用click方法模拟点击登录
username.send_keys("qiye")
password.send_keys("qiye_pass")
login_button.click()

# 轮流点击选项卡
#select = dirver.find_element_by_xpath("//form/select")
#all_options = select.find_elements_by_tag_name("option")
#for option in all_options:
#    print("Value is: %s"% option.get_attribute("value"))
#    option.click()

# 根据索引/文字/value值来获取选项卡
from selenium.webdriver.support.ui import Select
#select = Select(dirver.find_element_by_xpath('//form/select '))
#select.select_by_index(1)
#select.select_by_visible_text("用户名")
#select.select_by_value("name")

# 元素拖拽
element = dirver.find_element_by_name("source")
target = dirver.find_element_by_name("target")

from  selenium.webdriver import ActionChains
action_chains = ActionChains(dirver)
action_chains.drag_and_drop(element,target).perform()
