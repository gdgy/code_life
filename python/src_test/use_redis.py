#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 15:07
# @Author  : shaoyong_li
# @Site    : 
# @File    : use_redis.py
import os, sys
import redis

class RedisUse(object):

    def __init__(self, config):
        self.config = config
        self.connection_pool = redis.ConnectionPool(host=self.config['host'], port=self.config['port'], db=self.config['index'], password=self.config['auth'],
                                         encoding=self.config['encoding'], max_connections=10)
        self.redis_cli = redis.Redis(connection_pool=self.connection_pool)

    def key_isexists(self, key):
        return  self.redis_cli.exists(key)

    def _del_key(self, key):
        return self.redis_cli.delete(key)

    def _use_set(self):
        pass







