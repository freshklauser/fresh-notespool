# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-21 18:59:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-12-04 15:07:41

'''
python操作redis 发布/订阅模式的订阅客户端
publish [channel] [content]      # 将信息发送到指定的频道
subscribe channel [channel] ...  # 可以订阅一个或多个频道
TODO:
    不同的channel下执行的程序不一样
    收到信息后的反馈信息交互：
        后端接收到前端的数据后，publish状态信息到
'''

import redis
import redisUtil
from redisConf import *

msg_list = []

def redisSubscribe():
    pool = redisUtil.redisPool()
    redis_client = redis.StrictRedis(connection_pool=pool)
    # publish/subscribe object
    pubsub_terminal = redis_client.pubsub()
    # subscribe for channel(s): football and F1
    pubsub_terminal.subscribe(REDIS_CHANNELS)
    # listen for channels that have been subscribed
    for item in pubsub_terminal.listen():
        # print(type(item), item.keys())
        # <class 'dict'> dict_keys(['type', 'pattern', 'channel', 'data'])
        itype = item['type']
        ipattern = item['pattern']
        ichannel = item['channel']
        idata = item['data']
        # print(itype,ipattern,ichannel,idata)
        if item['type'] == 'message':
            # 如果itype是message，则继续
            if ichannel.decode() == REDIS_CHANNELS[-1]:
                print('From "{}"" get message: {}'.format(ichannel.decode(), idata.decode()))
                print('Default target channels: {}'.format(REDIS_CHANNELS[:-1]))
            else:
                print('Listen on channel: %s' %ichannel.decode())
                # 储存chn和msg至列表中，可保存至本地
                msg_list.append((ichannel.decode(), idata.decode()))
                # print(idata, idata.decode(), type(int(idata.decode())))   # b'1' 1 <class 'int'>
                '!!TODO: detail algorithm or data process!!'
                if int(idata.decode()) in STEP_INDEX:
                    'TODO: 从kafka取数据 (采集数据一直运行中)'
                    'TODO: 计算程序 (采集数据一直运行中)'
                    add(msg_list)
                else:
                    print("Step is out of index range {}.".format(STEP_INDEX))
                # 根据pub端发布的end word判断是否已停止发布，若停止，则跳出for且取消订阅
                # print('---------------', msg_list)
                if int(idata.decode()) == -1:
                    print('停止发布')
                    'TODO: 停止采集程序'
                    break
    # 取消订阅
    pubsub_terminal.unsubscribe()
    print("订阅已取消")
    return msg_list

def add(x):
    print("params %s." % x)



if __name__ == '__main__':
    print('订阅')
    flag_run = 1
    # while flag_run:
    info = redisSubscribe()
    # print(info)
        # step_index = info


