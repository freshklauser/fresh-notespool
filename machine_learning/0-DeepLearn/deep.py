# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:42:07 2018

@author: Administrator
"""

'''
深度神经网络
'''

import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt


train_x = np.linspace(-10, 10, 100)
train_y = 2 * np.square(train_x) + 7
# 归一化
train_y /= np.linalg.norm(train_y)              # np.linalg.norm?????????

train_x = train_x.reshape(-1,1)
train_y = train_y.reshape(-1,1)

# 深度学习的模型 forward
model = nl.net.newff([[train_x.min(), train_x.max()]],
                       [10, 10, 1]                  # 2层隐藏层,每层10个神经元, 只有1个输出
                       )
model.trainf = nl.train.train_gd                # 算法函数：gradiendown 梯度下降-- 算误差
error = model.train(train_x, train_y,
                    epochs=800,
                    show=20,                    # 每20次后显示误差
                    goal=0.01                   # 目标误差值
                    )


# test
test_x = np.linspace(-10, 10, 1000)
test_x = test_x.reshape(-1,1)
pred_test_y = model.sim(test_x)




plt.figure('Deep_Neural_Network', facecolor='lightgray')
plt.title('Deep_Neural_Network',fontsize=20)
plt.xlabel('x', fontsize=14)
plt.ylabel('y',fontsize=14)
plt.tick_params(labelsize=10)

plt.plot(train_x, train_y,
         c='dodgerblue',
         alpha=1,
         label='Training'
         )
plt.plot(test_x, pred_test_y,
         c='limegreen',
         alpha=1,
         label='Training'
         )
plt.legend()

plt.figure('Training_Process', facecolor='lightgray')
plt.title('Training_Process',fontsize=20)
plt.xlabel('Epoch', fontsize=14)           # 预测类别为列
plt.ylabel('Error',fontsize=14)            # 实际类别为行
plt.tick_params(labelsize=10)
plt.plot(error,
         c='r',
         alpha=1,
         label='testing'
         )
plt.legend()

plt.show()




