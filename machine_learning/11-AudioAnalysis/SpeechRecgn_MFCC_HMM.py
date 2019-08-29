# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:21:54 2018

@author: Administrator
"""

'''
语音识别：HMM隐马尔科夫模型和MFCC梅尔频率倒谱系数    ????????????
'''
import os
import warnings                         # 关闭警告
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf     # 语音特征提取模块
import hmmlearn.hmm as hl               # 隐马尔科夫模块
warnings.filterwarnings('ignore', category=DeprecationWarning)
np.seterr(all='ignore')


def search_speeches(directory, speeches):
    directory = os.path.normpath(directory)     # 标准化路径 Normalize path, eliminating double slashes, etc."""
    if not os.path.isdir(directory):
        raise(IOError('The directory' + directory + 'does not exist!'))
    for entry in os.listdir(directory):
        # 从路径右边开始找分隔符，最后一个分隔符后面的作为label
        label = directory[directory.rfind(os.path.sep) + 1:]
        # 路目录径和标签连接 --> 文件路径
        path = os.path.join(directory, entry)
        # 判断path是不是文件
        if os.path.isdir(path):                             # 判断path是不是文件
            search_speeches(path, speeches)                 # 不是则递归
        elif os.path.isfile(path) and path.endswith('.wav'):
            if label not in speeches:
                speeches[label] = []
                speeches[label].append(path)
'''
def normpath(path):
    """Normalize path, eliminating double slashes, etc."""
'''

train_speeches = {}
search_speeches('../ML/data/speeches/training', train_speeches)
#print(train_speeches)

train_x, train_y = [], []
for label, filenames in train_speeches.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            # 与label对应的mfccs
            mfccs = np.append(mfccs, mfcc, axis=0)      # 添加在数组的行上，不是列上，41行，42行...
    train_x.append(mfccs)
    train_y.append(label)

# 训练集 训练模型  隐马尔科夫
models = {}
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4,              # 4个中心 ？？？
                           covariance_type='diag',      # 皮氏距离， 协方差矩阵的对角线
                           n_iter=1000
                           )
    models[label] = model.fit(mfcc)                     # key:label; value:model


# test:
test_speeches = {}
search_speeches('../ML/data/speeches/testing', test_speeches)
#print(train_speeches)

test_x, test_y = [], []
for label, filenames in test_speeches.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            # 与label对应的mfccs
            mfccs = np.append(mfccs, mfcc, axis=0)      # 添加在数组的行上，不是列上，41行，42行...
    test_x.append(mfccs)
    test_y.append(label)


pred_test_y = []
for mfccs in test_x:
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(mfccs)                                   # 匹配度得分, 皮氏距离得分
        if (best_score is None) or (best_score < score):
            best_score = score                                      # best_score最高分存入score中
            best_label = label
    pred_test_y.append(best_label)

for y, pred_y in zip(test_y, pred_test_y):
    print(y, '->', pred_y)
#    apple -> lime
#    banana -> lime
#    kiwi -> lime
#    lime -> lime
#    orange -> lime
#    peach -> lime
#    pineapple -> lime
