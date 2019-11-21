# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-21 18:59:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-21 19:44:19

'''
python操作redis 发布/订阅模式的发布客户端(可考虑多线程发布)
'''

import redis
import redisUtil
from redisConf import *

def redisPublish():
    pool = redisUtil.redisPool()
    redis_client = redis.StrictRedis(connection_pool=pool)
    countFlag = 5
    while countFlag:
        chn = input("channel: ")
        if chn not in REDIS_CHANNEL_LIST:
            countFlag -= 1
            if countFlag == 0:
                redis_client.publish(REDIS_CHANNEL_0, 'over')
            print('No channel found for channel {}'.format(chn))
            continue
        msg = input("publish: ")
        redis_client.publish(chn, msg)
        if msg == 'over':
            print("停止发布")
            break

if __name__ == '__main__':
    redisPublish()