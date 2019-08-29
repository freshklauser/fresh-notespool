# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-05-27 15:26:49
# @Last Modified by:   Klaus
# @Last Modified time: 2019-05-27 22:37:17

import numpy as np


def dataCompress(data_in, ratio=1, method=None, val_step=5):
    # data_in: (n,) 1D array; data_out:(r,) 1D array
    # ratio: compress ratio.
    # method in ['isometric', 'average', 'peak_max', 'peak_min']
    if method not in ['isometric', 'average', 'peak_max', 'peak_min']:
        print("'Method' should be in ['isometric', 'average', 'peak_max', 'peak_min']")
        raise Exception('Incorrect Input.')

    size_out = int(data_in.shape[0] / ratio)
    data_out = np.zeros(size_out)

    if method == 'isometric':
        for i in range(size_out):
            # get one point in the middle of every val_step points
            indice = int(((2 * i + 1) * val_step - 1) * 0.5)
            data_out[i] = data_in[indice]

    if method == 'average':
        for i in range(size_out):
            data_out[i] = data_in[int(i * ratio):int((i + 1) * ratio)].mean()

    if method == 'peak_max':
        for i in range(size_out):
            data_out[i] = data_in[int(i * ratio):int((i + 1) * ratio)].max()
        # eliminate bias above x aixs when using max value method
        data_out -= np.min(data_out)

    if method == 'peak_min':
        for i in range(size_out):
            data_out[i] = data_in[int(i * ratio):int((i + 1) * ratio)].min()

    return data_out


if __name__ == '__main__':
    np.random.seed(32)
    dataIn = np.random.permutation(np.arange(1, 101))
    print(dataIn)
    dataOut = dataCompress(dataIn, ratio=10, method='isometric')
    print('isometric', dataOut, sep='\n')
    print(dataIn[12])
    dataOut = dataCompress(dataIn, ratio=10, method='average')
    print('average', dataOut, sep='\n')
    print(dataIn[10:20].mean())
    dataOut = dataCompress(dataIn, ratio=10, method='peak_max')
    print('peak_max', dataOut, sep='\n')
    print(dataIn[10:20].max())
    dataOut = dataCompress(dataIn, ratio=10, method='peak_min')
    print('peak_min', dataOut, sep='\n')
    print(dataIn[10:20].min())
