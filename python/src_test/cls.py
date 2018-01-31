#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 19:31
# @Author  : shaoyong_li
# @Site    : 
# @File    : cls.py
__doc__ = '类的静态方法类方法'


class Foo(object):
    X = 1
    Y = 2

    def __init__(self):
        print('__init__ func is called')

    def member(self):
        return self.averag(5, 2)

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)


class Foo2(Foo):

    def __init__(self):
        # 调用父类构造函数
        Foo.__init__(self)
        # super(Foo2, self).__init__()

    @staticmethod
    def static_method():
        print ('child func static_method')
        return Foo2.averag(Foo2.X, Foo2.Y)


foo = Foo()
print(foo.static_method())
print(foo.class_method())
print(foo.member())
foo2 = Foo2()
print(foo2.static_method())
print(foo2.class_method())
print(foo2.member())
