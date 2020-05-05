# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:42:07 2018

@author: Administrator
"""

'''
单层多输出神经网络
'''

import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

data = np.loadtxt('../ML/data/mono.txt')    # 文本以空格sep的，不需要sep=' '
#print(data)
# [0.9 3.7 0.  0. ]
# [7.  4.  0.  1. ]   可视化输出有两个，可以考虑组合成一个值进行映射
#...
train_x, train_y = data[:,:2], data[:,2:]   # 前两列输入, 后两列输出

# 以下label_set主要方便画图:将两个输出映射为一个组合后的变量
train_labels = []
for train_row in train_y:
    train_row = train_row.astype(int).astype(str)
    train_labels.append('.'.join(train_row))
label_set = np.unique(train_labels)                         # label去重

train_codes = []                                            # label_set进行编码
for train_label in train_labels:
    train_code = np.where(label_set == train_label)[0][0]   # 索引作为编码
    train_codes.append(train_code)
train_codes = np.array(train_codes)

model = nl.net.newp([[train_x[:, 0].min(), train_x[:, 0].max()],
                      [train_x[:, 1].min(), train_x[:, 1].max()]], 2)

error = model.train(train_x, train_y,
                    epochs=10,
                    show=1,
                    lr=0.01)

# test
test_x = np.array([[0.3, 4.5],
                   [4.5, 0.5],
                   [4.3, 8.0],
                   [6.5, 3.5]])
# 模型预测
pred_test_y = model.sim(test_x)               # 神经网络中模型预测使用model.sim, 不是predict

pred_test_labels = []
for pred_test_row in pred_test_y:
    pred_test_row = pred_test_row.astype(int).astype(str)
    pred_test_labels.append('.'.join(pred_test_row))
pred_label_set = np.unique(pred_test_labels)

pred_test_codes = []                                            # label_set进行编码
for pre_test_label in pred_test_labels:
    pred_test_code = np.where(pred_label_set == pre_test_label)[0][0]   # 索引作为编码
    pred_test_codes.append(pred_test_code)
pred_test_codes = np.array(pred_test_codes)
#pred_test_codes = pred_test_codes.astype(float)
#print(pred_test_codes.dtype)
print(train_codes, pred_test_codes)
#[0 0 0 0 1 1 1 1 2 2 2 2 3 3 3 3] [0 1 2 2]


plt.figure('Monolayer_Neuron_', facecolor='lightgray')
plt.title('Monolayer_Neuron_',fontsize=20)
plt.xlabel('x', fontsize=14)
plt.ylabel('y',fontsize=14)
plt.tick_params(labelsize=10)
plt.scatter(train_x[:,0], train_x[:, 1], 
            c=train_codes,                  # 画图y需要时一维
#            cmap='jet',                    # 为什么可以不要cmap ???????
            alpha=1,
            label='Neuron'
            )
plt.scatter(test_x[:,0], test_x[:, 1], 
            c=pred_test_codes,             # 画图y需要时一维
#            cmap='jet',
            marker='^',
            alpha=1,
            label='Monolayer_Neuron_'
            )
plt.legend()

plt.figure('Training_Process', facecolor='lightgray')
plt.title('Training_Process',fontsize=20)
plt.xlabel('Epoch', fontsize=14)           # 预测类别为列
plt.ylabel('Error',fontsize=14)            # 实际类别为行
plt.tick_params(labelsize=10)
plt.plot(error,
         marker='o',
         c='r',
         alpha=0.5,
         label='Neuron'
         )
plt.legend()

plt.show()




