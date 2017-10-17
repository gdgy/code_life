# !/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'shaoyong_li'
__doc__ = 'time cost demo'
import time

def func_run_cost(func):
    def wrapper(*args, **kwargs):
        starttime = time.time()
        ret = func(*args, **kwargs)
        print "time_cost:", time.time() - starttime
        return ret
    return wrapper

@func_run_cost
def tiem_TEST(a, b, c):
    time.sleep(2)
    print "----------", a, b, c

def main():
    tiem_TEST(1, 2, 3)

if __name__ == "__main__":
    main()

