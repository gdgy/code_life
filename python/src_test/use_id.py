#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 9:49
# @Author  : shaoyong_li
# @Site    : 
# @File    : use_id.py
__doc__ = 'python id'

a = 5
b = 10
c = a
assert (id(a) == id(c))
assert (id(a) != id(b))
assert (a is c)


def hello():
    print('Hello, World!')


class TestClass(object):
    x = 6

    def __init__(self, c):
        self.z = 5
        self.c = c
        self.test_func = hello

test_a = TestClass(3)
test_b = TestClass(2)

print ('static x:',id(test_a.x), id(test_b.x), id(TestClass.x))
print ('z:',id(test_a.z), id(test_b.z), id(TestClass.x))
print ('C:', id(test_a.c), id(test_b.c))
test_a.z = 7
test_b.z = 8
print ('z assignment:',id(test_a.z), id(test_b.z))
print ('func:', id(test_a.test_func), id(test_b.test_func))
test_a.x = 10
test_b.x = 'b'
print (test_a.x, test_b.x, TestClass.x)
print (id(test_a.x), id(test_b.x), id(TestClass.x))



