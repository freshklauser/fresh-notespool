# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:40:43 2019
@author: Klaus
决策边界 decision_boundary
"""
import numpy as np
import matplotlib.pyplot as plt

def plt_decision_boundary(model,X,y):
    '''
    利用 plt.pcolormesh 或者 plt.contour 绘制决策边界
    
    参数：
        model: 算法模型
            调用model时：model --> lambda x: model_fitted.predict(x)
            model_fitted：训练好的模型
        X:数据集输入，维度：(n_features,m_train)
        y:数据集标签，维度：(n_output,m_train)
            n_features:数据集的特征数
            m_train / m_test: 样本数量
            n_output:分类模型的分类类别数
    Notes:
        X和y的维度都遵循：一行一特征，一列一样本
        
    Tips:
        np.squeeze(y): (1,9) --> (9,)       
        
    eg:plt_decision_boundary(lamda x:clf.predict(x), X,y)
    '''
    
    # Define the boundary scope and step size of the grip area
    l, r, h = X[0, :].min() - 1, X[0, :].max() + 1, 0.005 # 左边界，右边界，水平方向点间距
    b, t, v = X[1, :].min() - 1, X[1, :].max() + 1, 0.005 # 下边界，上边界，垂直方向点间距
    
    # Generate a grid of points with distance h and v between them
    xx, yy = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
    
    # Predict the function value for the whole grid:flatten and predict, then reshape
    flat_x = np.c_[xx.ravel(), yy.ravel()]                # all points  in the grids as the input of model
    flat_y = model.predict(flat_x)                        # prediction for all points in the grids
    Z = flat_y.reshape(xx.shape)
    
    # Plot the decision_boundary
    '''
    two methods to plot:
        # plt.pcolormesh()
        plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Spectral)
        # plt.contour()
        plt.contour(xx, yy, Z, cmap=plt.cm.Spectral)
    '''
    # plt.pcolormesh()
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    # plt scatter of samples
    plt.scatter(X[0, :], X[1, :], c=np.squeeze(y), cmap='brg', s=60)