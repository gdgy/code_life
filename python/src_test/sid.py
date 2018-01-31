#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 11:06
# @Author  : shaoyong_li
# @Site    : 
# @File    : sid.py


def handle_exit(signum, _):
    if signum == signal.SIGTERM:
        print ('%d is exiting' % (os.getpid()))
        sys.exit(0)
    sys.exit(1)

if __name__ == '__main__':
    import os, sys, time, signal
    signal.signal(signal.SIGTERM, handle_exit)
    pid = os.fork()
    if pid > 0:
        print ('child pid:%s' % (pid))
        time.sleep(10)

    ppid = os.getppid()
    os.setsid()
    print ('kill %d' %(ppid))
    os.kill(ppid, signal.SIGTERM)
    print(os.getpid())

    while True:
        time.sleep(5)
