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

def redisPublish(channel, msg):
    pool = redisUtil.redisPool()
    redis_client = redis.StrictRedis(connection_pool=pool)

    if channel not in REDIS_CHANNELS:
        
        redis_client.publish(REDIS_CHANNELS[-1], 'channel:"{}" is not found.'.format(channel))
        print('No channel found for channel:"{}"'.format(channel))
        print('Default target channels: {}'.format(REDIS_CHANNELS[:-1]))
    a = redis_client.publish(channel, msg)
    print("a:", a)
    if msg == -1:
        print("停止发布")


if __name__ == '__main__':
    import numpy as np
    import time
#    used = []
#    for i in range(10):
#        i += 1
#        channel = np.random.choice(REDIS_CHANNELS, 1, p=[0.1,0.3,0.4,0.2])[0]
#        if channel not in used:
#            used.append(channel)
#            msg = np.random.choice(REDIS_TOPICS, p=[0.9, 0.1])
#            if msg == 'exitflag':
#                break
#            redisPublish(channel, msg)
#        print('i --> ', i, ' :', channel, msg)
#        time.sleep(10)
#    
#    redisPublish(channel, 'exitflag')
        
#    print(channel)
    
    cnt = 5
    while cnt:
        channel = input()
        msg = input()
        redisPublish(channel, msg)
        cnt -= 1
        