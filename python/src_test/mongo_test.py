#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 10:40
# @Author  : shaoyong_li
# @Site    : 
# @File    : mongo_test.py
import re
import pymongo
import json
import bson
import datetime
config = {
    'mongo_iData':{
        "write_host": "10.25.172.254:23451",
        "read_host": "10.25.172.254:23451",
        "username": "qxbdev",
        "password": "dEGJI53F#m8gxg58#pfgH76FDST",
        "db": "iData"},
    'mongo_test': {
        "write_host": "10.31.121.3:27017",
        "read_host": "10.31.121.3:27017",
        "username": "qxbdev",
        "password": "FDsaf#m8gxg58#pqirv787Oo0IN",
        "db": "iEnterprise"},

}
def mongo_cli_query(table, query):
    mongo_client = pymongo.MongoClient(host=config["mongo_iData"]["write_host"])
    mongo_db_write = mongo_client[config["mongo_iData"]["db"]]
    mongo_db_write.authenticate(config["mongo_iData"]["username"], config["mongo_iData"]["password"])
    _table = mongo_db_write[table]
    data_rows = _table.find(query)
    for data_row in data_rows:
        print ('keyword:', data_row['keyword'])
        print ('company:', json.dumps(data_row['infos'], ensure_ascii=False))
        print ('---------------')


def mongo_write(table, docs):
    mongo_client = pymongo.MongoClient(host=config["mongo_test"]["write_host"])
    mongo_db_write = mongo_client[config["mongo_test"]["db"]]
    mongo_db_write.authenticate(config["mongo_test"]["username"], config["mongo_test"]["password"])
    _table = mongo_db_write[table]
    data_rows = _table.insert(docs)
    print data_rows

if __name__ == '__main__':
    # mongo_cli_query(table='custom_keywords', query={'infos.companies':{'$in': [re.compile('博西家用*')]}})
    #  mongo_cli_query(table='custom_keywords', query={'keyword': re.compile('浙江昌德成电器有限公司*')})
    # mongo_cli_query(table='custom_keywords', query={'keyword': '西安海镁特镁业有限公司'})
    docs = {
        "sign" : "c34e558f813f4e0f9262540ade1bfc21",
        "user_id" : "5a0c08cf0207cd0ad9dc0f6a",
        "title" : "测试印象 测试",
        "brief" : "U传播平台从单一的软文发稿发展为整合网络营销服务商，媒体资源从单一的网络媒体资源拓宽至微博、微信等新媒体精准营销资源，从紧跟时事热点到不定期推送媒体套餐服务，力图满足每一个客户的需求，让无数企业通过软文推广的方式获得了大范围的曝光，不仅提升了企业品牌知名度，也促进了企业产品销售成交。",
        "link" : "http://ifeng.com/a/20180119/55272451_0.shtml",
        "img" : "",
        "related" : "深圳拓宽传媒有限公司",
        "status" : "U",
        "created_by" : "5a0c08cf0207cd0ad9dc0f6a",
        "last_updated_by" : "5a0c08cf0207cd0ad9dc0f6a",
        "last_updated_time" : datetime.datetime.now(),
        "created_time" : datetime.datetime.now(),
        "retry_times": 2,
        "__v" : 0
    }
    mongo_write('ruanwens', docs)
