#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 17:12
# @Author  : shaoyong_li
# @Site    : 
# @File    : data_chunk.py
import json
import re
pattern = re.compile(U'person_name:([\w]*)')
def chunk():
    with open('src.txt', 'r') as fp:
        data_str = fp.read()
    data_list = data_str.split('},')
    for item in data_list:
        personname = pattern.search(item)
        if personname:
            print (personname.group())
    # with open('result.txt', 'w+') as fp:
    #     pass


if __name__ == '__main__':
    chunk()

