# -*- coding: utf-8 -*-
'''
图像识别：基于HMM模型和特征描述矩阵的图像识别
目前代码问题：
    1）只能在已确定标签范围内才能正确实现分类，对标签范围外的图片 会分到已知标签类，导致未知类别的错误分类。
该模型有监督分类中，遍历训练集，只获得了三种分类，即label只有3个，增加label以外的图片不会报错，而是会强制近似匹配
分配到已有类别中 
    2）正确图片放到其他分类中识别时，会识别出错

'''

import os
import warnings
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hmm

warnings.filterwarnings('ignore',
                        category=DeprecationWarning)
np.seterr(all='ignore')

'''
search_objects作用：遍历文件夹，返回 {类别标签label: image访问路径}，字典对象 key-label; value-image_path
    label == train数据集中image所在文件夹的filename
'''
def search_objects(directory):
    directory = os.path.normpath(directory)             # Normalize path, eliminating double slashes, etc."""
    if not os.path.isdir(directory):                    # os.path.isdir(file):判断file是不是文件夹即目录
        raise IOError('The directory' + directory + 'does not exist!')
                                                        # 不是目录，则生成错误
    objects = {}                                        # 定义字典对象，label作为key,文件(图片)完整路径作为value
    '''
    os.walk(): Directory tree generator.yields a 3-tuple:(dirpath, dirnames, filenames)
        dirpath is a string, the path to the directory.   当前目录
        dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..'). 当前目录下的子目录
        filenames is a list of the names of the non-directory files in dirpath. 当前目录下的文件
    可迭代对象，for循环遍历目录directory的每一个分支 (语音识别使用的是递归方法,这里采用os.walk方法)
    '''
    for curdir, subdirs, files in os.walk(directory):   # 当前目录h，当前目录下的子目录，当前目录下的文件
        # 遍历到的文件file进行筛选,获取 .jpg或png格式的文件(有其他格式的话继续 or 语句连接)
        for jpeg in (file for file in files if file.endswith('.jpg') or file.endswith('.png')):
            path_image = os.path.join(curdir, jpeg)           # 获取jpg格式文件的绝对路径 ../../chairs/chair.jpg
            
            label = path_image.split(os.path.sep)[-2]         # 获取标签label ../../chairs/chair.jpg中的chairs
            if label not in objects:
                objects[label] = []
            objects[label].append(path_image)

    return objects


train_objects = search_objects('../ML/data/objects/training')
#print(train_objects)

train_x, train_y = [], []
for label, filenames in train_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)        # 灰度图
        # 图片缩放，统一尺寸  短的设置为200像素，宽的成比例调整
        h, w = gray.shape[:2]                       # 原始gray的高和宽
        f = 200 / min(h,w)                          # 缩放比例, 以短边设置为200像素为基准
        gray = cv.resize(gray, None, fx=f, fy=f)
        # star特征检测
        star = cv.xfeatures2d.StarDetector_create() # star特征检测器
        keypoints = star.detect(gray)               # star特征检测器对灰度图检测，获取灰度图star特征
        # sift特征检测
        sift = cv.xfeatures2d.SIFT_create()
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    train_x.append(descs)                           # descs 输入  图形特征矩阵
    train_y.append(label)                           # label 输出  图形分类

models = {}
for descs, label in zip(train_x, train_y):
    # 构建模型 隐马尔科夫模型
    model = hmm.GaussianHMM(n_components=4,         # 隐藏状态 ？？？？？？？？？
                            covariance_type='diag',
                            n_iter=1000
                            )
    # 训练模型：HMM模型存储
    models[label] = model.fit(descs)                # 分类对应的隐马模型，包含所有该类别的特征信息

'''
test
'''
test_objects = search_objects('../ML/data/objects/testing')
#print(test_objects)

test_x, test_y, test_z = [], [], []                 # test_z存图片
for label, filenames in test_objects.items():
    test_z.append([])                               # 存储对应label的图片
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        test_z[-1].append(image)                    # image加入到test_z中
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)        # 灰度图
        # 图片缩放，统一尺寸  短的设置为200像素，宽的成比例调整
        h, w = gray.shape[:2]                       # 原始gray的高和宽
        f = 200 / min(h,w)                          # 缩放比例, 以短边设置为200像素为基准
        gray = cv.resize(gray, None, fx=f, fy=f)
        # star特征检测
        star = cv.xfeatures2d.StarDetector_create() # star特征检测器
        keypoints = star.detect(gray)               # star特征检测器对灰度图检测，获取灰度图star特征
        # sift特征检测
        sift = cv.xfeatures2d.SIFT_create()
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    test_x.append(descs)                           # descs 输入  图形描述特征矩阵
    test_y.append(label)                           # label 输出  图形分类

pred_test_y = []
for descs in test_x:
    best_scrore, best_label = None, None
    for label, model in models.items():            # 遍历模型字典，分别比对特征信息输入数据的得分
        score = model.score(descs)
        if (best_scrore is None) or (best_scrore < score):
            best_scrore, best_label = score, label
    pred_test_y.append(best_label)
print('test_y:', test_y)
print('pred_test_y:', pred_test_y)

i = 0       # 防止图片显示时图片被后续图片覆盖
for label, pred_label, images in zip(test_y, pred_test_y, test_z):
    for image in images:
        i += 1
#        print(label, '==' if label == pred_label else '!=' pred_label)
        cv.imshow('{} - {} {} {}'.format(i, label, '==' if label == pred_label else '!=', pred_label), image)

cv.waitKey()                                      # 