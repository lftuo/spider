#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/3 下午10:39
# @File : OsMultiThread.py
# @Software : PyCharm
# 使用os模块中的fork方法，只适用于unix/linux系统
import os

if __name__ == '__main__':
    print 'current Process (%s) start ... ' % (os.getpid())
    pid = os.fork()
    if pid < 0:
        print 'error in fork'
    elif pid == 0:
        print 'I am child process(%s) and my parent process is (%s)' % (os.getpid(), os.getppid())
    else:
        print 'I(%s) created a child process (%s).' % (os.getpid(), pid)
