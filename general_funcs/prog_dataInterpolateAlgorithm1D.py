# -*- coding: utf-8 -*-
# @Author: Klaus
# @Date:   2019-05-27 22:24:51
# @Last Modified by:   Klaus
# @Last Modified time: 2019-05-28 00:38:32

'''
# "nearest","zero"为阶梯插值
# "slinear" 线性插值
# "quadratic","cubic" 为2阶、3阶B样条曲线插值
# interpolate.lagrange(x,y): 拉格朗日插值
    x = [1,2,4]
    y = [2,3,8]
    f = lagrange(x,y)
    ===》 f(3) = 6
'''

import numpy as np
from numpy import pi, sin, cos
from scipy import interpolate
import matplotlib.pyplot as plt


def DataInterpolate1D(x, y, x_interp, kind, if_plot=False):
    '''
    x, y: initial data coordinates

    '''
    if kind not in ['nearest', 'zero', 'slinear', 'quadratic', 'cubic']:
        print(
            "kind should be in ['nearest','zero','slinear','quadratic','cubic']")
        raise Exception('Incorrect input.')
    # Build the interpolate function
    func = interpolate.interp1d(x, y, kind=kind)
    # Calaculate the interpolated y value for input x_into
    y_interp = func(x_interp)
    if if_plot:
        plt.plot(x, y, 'ro', label='Origial data before interpolated')
        plt.plot(x_interp, y_interp, 'y',
                 linestyle='-.', label='{}'.format(kind))
        plt.legend()
        # plt.show() should be added in the main running codes
    return y_interp


def lagrangeInterp(x, y, x_interp):
    func = interpolate.lagrange(x, y)
    y_interp = func(x_interp)
    return y_interp


if __name__ == '__main__':
    x = np.linspace(0, 10, 21)
    y = sin(2 * x) + cos(0.5 * pi * 50 * x)
    x_interp = np.linspace(0, 10, 201)
    kinds = ['nearest', 'zero', 'slinear', 'quadratic', 'cubic']
    k = 1
    fig, axes = plt.subplots(3, 2)
    for i in np.arange(3):
        for j in np.arange(2):
            y_interp = DataInterpolate1D(x, y, x_interp, kind=kinds[k - 1], if_plot=False)
            axes[i, j].plot(x, y, 'ro')
            axes[i, j].plot(x_interp, y_interp, 'g', linestyle='-', label='{}'.format(kinds[k - 1]))
            axes[i, j].legend(loc='lower left')
            k += 1
            if k > len(kinds):
                y_interp = lagrangeInterp(x, y, x_interp)
                axes[i, j + 1].plot(x, y, 'ro')
                axes[i, j + 1].plot(x_interp, y_interp, 'g', linestyle='-', label='lagrange')
                axes[i, j + 1].legend(loc='upper center')
                break
        else:
            continue
        break
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.2, hspace=0.2)
    plt.show()
