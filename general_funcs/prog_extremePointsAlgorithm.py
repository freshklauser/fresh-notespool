# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-05-29 10:08:48
# @Last Modified by:   Klaus
# @Last Modified time: 2019-06-13 22:42:44

# There are some differences with that for Bearing.

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


def GetExtramaPoints2D(dataIn, if_plot=True):
    '''
    dataIn: 2D array(2,n)/(1,n) or like
    For (2,n) data:
        First row stands for x axis value
        Second row stands for y axis value
        Target: Find extrme(max and min) points within these points with (x,y)
    '''
    # Ensure the shape of array
    if len(dataIn.shape) > 2:
        print('Dimension of dataIn is not suitable.')
        raise Exception('Input Error: Please input a 1D or 2D array')
    if len(dataIn.shape) < 2:
        print('len(dataIn.shape) < 2')
        index_data = np.arange(1, dataIn.size + 1)
        dataIn = np.vstack((index_data, dataIn))
    if len(dataIn.shape) == 2 and dataIn.shape[0] == 1:
        index_data = np.arange(1, dataIn.size + 1)
        dataIn = np.vstack((index_data, dataIn))
    # Find the index of peak(or extrema max point): [0] necessary
    index_extmax = signal.argrelextrema(dataIn[1], np.greater)[0]
    # Line above equals to 'signal.argrelmax(dataIn[1])[0]'
    index_extmin = signal.argrelextrema(dataIn[1], np.less)[0]
    # Line above equals to 'signal.argrelmin(dataIn[1])[0]'
    points_extmax = dataIn[:, index_extmax]
    points_extmin = dataIn[:, index_extmin]
    # print(points_extmax.shape, points_extmin)
    if if_plot:
        PlotExtPoints(dataIn, points_extmax, points_extmin)
    return points_extmax, points_extmin


def GetQuantilePoints(dataIn, quantile, cond='greater', axis=None):
    '''
    dataIn: 2D array(2,n) or like
        First row stands for x axis value
        Second row stands for y axis value
    quantile: [0, 100]  quantile percentage
    cond: 'greater' or 'less' > or < threshold
    '''
    threshold = np.percentile(dataIn[1], quantile, axis=axis, interpolation='linear')
    # Get index based on y value condition: [0] is necessary
    if cond in ['greater', 'less']:
        if cond == 'less':
            index_quantile = np.where(dataIn[1] < threshold)[0]
        if cond == 'greater':
            index_quantile = np.where(dataIn[1] >= threshold)[0]
        # print('index_quantile: ', index_quantile)
        dataQuantile = dataIn[:, index_quantile]
    else:
        print("Incorrect argument. 'Cond' should in ['greater', 'less']")
        raise AttributeError
    return dataQuantile


def PlotExtPoints(dataIn, points_extmax, points_extmin):
    '''
    all input: 2D array(2,n)
    For (2,n) data:
        First row stands for x axis value
        Second row stands for y axis value
        Target: plot and annotate extrme(max and min) points within these points
    '''
    plt.figure()
    # plot the original dataset
    plt.plot(dataIn[0], dataIn[1])
    plt.scatter(points_extmax[0], points_extmax[1], s=30,
                edgecolor='purple', facecolor='purple', marker='o')
    plt.scatter(points_extmin[0], points_extmin[1], s=30,
                edgecolor='limegreen', facecolor='limegreen', marker='o')
    # Lable the coordinate values of ext points
    for ind, points in enumerate([points_extmax, points_extmin]):
        if ind == 0:
            xytext = (-10, 8)
        else:
            xytext = (-10, -15)
        for i in range(points.shape[1]):
            plt.annotate(
                '({},{})'.format(points[0, i], points[1, i]),
                xy=(points[0, i], points[1, i]),
                xycoords='data',
                xytext=xytext,
                textcoords='offset points')
    plt.show()


if __name__ == '__main__':
    a = np.arange(26) * 12
    t = np.array([0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -
                  15, -3, 4, 10, 8, 13, 8, 10, 3, 1, 20, 7, 3, 0])
    t = t.reshape((1, -1))
    x = np.vstack([a, t])
    points_extmax, points_extmin = GetExtramaPoints2D(x, if_plot=True)
    dataQuantile = GetQuantilePoints(points_extmax, 60, cond='greater')
    print(points_extmax)
    print(dataQuantile)
