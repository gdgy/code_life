#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 11:22
# @Author  : shaoyong_li
# @Site    : 
# @File    : path_test.py
import os, sys
THIS_FILE_NAME = __file__
THIS_FILE_PATH = ''
print ('dir_name:', os.path.dirname(THIS_FILE_NAME))
print ('base_name:', os.path.basename(THIS_FILE_NAME))
