# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:04:08 2018

@author: Administrator
"""
'''
视频捕捉 人脸定位
'''

import cv2 as cv

fd = cv.CascadeClassifier('../ML/data/haar/face.xml')
ed = cv.CascadeClassifier('../ML/data/haar/eye.xml')
nd = cv.CascadeClassifier('../ML/data/haar/noise.xml')

vc = cv.VideoCapture(0)                             # 0 - 视频捕捉设备编号
while True:
    frame = vc.read()[1]                            # return 视频帧属性，取index=1的属性
    faces = fd.detectMultiScale(frame, 1.3, 5)      # 1.3, 5: 检测精度，扫描的力度和步长(0-10通常)
                                                    # faces 保存脸的位置和区域大小
    for l, t, w, h in faces:                        #  人脸区域左上角坐标(l, t), w 人脸区域宽度， h 区域高度  ?? 左下角坐标？？
        a, b = int(w / 2), int(h / 2)               # 确定椭圆圆心，人脸区域的中心位置 (a,b)=(w/2,h/2) 即椭圆的长短轴半径
        cv.ellipse(frame,                           # 画布，在frame即截取的视频帧上直接画椭圆
                   (l+a, t+b),                      # 椭圆圆心
                   (a, b),                          # (横轴半径，纵轴半径)
                   0, 0, 360,                       # rotation_angle, startAngle, endAngle
                   (255,0,255),                     # color 线条颜色
                   2                                # 线宽
                   )
        face = frame[t:t + h, l:l+w]                # 坐标轴

        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:                     #  人脸区域左上角坐标(l, t), w 人脸区域宽度， h 区域高度  ?? 左下角坐标？？
            a, b = int(w / 2), int(h / 2)           # 确定椭圆圆心，人脸区域的中心位置 (a,b)=(w/2,h/2) 即椭圆的长短轴半径
            cv.ellipse(face,                        # 画布，在face上直接画椭圆
                       (l+a, t+b),                  # 椭圆圆心
                       (a, b),                      # (横轴半径，纵轴半径)
                       0, 0, 360,                   # rotation_angle, startAngle, endAngle
                       (0,255,0),                   # color 线条颜色
                       2                            # 线宽
                       )
        noses = nd.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in noses:                    #  人脸区域左上角坐标(l, t), w 人脸区域宽度， h 区域高度  ?? 左下角坐标？？
            a, b = int(w / 2), int(h / 2)           # 确定椭圆圆心，人脸区域的中心位置 (a,b)=(w/2,h/2) 即椭圆的长短轴半径
            cv.ellipse(face,                        # 画布，在face上直接画椭圆
                       (l+a, t+b),                  # 椭圆圆心
                       (a, b),                      # (横轴半径，纵轴半径)
                       0, 0, 360,                   # rotation_angle, startAngle, endAngle
                       (255,0,0),                   # color 线条颜色  b
                       2                            # 线宽
                       )
        
    cv.imshow('VideoCapture', frame)
    
    if cv.waitKey(33) == 27:
        '''
        # 27为ESC按键， 33ms(1s看30张图片相当于连续的图片动图串成视频，即帧速率30fps/s) 表示30fps 帧速率 30帧/s
        '''
        break

vc.release()                         # 使用完后释放视频设备
cv.destroyAllwindows()               # 销毁所有窗口，包括隐藏窗口 如缓存

