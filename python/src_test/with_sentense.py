#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 11:53
# @Author  : shaoyong_li
# @Site    : 
# @File    : with_sentense.py

class ThisTestClass(object):

    def __init__(self):
        print ('this is test__init__')

    def __enter__(self):
        print ('this is enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print ('this is test__exit__')

    def __del__(self):
        print ('this is test__del__')

    def hello_test(self):
        print ('hello this is :%s'% self.hello_test.__name__)

with ThisTestClass() as test:
    """
    with 语句对象必须实现__enter__() 和 __exit__() 方法
    
    """
    #raise Exception
    test.hello_test()
    print ('this is for test')

from contextlib import contextmanager


@contextmanager
def demo():
    print ('[Allocate resources]')
    yield '*** contextmanager demo ***'
    print ('Code after yield-statement executes in __exit__')
    print ('[Free resources]')


with demo() as value:
    print 'Assigned Value: %s' % value

test_dict = dict()
assert ('test' not in test_dict.keys())
assert (not test_dict.keys())