# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os
import logging

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


def tick():
    time.sleep(10)
    print('Tick! The time is: %s' % datetime.now())


def one_time_job(**kwargs):
    if kwargs:
        print (kwargs)
    print ('this is onetimes job:%s' % datetime.now())


def cron_job():
    print ('beg sleep....:%s' % datetime.now())
    time.sleep(500)
    print ('end sleep....:%s' % datetime.now())



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    # 单独一个线程处理scheduler job
    scheduler = BackgroundScheduler()
    # scheduler job 业务代码不会执行
    scheduler = BlockingScheduler()
    logger = logging.getLogger('my')
    # 间隔任务
    scheduler.add_job(tick, 'interval', seconds=30)
    scheduler.add_job(one_time_job, 'interval', seconds=30, kwargs={'a':1, 'b':2})
    #定时任务
    scheduler.add_job(one_time_job, 'date', run_date='2018-01-16 16:19:05')
    scheduler.add_job(cron_job, 'cron', day_of_week='0-6', second='*/5' , id='test1')
    scheduler.start()    #这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    scheduler.print_jobs()
    scheduler.remove_job('test1')

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            with open('myapp.log', 'a') as fp:
                scheduler.print_jobs(out=fp)
            time.sleep(2)    #其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
