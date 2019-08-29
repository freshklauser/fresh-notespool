# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:23:11 2018

@author: Administrator
"""
'''
SVM回归：交通状况预测
'''

import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm

# 自定义编码器：数字编码
class DigitEncoder():
    def fit_transform(self, y):
        return y.astype(int)
    
    def transform(self, y):
        return y.astype(int)
    
    def inverse_transform(self, y):
        return y.astype(str)
    
data = []
with open('traffic.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
    if data[row, 0].isdigit():                                              # 数字，用自定义的encoder
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()                                         # 非数字，用sp的标签编码器
    if row < len(data) - 1:                                                 # 前n-1行 x, 最后一行y
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])                                # y: <class 'numpy.ndarray'>
    encoders.append(encoder)
x = np.array(x).T

# 测试集和训练集划分
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)

model = svm.SVR(kernel='rbf', C=10)                                         # 支持向量机回归模型 SVR
# 交叉验证评估模型：测试f1_score
#print('f1_score:',ms.cross_val_score(model, x, y, cv=3, scoring='f1_weighted').mean())
# 0.938166292765643 fi_score可以，采用该参数组训练模型

model.fit(train_x, train_y)                                                 # 训练集训练模型
pred_test_y = model.predict(test_x)                                         # 测试集测试模型
# r^2score
print('r2_score:',sm.r2_score(test_y, pred_test_y))
print('pred_test_y:',pred_test_y[:10])                                      # pred_test_y: [1 1 1 1 1 1 1 1 1 1]


# 根据输入数据利用SVM模型进行分类预测
data = [['Tuesday','13:35','San Francisco','yes']]
data = np.array(data).T
print(data)
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))                                  # 使用已有的编码器
x = np.array(x).T
pred_y = model.predict(x)
output_y = encoders[-1].inverse_transform(pred_y)                           # 解码
print('pred_y:', pred_y)                                                    # pred_y: [22.49716868]
print('output_y:', output_y)                                                # output_y: ['22.497168681114907']



'''
class SVR(sklearn.svm.base.BaseLibSVM, sklearn.base.RegressorMixin)
 |  Epsilon-Support Vector Regression.
 |  
 |  The free parameters in the model are C and epsilon.
 |  
 |  The implementation is based on libsvm.
 |  
 |  Read more in the :ref:`User Guide <svm_regression>`.
 |  
 |  Parameters
 |  ----------
 |  C : float, optional (default=1.0)
 |      Penalty parameter C of the error term.
 |  
 |  epsilon : float, optional (default=0.1)
 |       Epsilon in the epsilon-SVR model. It specifies the epsilon-tube
 |       within which no penalty is associated in the training loss function
 |       with points predicted within a distance epsilon from the actual
 |       value.
 |  
 |  kernel : string, optional (default='rbf')
 |       Specifies the kernel type to be used in the algorithm.
 |       It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or
 |       a callable.
 |       If none is given, 'rbf' will be used. If a callable is given it is
 |       used to precompute the kernel matrix.
 |  
 |  degree : int, optional (default=3)
 |      Degree of the polynomial kernel function ('poly').
 |      Ignored by all other kernels.
 |  
 |  gamma : float, optional (default='auto')
 |      Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.
 |      If gamma is 'auto' then 1/n_features will be used instead.
 |  
 |  coef0 : float, optional (default=0.0)
 |      Independent term in kernel function.
 |      It is only significant in 'poly' and 'sigmoid'.
 |  
 |  shrinking : boolean, optional (default=True)
 |      Whether to use the shrinking heuristic.
 |  
 |  tol : float, optional (default=1e-3)
 |      Tolerance for stopping criterion.
 |  
 |  cache_size : float, optional
 |      Specify the size of the kernel cache (in MB).
 |  
 |  verbose : bool, default: False
 |      Enable verbose output. Note that this setting takes advantage of a
 |      per-process runtime setting in libsvm that, if enabled, may not work
 |      properly in a multithreaded context.
 |  
 |  max_iter : int, optional (default=-1)
 |      Hard limit on iterations within solver, or -1 for no limit.
'''