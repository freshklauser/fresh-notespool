# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:04:08 2018

@author: Administrator
"""
'''
视频捕捉
'''

import cv2 as cv

vc = cv.VideoCapture(0)              # 0 - 视频捕捉设备编号
while True:
    frame = vc.read()[1]             # return 视频帧属性，取index=1的属性
    cv.imshow('VideoCapture', frame)
    
    if cv.waitKey(33) == 27:
        '''
        # 27为ESC按键， 33ms(1s看30张图片相当于连续的图片动图串成视频，即帧速率30fps/s) 表示30fps 帧速率 30帧/s
        '''
        break

vc.release()                         # 使用完后释放视频设备
cv.destroyAllwindows()               # 销毁所有窗口，包括隐藏窗口 如缓存

