#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : MrTuo
# @Time : 2017/10/3 下午11:00
# @File : MultiprocessingPool.py
# @Software : PyCharm
# 进程池pool，如果进程池未满，则创建一个新的进程来执行，否则阻塞。进程结束后释放进程池中的占用。
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print 'Task %s (pid = %s) is running ... ' % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' % name


if __name__ == '__main__':
    print 'Current process %s.' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print 'Waiting for all subprocesses done ...'
    p.close()
    p.join()
    print 'All subprocesses done.'
