# -*- coding: utf-8 -*-
# @Author: Klaus
# @Date:   2019-05-26 15:18:59
# @Last Modified by:   Klaus
# @Last Modified time: 2019-05-26 15:19:10

import chainer
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# with reference to "Machine Learning in Action"


def PCA(dataMat, topNfeat=9999999):
    meanVals = np.mean(dataMat, axis=0)  # calculate mean
    meanRemoved = dataMat - meanVals  # minus mean
    covMat = np.cov(meanRemoved, rowvar=0)  # calculate the covariance matrix
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))  # calculate eigenvalues
    # sort eigenvalues
    eigValInd = np.argsort(eigVals)
    eigValInd = eigValInd[: -(topNfeat + 1): -1]
    redEigVects = eigVects[:, eigValInd]
    # dimensionality reduction
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


if __name__ == "__main__":
    train, test = chainer.datasets.get_mnist()
    img = []
    label = []
    for i in range(10000):  # get numbers 3, 6, 8
        if train[i][1] == 3 or train[i][1] == 6 or train[i][1] == 8:
            img.append(train[i][0])
            label.append(train[i][1])
    lowDDataMat, reconMat = PCA(np.array(img), 3)
    # draw
    fig = plt.figure()
    axes = fig.add_subplot(111, projection='3d')
    for i in range(len(label)):
        if label[i] == 3:
            axes.scatter(np.array(lowDDataMat[i, 0]), np.array(
                lowDDataMat[i, 1]), np.array(lowDDataMat[i, 2]), color='red')
        if label[i] == 6:
            axes.scatter(np.array(lowDDataMat[i, 0]), np.array(
                lowDDataMat[i, 1]), np.array(lowDDataMat[i, 2]), color='green')
        if label[i] == 8:
            axes.scatter(np.array(lowDDataMat[i, 0]), np.array(
                lowDDataMat[i, 1]), np.array(lowDDataMat[i, 2]), color='blue')
    plt.title("PCA")
    plt.show()
