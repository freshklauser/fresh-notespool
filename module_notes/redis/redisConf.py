# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-21 18:59:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-21 20:19:32

'''
redis参数
'''

REDIS_HOST = '192.168.1.215'
REDIS_PORT = 6379
REDIS_DB_TEST = 15
REDIS_PASSWORD = 'spindle123456'

REDIS_CHANNEL_LIST = []
REDIS_CHANNEL_0 = 'flag'        # channel-0: 监听是否收到停止发布的信息,flag的内容为over则stop
REDIS_CHANNEL_LIST.append(REDIS_CHANNEL_0)
REDIS_CHANNEL_1 = 'spindle_collection'
REDIS_CHANNEL_LIST.append(REDIS_CHANNEL_1)
REDIS_CHANNEL_2 = 'football'
REDIS_CHANNEL_LIST.append(REDIS_CHANNEL_2)
REDIS_CHANNEL_3 = 'F1'
REDIS_CHANNEL_LIST.append(REDIS_CHANNEL_3)

