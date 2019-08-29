# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:21:54 2018

@author: Administrator
"""

import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import numpy.fft as nf

sample_rate, sigs = wf.read('../ML/data/freq.wav')  # ./ML 当前目录的ML文件夹， ../ML 上一级目录的ML文件夹
print(sample_rate)                          # 44100 采样率
print(sigs.shape)                           # (132300,)  单声道 一列
print('time_wav = ', sigs.shape[0] / sample_rate, 's')      # 音频播放时长
print(sigs[:5])                             # [ -3893 -18346 -10040  19031  30756] / 2**15 == 声场强度
sigs = sigs / 2 ** 15
print(sigs)
#[-0.11880493 -0.55987549 -0.30639648  0.58078003  0.93859863  0.17752075
# -0.40713501 -0.37188721  0.23010254  0.79000854  0.60708618 -0.33999634
# -0.45401001 -0.03741455  0.72381592  0.71847534 -0.00985718 -0.65844727
# -0.23483276  0.56091309  0.84158325  0.03463745 -0.5508728  -0.49267578
#  0.39089966  0.89395142  0.54898071 -0.48608398 -0.44085693  0.05752563]

times = np.arange(sigs.shape[0]) / sample_rate
freqs = nf.fftfreq(len(sigs), 
                   d=1/sample_rate          # 采样周期 = 1/ 采样频率
                   )
ffts = nf.fft(sigs)                         # 快速傅里叶变换
pows = np.abs(ffts)



plt.figure('Audio_Signal', facecolor='gray')
plt.title('Audio_Signal')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.plot(times, sigs, '-', c='purple', label='Signal')
plt.legend()

plt.figure('Audio_Frequency', facecolor='gray')
plt.title('Audio_Frequency')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.plot(freqs[freqs>=0], pows[freqs>=0], '-', c='g', label='Frequency')

plt.legend()
plt.show()