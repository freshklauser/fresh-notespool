# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-21 18:59:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-21 19:22:58

'''
redis基本功能函数
'''
import redis
from redisConf import *

def redisPool():
    return redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db= REDIS_DB_TEST, password=REDIS_PASSWORD)


