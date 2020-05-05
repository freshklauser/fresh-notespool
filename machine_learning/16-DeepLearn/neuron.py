# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:42:07 2018

@author: Administrator
"""

'''
神经元
def newp(minmax, cn, transf=trans.HardLim()):
    """
    Create one layer perceptron
    :Parameters:
        minmax: list of list, the outer list is the number of input neurons, 
			inner lists must contain 2 elements: min and max
            Range of input value
        cn: int, number of output neurons
            Number of neurons
        transf: func (default HardLim)
            Activation function
'''

import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

x = np.array([[0.3, 0.2],               # 输入层
              [0.1, 0.4],
              [0.4, 0.6],
              [0.9, 0.5]])
y = np.array([[0], 
              [0], 
              [0], 
              [1]])                     # 输出层,严格要求列向量，与x一一对应

# 模型
model = nl.net.newp([[0, 1], [0, 1]],   # 输入范围，即特征值域  格式[....]
                    1                   # 输出的个数
                    )
# 训练模型
error = model.train(x, y, 
                    epochs=50,          # epochs:训练的最大次数
                    show=1,             # 是否显示 show=n 次训练后的误差
                    lr=0.01             # 学习率，k'=k - alpha 偏导
                    )

plt.figure('Neuron', facecolor='lightgray')
plt.title('Neuron',fontsize=20)
plt.xlabel('x', fontsize=14)           # 预测类别为列
plt.ylabel('y',fontsize=14)            # 实际类别为行
plt.tick_params(labelsize=10)
plt.scatter(x[:,0], x[:, 1], 
            c=y.ravel(),               # 画图y需要时一维
            cmap='brg',
            alpha=0.5,
            label='Neuron'
            )
plt.legend()


plt.figure('Training_Process', facecolor='lightgray')
plt.title('Training_Process',fontsize=20)
plt.xlabel('Epoch', fontsize=14)           # 预测类别为列
plt.ylabel('Error',fontsize=14)            # 实际类别为行
plt.tick_params(labelsize=10)
plt.plot(error,
         c='r',               # 画图y需要时一维
         alpha=0.5,
         label='Neuron'
         )
plt.legend()
plt.show()



