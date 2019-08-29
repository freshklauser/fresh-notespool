# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:17:48 2018
@author: Administrator
"""
'''
#人脸识别：基于OpenCV的局部二值模式直方图（LBPH）模型
'''
import os
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp

'''
级联分类器
'face.xml'文件存储信息为人脸定位信息，传参到cv.CascadeClassifier中，构建人脸级联分类器
ed = cv.CascadeClassifier('../ML/data/haar/eye.xml')        眼睛级联分类器(检测对象为face的image)
nd = cv.CascadeClassifier('../ML/data/haar/noise.xml')      鼻子级联分类器(检测对象为face的image)
face.xml, eye.xml, noise.xml分别存储的是人脸定位信息，眼睛定位信息，鼻子定位信息
'''
fd = cv.CascadeClassifier('../ML/data/haar/face.xml')


'''
search_faces {类别标签label: image访问路径}，字典对象 key-label; value-image_path
    label == train数据集中image所在文件夹的filename
'''
def search_faces(directory):
    directory = os.path.normpath(directory)             # Normalize path, eliminating double slashes, etc."""
    if not os.path.isdir(directory):                    # os.path.isdir(file):判断file是不是文件夹即目录
        raise IOError('The directory' + directory + 'does not exist!')
                                                        # 不是目录，则生成错误
    faces = {}                                        # 定义字典对象，label作为key,文件(图片)完整路径作为value
    '''
    os.walk(): Directory tree generator.yields a 3-tuple:(dirpath, dirnames, filenames)
        dirpath is a string, the path to the directory.   当前目录
        dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..'). 当前目录下的子目录
        filenames is a list of the names of the non-directory files in dirpath. 当前目录下的文件
    可迭代对象，for循环遍历目录directory的每一个分支 (语音识别使用的是递归方法,这里采用os.walk方法)
    '''
    for curdir, subdirs, files in os.walk(directory):   # 当前目录h，当前目录下的子目录，当前目录下的文件
        '''
        对遍历的文件file进行筛选,获取 .jpg或png格式的文件(有其他格式的话继续 or 语句连接)
        '''
        for jpeg in (file for file in files if file.endswith('.jpg') or file.endswith('.png')):
            '''
            join(path, *paths): Join two (or more) paths.
            os.path.sep: 获得当前系统下的路径分隔符
            '''
            # dict键值对： key:label; value:path_image
            path_image = os.path.join(curdir, jpeg)           # 获取jpg/png格式文件的绝对路径 ../../chairs/chair.jpg
            label = path_image.split(os.path.sep)[-2]         # 获取标签label ../../chairs/chair.jpg中的chairs
            # label -->  ['..', 'ML', 'data', 'faces', 'testing', 'Sala', 'image_0089.jpg']
            '''
            判断key(即label)在不在faces的keys中，不在则 初始化为空，然后添加第一条value内容到faces[label]中
            在则直接执行添加value内容到faces[label]中
            一个label对应多个path_image文件： key和value一对多，多个value以list格式构成字典的1个value
            '''
            if label not in faces.keys():
                faces[label] = []
            faces[label].append(path_image)
    return faces

'''
导入训练集，并对训练集的标签进行标签转码（训练集的标签储存在字典对象faces的keys中）
'''
train_faces = search_faces('../ML/data/faces/training') # 返回值：dict. 
codec = sp.LabelEncoder()                               # label编码器
codec.fit_transform(list(train_faces.keys()))           # 构建label编码表，输入参数array-like， list array mat都可以

'''
针对训练集，训练模型
'''
train_x, train_y = [], []
for label, filenames in train_faces.items():
    for filename in filenames:                          # key和value 1对多，针对1个key,遍历其value的list中的所有image文件
        image = cv.imread(filename)                     # 读取文件中的图片
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    # 获取灰度图（人脸特征对于色彩不敏感，一般采用灰度图作为对象处理）
        '''
        使用级联分类器的detecMultiScale方法进行人脸定位
        detectMultiScale(...): detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) -> objects
        '''
        faces = fd.detectMultiScale(gray,               # 灰度图中人脸定位
                                    1.1, 2,             # 精度
                                    minSize=(100,200)   # 人脸的最小尺寸 单位 像素
                                    )
        for l, t, w, h in faces:
            train_x.append(gray[t:t+h, l:l+w])          # 截取人脸图片数组作为输入数据添加到train_x中:图片
            train_y.append(codec.transform([label]))   
            # label为str类型，需转为list或array作为输入(不能直接list(label):label=='Roy', list(label) == ['R','o', 'y'])
            # label标签转码， 添加到train_y中：人名的编码
            # note: (l,t)指左上角坐标,截图切片 t:t+h原因见代码结尾 cv2中的坐标系


# 获得训练集数组：
train_x = np.array(train_x)
train_y = np.array(train_y)
# 构建LBPH模型： cv.face.....
model = cv.face.LBPHFaceRecognizer_create()             # 局部二值模式直方图人脸识别器
# 训练模型
model.train(train_x, train_y)                           # opencv中训练模型不是fit, 是train
'''
模型输入是图片，不是特征描述矩阵(HMM模型中训练模型输入的是HMM保存的描述特征矩阵)
LBPH模型内部嵌入的有降维功能，能过滤噪声，提高图像的精度(采用HMM模型和特征矩阵输入会有很多噪声)
'''
# 测试模型
test_faces = search_faces('../ML/data/faces/testing')
test_x, test_y, test_z = [], [], []                     # test_z 存储图片，便于imshow
for label, filenames in test_faces.items():
    for filename in filenames:
        image = cv.imread(filename)                     # 读取文件中的图片
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # 使用级联分类器的detecMultiScale方法进行人脸定位
        faces = fd.detectMultiScale(gray,               # 灰度图中人脸定位
                                    1.1, 2,             # 标度系数，反映识别精度 扫描的力度和步长(0-10通常)，常用 '1.3, 5'
                                    minSize=(100,200)   # 人脸的最小尺寸 单位 像素
                                    )
        for l, t, w, h in faces:
            test_x.append(gray[t:t+h, l:l+w])           # 截取的人脸图片数组作为输入数据添加到train_x中:图片
            test_y.append(int(codec.transform([label])))    # 标签编码后的label
            # 原图中画圈标出人脸
            a, b = int(w / 2), int(h / 2)               # 确定椭圆圆心，人脸区域的中心位置 (a,b)=(w/2,h/2) 即椭圆的长短轴半径
            cv.ellipse(image,                           # 画布，在image上画椭圆
                       (l+a, t+b),                      # 椭圆圆心
                       (a, b),                          # (横轴半径，纵轴半径)
                       0, 0, 360,                       # rotation_angle, startAngle, endAngle
                       (255,0,255),                     # color 线条颜色
                       2                                # 线宽
                       )
            test_z.append(image)                        # 标记完之后把图片添加到test_z中

test_x = np.array(test_x)
test_y = np.array(test_y)                               # [0 0 0 1 1 1 1 2 2 2]

pred_test_y = []
for face in test_x:
    pred_code = model.predict(face)[0]                  # 编码类别  model.predict()输出有什么内容？？？
#    print(model.predict(face))
    # (0, 26.450995617566445)
    # (1, 17.74929617386343)
    pred_test_y.append(pred_code)

escape = False
while not escape:
    for code, pred_code, image in zip(test_y, pred_test_y, test_z):     # zip()参数是迭代器，list, array都可以
        label = codec.inverse_transform([code])[0]
        pred_label = codec.inverse_transform([pred_code])[0]
        '''
        pred_code为str; 
        codec.inverse_transform([pred_code]) : ['Bob']...
        codec.inverse_transform([pred_code])[0] : Bob     (label解码后加索引[0]的原因)
        '''
        text = '{} {} {}'.format(label, '==' if label == pred_label else '!=', pred_label)
        cv.putText(image, 
                   text,
                   (10, 60),                            # text在图片中的坐标位置
                   cv.FONT_HERSHEY_SIMPLEX,             # 字体
                   2,                                   # 线宽
                   (255,255,255),
                   6                                    # 字体大小
                   )
        cv.imshow('Recongnizing...', image)
        if cv.waitKey(1000) == 27:
            escape = True
            break


'''
cv2坐标系
----------------------
0-------------------->x
|
|
|
|
|
v
y

'''
'''
help(cv.face.LBPHFaceRecognizer_create)
Help on built-in function LBPHFaceRecognizer_create:

LBPHFaceRecognizer_create(...)
    LBPHFaceRecognizer_create([, radius[, neighbors[, grid_x[, grid_y[, threshold]]]]]) -> retval
    .   @param radius The radius used for building the Circular Local Binary Pattern. The greater the
    .   radius, the smoother the image but more spatial information you can get.
    .   @param neighbors The number of sample points to build a Circular Local Binary Pattern from. An
    .   appropriate value is to use `8` sample points. Keep in mind: the more sample points you include,
    .   the higher the computational cost.
    .   @param grid_x The number of cells in the horizontal direction, 8 is a common value used in
    .   publications. The more cells, the finer the grid, the higher the dimensionality of the resulting
    .   feature vector.
    .   @param grid_y The number of cells in the vertical direction, 8 is a common value used in
    .   publications. The more cells, the finer the grid, the higher the dimensionality of the resulting
    .   feature vector.
    .   @param threshold The threshold applied in the prediction. If the distance to the nearest neighbor
    .   is larger than the threshold, this method returns -1.
    .   
    .   ### Notes:
    .   
    .   -   The Circular Local Binary Patterns (used in training and prediction) expect the data given as
    .   grayscale images, use cvtColor to convert between the color spaces.
    .   -   This model supports updating.
    .   
    .   ### Model internal data:
    .   
    .   -   radius see LBPHFaceRecognizer::create.
    .   -   neighbors see LBPHFaceRecognizer::create.
    .   -   grid_x see LLBPHFaceRecognizer::create.
    .   -   grid_y see LBPHFaceRecognizer::create.
    .   -   threshold see LBPHFaceRecognizer::create.
    .   -   histograms Local Binary Patterns Histograms calculated from the given training data (empty if
    .   none was given).
    .   -   labels Labels corresponding to the calculated Local Binary Patterns Histograms.
'''