# -*- coding: utf-8 -*-

'''
ORC识别 
'''
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import neurolab as nl
import pickle
import time

charset = 'abcdefghijklmnopqrstuvwxyz'                  # 待编码字母表：全部用来对应编码
'''
字母编码原理(25个0和1个1组成)：
  a b c d e f g h i j k l m n o p q r s t u v w x y z
c 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
m 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0   (字母出现的位置设为1, 其他全为0, 形成26个英文字母的独热编码)
......
'''

x, y = [], []
with open('ocrdb.dat', 'r') as f:            # ocrdb.dat存储数据 字母和字母图片： 128个(1 or 0)表示
    for line in f.readlines():
        items = line.split('\t')
        char, image = items[1], items[6:-1]             # char: 手写的字母， image:写字母的图片(128个0或1)
        '''
        独热编码, 判断 items[1]即字母是否在待编码字母表中, 在则进行编码并将编码后的数据传入数据集
        '''
        if char in charset:
            code = np.zeros(len(charset), dtype=int)    # 生成字符集等长的编码zeros数组
            code[charset.index(char)] = 1               # 字符在charset中的位置作为index, 值设为1
            '''
            编码后的char作为输出即分类的类别传给标签label集 y;  image作为输入传给数据集 x
            '''
            y.append(code)                              # code(array格式)作为 输出label集的元素
            x.append(np.array(image, dtype=int))        # image转化为数组作为 输入数据集的元素
            if len(x) >= 30:                            # 取30个输入样本，方便代码执行演示
                break

x = np.array(x)                                         # 128： 字母图片： 128个(1 or 0)表示
y = np.array(y)                                         # 26：字母的编码-- 25个0和1个1组成
print(x.shape, y.shape)                                # (30, 128) (30, 26)

...
'''
划分训练集
'''
train_size = int(len(x) * 0.8)
train_x, train_y = x[:train_size], y[:train_size]
test_x, test_y = x[train_size:], y[train_size:]


'''
测试集：测试集可以直接按20%划分，这里由于只编码了样本前30个字母数据，因此有针对性的选取测试集进行模型测试
理论上: 
    1) 取样本head_10字母数据'ommandingo',由于前30个样本都进行了编码，因此模型都应该能够正确匹配
        result: ommandingo -> ommandingo
    2) 取样本tail_10字母数据'sequential',有部分是没经过编码的，因此只有在前30个样本中出现过的字母才可能正确匹配
        result: sequential -> dmdoonming
'''
# test_x, test_y = [], []
# #with open('../ML/data/ocrtest_head10.dat', 'r') as f:   # ocrtest_head10.dat中的字母：ommandingo
# with open('../ML/data/ocrtest_tail10.dat', 'r') as f:   # ocrtest_tail10.dat中的字母：sequential
#     for line in f.readlines():
#         items = line.split('\t')
#         char, image = items[1], items[6:-1]
#         # 独热编码
#         if char in charset:
#             code = np.zeros(len(charset), dtype=int)
#             code[charset.index(char)] = 1
#             test_y.append(code)
#             test_x.append(np.array(image, dtype=int))
# test_x = np.array(test_x)
# test_y = np.array(test_y)
# print('test_y:', test_y,sep='\n')
#[[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0]
# [0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#...


'''
模型参数初始化：
def newff(minmax, size, transf=None):
    Create multilayer perceptron   多层感知器
        minmax: list of list,the outer list is the number of input neurons,
                inner lists must contain 2 elements: min and max(神经元个数即训练集特征的个数)
                针对该数据集,输入为image即128个(1 or 0),即有128个神经元，minmax是有128个 list元素 的list,
                每个list元素的元素取值均为0或1，范围即[0,1], list元素==[0,1].
        size: [128, 16, y.shape[1]]--2层隐藏层，第一层128个神经元，第二层16个神经元，输出层神经元个数=y.shape[1]
'''
input_ranges = []
for _ in x.T:                                       # 循环生成参数 minmax
    input_ranges.append([0, 1])                     # 有多少列，model的第一个参数就要有多少个min和max即范围
'''
建立模型：多层感知器模型 nl.net.newff(minmax, size, transf=None)
指定模型训练使用的算法函数：model.trainf=nl.train.train_gd 梯度下降 （详见code_end）
'''
print('##########################################')
print('Start Processing the model...')

time1 = time.perf_counter()
print(time1)

model = nl.net.newff(input_ranges, [128, 16, y.shape[1]])
model.trainf = nl.train.train_gd        # 模型训练使用的函数：gradientdown 梯度下降
# 模型误差：
error = model.train(train_x,                        # 训练集输入
                    train_y,                        # 训练集输出
                    epochs=100000,                   # 训练的最大次数
                    show=500,                       # 每训练500次打印error
                    goal=0.05                       # 目标误差
                    )
#Epoch: 500; Error: 93.29025971348494;
#Epoch: 1000; Error: 93.91877180275394;
#...

'''
模型预测：神经网络中模型预测使用model.sim, 不是predict
def sim(self, input):
    Simulate a neural network
    :Parameters:
        input: array like,  array input vectors
    :Returns:
        outputs: array like,  array output vectors
'''
pred_test_y = model.sim(test_x)                     # test_x格式,array like, 不能是list

time2 = time.perf_counter()
print('Training model time uses: {}'.format(time2-time1))

# 模型写入硬盘 pkl格式 方便pickle模块读取
with open('OCR_newff.pkl', 'wb') as f:
    pickle.dump(model, f)

'''
自定义解码函数：
code.argmax():即1在26位编码中的位置,即index(其他25个位置全是0)
charset[code.argmax()]:根据index获得charset的字母元素
'''
def decode(codes):
    return ''.join(charset[code.argmax()] for code in codes)

true_str = decode(test_y)                           # test_y解码即原测试集真是字母
pred_str = decode(pred_test_y)                      # pred_test_y解码为模型预测的字母
print(true_str, '->', pred_str)                     # tail_10: sequential -> dmdoonming
                                                    # head_10: ommandingo -> ommandingo

'''
plt.subplots ??????????????????????????????????????????????
'''
axes= plt.subplots(1, len(test_x), num='OCR')[1]
for ax, char_image, true_char, pred_char in zip(axes, test_x, true_str, pred_str):
    ax.matshow(char_image.reshape(16, 8), cmap='brg')
    ax.set_title('{}{}{}'.format(true_char, '==' if true_char == pred_char else '!=', pred_char),
                 fontsize=8,
                 color='b' if true_char == pred_char else 'g'
                 )
    ax.set_xticks(())
    ax.set_yticks(())

'''
绘图：Error~Epoch 曲线
'''
plt.figure('Training_Process', facecolor='lightgray')
plt.title('Training_Process',fontsize=20)
plt.xlabel('Epoch', fontsize=14)
plt.ylabel('Error',fontsize=14)
plt.tick_params(labelsize=10)
plt.plot(error,
         c='r',
         alpha=0.5,
         label='Neuron'
         )
plt.legend()
plt.show()





'''
模型训练使用的算法
help(nl.train)
Help on package neurolab.train in neurolab:

NAME
    neurolab.train

DESCRIPTION
    Train algorithms based  gradients algorithms
    ===========================================
    
    .. autofunction:: train_gd
    .. autofunction:: train_gdm
    .. autofunction:: train_gda
    .. autofunction:: train_gdx
    .. autofunction:: train_rprop
    
    Train algorithms based on Winner Take All - rule
    ================================================
    .. autofunction:: train_wta
    .. autofunction:: train_cwta
    
    Train algorithms based on spipy.optimize
    ========================================
    .. autofunction:: train_bfgs
    .. autofunction:: train_cg
    .. autofunction:: train_ncg
    
    Train algorithms for LVQ networks
    =================================
    .. autofunction:: train_lvq
    
    Delta rule
    ==========
    
    .. autofunction:: train_delta

PACKAGE CONTENTS
    delta
    gd
    lvq
    spo
    wta

FUNCTIONS
    trainer(Train, **kwargs)
        Trainner init
'''

