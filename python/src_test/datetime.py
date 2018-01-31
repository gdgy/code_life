#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 9:39
# @Author  : shaoyong_li
# @Site    : 
# @File    : datetime.py
__doc__ = """datetime 使用样例"""
import datetime, time

def use_datetime():
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))

    str_to_datetime = datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
    print (str_to_datetime)

    datetime_to_timetuple = now.timetuple()
    print (datetime_to_timetuple)
    timestamp = time.mktime(datetime_to_timetuple)
    print (timestamp)

    timestamp_to_datetime = datetime.datetime.fromtimestamp(timestamp)
    print (timestamp_to_datetime)

    #日期
    print (now.date())

    # 一天的开始时间
    today = datetime.datetime.today()
    assert (today.date(), now.date())
    print (type(today), type(now.date()))
    print (datetime.datetime.combine(today, datetime.time.max))
    print ('today_start: ', datetime.datetime.combine(today, datetime.time.min))

if __name__ == "__main__":
    use_datetime()
