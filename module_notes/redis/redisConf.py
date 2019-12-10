# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-21 18:59:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-12-04 14:48:09

'''
redis参数
'''

REDIS_HOST = '192.168.1.215'
REDIS_PORT = 6379
REDIS_DB_TEST = 15
REDIS_PASSWORD = 'spindle123456'

REDIS_CHANNELS = ['192.168.1.1', 'collection-status', 'unbalance-step','nullchannel']
REDIS_TOPICS = ['group1']

# STEP_INDEX: 步骤序号，如果前端传入的序号为-1，则停止获取采集数据
STEP_INDEX = [1,2,3,4]

