# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:21:54 2018

@author: Administrator
"""
'''
MFCC:  ???????????????????????
'''

import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import python_speech_features as sf                 # 音频特征提取模块

sample_rate, sigs = wf.read('../ML/data/speeches/training/apple/apple02.wav')  # ./ML 当前目录的ML文件夹， ../ML 上一级目录的ML文件夹
mfcc = sf.mfcc(sigs, sample_rate)                   # MFCC矩阵   (40, 13)  40个时域区间矩阵图y，13个关键频率矩阵图x
#print(type(mfcc))

'''
画矩阵：plt.imshow()--热像图  /  plt.matshow()
def matshow(A, fignum=None, **kw):
    Display an array as a matrix in a new figure window.
'''
plt.matshow(mfcc, 
            cmap='gist_rainbow',
            fignum='MFCC'
            )

plt.title('MFCC')
plt.xlabel('Feature')
plt.ylabel('Sample')
plt.tick_params(which='both', top=False, labeltop=False, labelbottom=True, labelsize=10)

plt.show()
plt.savefig('apple02.png')