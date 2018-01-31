#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 16:50
# @Author  : shaoyong_li
# @Site    : 
# @File    : small_test.py
from apscheduler.scheduler import Scheduler
import random
print random.randint(1, 5)


import logging
def test():
    try:
        test1()
        logging.info('a.key----------')
    except Exception as e:
        logging.info("err_msg:%s", str(e))


def test1():
    try:
        a = dict()
        logging.info('a.key:%s', a['key'])
    except Exception as e:
        logging.info('key:%s, key2:%s err_msg:%s', str(e), '1111')

def chinese_key():
    key_test = dict()
    key_test.setdefault('中文', list())
    print key_test

def list_insert():
    a = list()
    a.append(0)
    a.append(1)
    a.insert(0, 3)
    print (a)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
    # formater = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    # console = logging.StreamHandler()
    # # console.setFormatter(formater)
    # # 将定义好的console日志handler添加到root logger
    # logging.getLogger('').addHandler(console)
    # test()
    chinese_key()
    list_insert()
    import os
    os.re