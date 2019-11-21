# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-21 18:59:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-21 20:15:47

'''
python操作redis 发布/订阅模式的订阅客户端
publish [channel] [content]      # 将信息发送到指定的频道
subscribe channel [channel] ...  # 可以订阅一个或多个频道
'''

import redis
import redisUtil
from redisConf import *

def redisSubscribe():
    pool = redisUtil.redisPool()
    redis_client = redis.StrictRedis(connection_pool=pool)
    # publish/subscribe object
    pubsub_terminal = redis_client.pubsub()
    # subscribe for channel(s): football and F1
    pubsub_terminal.subscribe(REDIS_CHANNEL_0, REDIS_CHANNEL_2, REDIS_CHANNEL_3)
    # listen for channels that have been subscribed
    for item in pubsub_terminal.listen():
        # print(type(item), item.keys())
        # <class 'dict'> dict_keys(['type', 'pattern', 'channel', 'data'])
        itype = item['type']
        ipattern = item['pattern']
        ichannel = item['channel']
        idata = item['data']
        # print(itype,ipattern,ichannel,idata)
        print('Listen on channel: %s' %ichannel.decode())
        if item['type'] == 'message':
            # 如果itype是message, 则 TODO
            '!!TODO: detail algorithm or data process!!'
            print('From {} get message: {}'.format(ichannel.decode(), idata.decode()))
            # 根据pub端发布的end word判断是否已停止发布，若停止，则跳出for且取消订阅
            if idata.decode() == 'over':
                print('停止发布')
                break
    # 取消订阅
    pubsub_terminal.unsubscribe()
    print("订阅已取消")


if __name__ == '__main__':
    redisSubscribe()


