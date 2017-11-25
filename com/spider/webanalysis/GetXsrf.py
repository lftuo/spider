#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/24 下午9:03
# @File : GetXsrf.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
import re
import requests


def get_xsrf(session):
    '''
    _xsrf是一个动态变化的参数，从网页中提取
    :param session:
    :return:
    '''
    index_url = 'http://www.zhihu.com'
    # 获取登录时的_xsrf
    index_page = session.get(index_url,headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf返回的是一个list
    _xsrf = re.findall(pattern,html)
    return _xsrf[0]


agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0'
headers = {
    'User-Agent':agent
}
session = requests.session()
_xsrf = get_xsrf(session)
post_url = 'http://www.zhihu.com/login/phone_num'
postdata = {
    '_xrsf':_xsrf,
    'password':'1991721tlf',
    'remember_me':'true',
    'phone_num':'15295733044'
}
login_page = session.post(post_url,data=postdata,headers=headers)
login_code = login_page.text
print(login_page.status_code)
print(login_code)

