# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:56:50 2018

@author: Administrator
"""

import pickle                              # 硬盘存储模块
import numpy as np
import sklearn.linear_model as lm          # 线性模型模块
import sklearn.metrics as sm               # 模型评估模块
import matplotlib.pyplot as plt
import sklearn.pipeline as spl             # 
import sklearn.preprocessing as sp

# traning datas
train_x, train_y = [], []
# 读取文件
with open('single.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        train_x.append(data[:-1])
        train_y.append(data[-1])
train_x = np.array(train_x)                 # 训练数据集必须为array或者array_like
train_y = np.array(train_y)                 # 训练数据集必须为array或者array_like
#print(x.shape, y.shape)

'''
模型建立
sklearn.linear_model.LinearRegression()
    --> return：线性回归器
                线性回归器.fit(输入样本，输出标签)                # 训练数据
                线性回归器.predict(输入样本)                      # 预测数据
                    -- > return：预测输出标签
'''
model_ln = lm.LinearRegression()               # 构建线性回归器
model_ln.fit(train_x, train_y)                 # 训练数据  不返回k和b model中存储
pred_y_ln = model_ln.predict(train_x)

'''
岭回归 (削弱异常值对拟合的影响,正则强度越大，削弱的越厉害，降低对异常数据的依赖)
loss = J(k, b) + 正则函数(样本权重)*正则强度(或惩罚系数）         # 正则项：可以防止过拟合
sklearn.linear_model.Ridge(正则强度,
                           fit_intercept=是否修正截距，
                           max_iter=最大迭代次数)
    --> return：岭回归器
                岭回归器.fit()                      # 训练数据
                岭回归器.predict()                  # 预测数据
'''
model_rd = lm.Ridge(150, fit_intercept=True, max_iter=10000)     # 构建线性回归器
model_rd.fit(train_x, train_y)                                   # 训练数据  不返回k和b model中存储
pred_y_rd = model_rd.predict(train_x)

'''
多项式回归
sklearn.preprocessing.PolynomialFeatures(最高次数)
    --> return：多项式特征扩展器
sklearn.pipeline.make_pipeline(多项式特征扩展器, 线性回归器)         # 管线函数 pipeline模块 后续需要再研究？？？
    --> return：k1,k2,k3...
x-->多项式特征扩展器 -- x x^2 x^3 ... --> 线性回归器 ---> k1,k2,k3...
'''
# 构建模型：训练数据train
model_poly = spl.make_pipeline(sp.PolynomialFeatures(7),lm.LinearRegression())  # 构建多项式特征扩展器
model_poly.fit(train_x, train_y)                                                # 训练数据集
pred_train_y = model_poly.predict(train_x)                                      # 根据训练集进行训练数据的预测
# 拟合模型性能评估R^2
est_error = sm.r2_score(train_y, pred_train_y)                                  # R-square：模型决定系数R^2
# R^2:
#    越接近1，表明方程的变量对y的解释能力越强，这个模型对数据拟合的也较好
#    越接近0，表明模型拟合的越差
#    经验值：>0.4， 拟合效果好
# R^2缺点：数据集的样本越大，R²越大，因此，不同数据集的模型结果比较会有一定的误差
print(est_error)

# 使用模型，预测数据test: 利用多项式模型进行数据测试test
#test_x = np.linspace(train_x.min(), train_y.max(), 1001)[:,np.newaxis]  # np.newaxis新增一个列--> 2-dim
test_x = np.linspace(train_x.min(), train_y.max(), 1001)        # .shape == (1001,)
# 一维数组 -->  二维数组(单纯增加一个列)
test_x = test_x.reshape((test_x.shape[0],-1))                   # (1001, 1),数组test_x行数:test_x.shape[0]; 列数：任意多列
pred_test_y = model_poly.predict(test_x)
'''
By default, the input is converted to an at least 2D numpy array

'''


## 评估模型
#print(sm.mean_absolute_error(y, pred_y_ln))        # 平均绝对误差
#print(sm.mean_squared_error(y, pred_y_ln))         # 均方差
#print(sm.median_absolute_error(y, pred_y_ln))      # 中位数绝对误差
#print(sm.r2_score(y, pred_y_ln))                   # LR模型推荐使用sm.r2_score评估 coefficient of determination
#
# 模型写入硬盘 pkl格式 方便pickle模块读取
with open('linear.pkl', 'wb') as f:                 # pickle.dump() 与 pickle.dumps()有什么区别 ???????
    pickle.dump(model_ln, f)
with open('ridge.pkl', 'wb') as f:
    pickle.dump(model_rd, f)
with open('polynomial.pkl', 'wb') as f:
    pickle.dump(model_poly, f)
    

'''
可视化
'''
plt.figure('Regressions', facecolor='lightgray')
plt.title('Regressions', fontsize=20)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

# 输入样本散点图
plt.scatter(train_x, train_y, label='Sample', color='black',linewidth=1,alpha=0.8)
# 绘制线性回归和岭回归拟合图（由于训练集的点x不是有排列的，因此作为x轴画图时需要先对点按x进行排序）
sorted_indices = train_x.T[0].argsort()       # train_x 不是有序的，需要进行排序                    ??????
plt.plot(train_x[sorted_indices], pred_y_ln[sorted_indices], 'o-', label='LinearRegression', color='g',linewidth=1,alpha=1)
plt.plot(train_x[sorted_indices], pred_y_rd[sorted_indices], 'o-', label='RidgeRegression', color='b',linewidth=1,alpha=1)
# 绘制多项式回归拟合图
plt.plot(test_x, pred_test_y, label='PolynomialRegression', color='r',linewidth=2,alpha=1)

plt.legend(fontsize=8, loc='upper left')
plt.show()






'''
def r2_score(y_true, y_pred, sample_weight=None,
             multioutput="uniform_average"):
    """R^2 (coefficient of determination) regression score function.

    Best possible score is 1.0 and it can be negative (because the
    model can be arbitrarily worse). A constant model that always
    predicts the expected value of y, disregarding the input features,
    would get a R^2 score of 0.0.
'''

'''
def normalize(X, norm='l2', axis=1, copy=True, return_norm=False):
    """Scale input vectors individually to unit norm (vector length).
    Read more in the :ref:`User Guide <preprocessing_normalization>`.
    Parameters
    ----------
    X : {array-like, sparse matrix}, shape [n_samples, n_features]
        The data to normalize, element by element.
        scipy.sparse matrices should be in CSR format to avoid an
        un-necessary copy.
        
def transform(self, X):
        """Transform data to polynomial features
        Parameters
        ----------
        X : array-like, shape [n_samples, n_features]
            The data to transform, row by row.

def fit(self, X, y=None):
        """
        Compute number of output features.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The data.
            
dir(sklearn.pipeline)：         
    ['Bunch', 'FeatureUnion', 'Memory', 'Parallel', 'Pipeline', 'TransformerMixin', 
    '_BaseComposition', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
    '__loader__', '__name__', '__package__', '__spec__', '_fit_one_transformer', '_fit_transform_one', 
    '_name_estimators', '_transform_one', 'check_memory', 'clone', 'defaultdict', 'delayed', 
    'if_delegate_has_method', 'make_pipeline', 'make_union', 'np', 'six', 'sparse']
'''