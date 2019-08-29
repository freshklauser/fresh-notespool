# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:47:11 2018

@author: Administrator
"""
'''
1. 分类边界
同时满足四个条件：
    A. 正确分类
    B. 支持向量到分类边界的距离相等
    C. 间距最大
    D. 线性（直线，平面）
2. 升维变换（如二维不可分 --> 三维可分）
对于在低纬度空间中无法线性划分的样本，通过升维变换，在高纬度空间寻找最佳线性分类边界。
核函数：用于对特征值进行升维变换的函数
  线性核函数   linear
	多项式核函数 poly
	径向基核函数 rbf
代码：svm_line.py, svm_poly.py
3. 当不同类别的样本数量相差悬殊时，样本数较少的类别可能被支持向量机分类器忽略，为此可以通
过class_wieght参数指定为balanced， 通过调节不同类别样本的权重，均衡化。
model = svm.SVC(kernel='linear', class_weight='balanced')

4. 置信概率
svm.SVM(..., probability=True,..)   
支持向量机分类器.predict_proba(输入样本) --> 置信概率矩阵
	类别1    类别2
样本1 -> 0.99	  0.01
样本2 -> 0.02	  0.98
'''

'''
代码如下：
'''

import numpy as np















