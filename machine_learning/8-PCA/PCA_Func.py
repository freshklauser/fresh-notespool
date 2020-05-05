# -*- coding: utf-8 -*-
# @Author: Klaus
# @Date:   2019-05-26 15:50:23
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-16 14:41:00

import numpy as np
import matplotlib.pyplot as plt

# It's suggested to use matrix instead of array to calculate
'''
ATTENTION: Only datasets according with Gaussian distribution ares suitable for PCA
'''


class pcaFunc(object):
    def __init__(self, dimension):
        self.dimension = dimension
        # self.dataGauss = np.mat('3 2000; 2 3000; 4 5000; 5 8000; 1 2000', dtype=float)

    def GenerateGaussData(self):
        '''
        ---> or:np.random.normal(loc=0.0, scale=1.0, size=None)
                Draw random samples from a normal (Gaussian) distribution.
        [Generate a Gussian distribution data with specified mean and sigma value]
        Arguments:
            mean {[2D mat]} -- [mean value of generated data]
            base_coordinate {[2D mat} -- [mat to rotate the coordinate system]
        ATTENTION:
            matrix * vector = vector_new (coordinate transformation)
            Refer: http://blog.codinglabs.org/articles/pca-tutorial.html
        '''
        np.random.seed(32)
        mean_val = np.mat([[0], [0]])
        base_coordinate = np.mat([[1, 0.6], [0.6, 2]])
        # Normalized gaussian distribution data with mean=0 and std=1
        dataRnd = np.random.randn(2000, 2)
        # Generate specified rotated Gaussin distribution
        self.dataGauss = base_coordinate * np.mat(dataRnd.T) + mean_val
        self.dataGauss = self.dataGauss.T
        print('GenerateGaussData', type(self.dataGauss), self.dataGauss.shape)

    def NormalizeData(self, data):
        '''
        [Normalize data]
        Arguments:
            data {[1D/2D array or like]} -- [row: observation or sample,
                                             col: feature or variable]
        NOTE: data is according with Gaussian distribution, there is no need to normalize.
        '''
        data = np.mat(data)
        # self.mean_val = data.mean(axis=0)
        # self.std_val = data.std(axis=0)
        self.mean_val = np.mat([0, 0])
        self.std_val = np.mat([1, 1])

        self.dataNormed = (data - self.mean_val) / self.std_val
        self.std_val = np.mat(self.std_val)

        print('NormalizeData:', type(self.dataNormed), type(self.mean_val), self.std_val.shape)

    def Get_Covariance(self, x, y=None):
        '''
        [Calaculate the covariance of x or (x and y)]
        Arguments:
            x {[1D/2D array or like]} -- [row: observation or sample,
                                          col: feature or variable]
        Keyword Arguments:
            y {[1D/2D array or like]} -- [same shape and type with x] (default: {None})
        '''
        x, y = np.mat(x), np.mat(y)
        print('----------------', y)
        if y == None:
            self.covarMatrix = np.mat(np.cov(x, rowvar=0))
            # self.covarMatrix = x.T * x
        else:
            self.covarMatrix = np.mat(np.cov(x, y, rowvar=0))
            # self.covarMatrix = x.T * x
        print('Get_Covariance:', self.covarMatrix, sep='\n')

    def Get_Eigen(self):
        '''
        [description]
        Arguments:
            matrix {[1D/2D array or like]} -- [covariance of x or (x and y)]
            topNum {[int]} -- [top values wanted]
        Note:
            1) For 2D array, eigVal is a 1D array
            2) Each eigVal corresponds to one column vector instead of one row
        '''
        self.eigVal, self.eigVect = np.linalg.eig(self.covarMatrix)
        # sort eigenvalues via descending order
        # ascend order default(cant't change)
        eigValInd = np.argsort(self.eigVal)
        # topNum eigValInd
        # -1 means reversed order:　data[:-N:-1] == data[::-1][:N-1]
        self.eigValIndTop = eigValInd[:-(self.dimension + 1):-1]
        # Get the topNum egiVal and eigVect
        self.eigValTop = self.eigVal[self.eigValIndTop]
        self.eigVectTop = self.eigVect[:, self.eigValIndTop]
        print('Get_Eigen:', self.eigVal, self.eigVect, self.eigVectTop, sep='\n')

    def Get_ReductDim_Data(self):
        '''
        [Get dimension_reducted data by eigen vector]
        Arguments:
            data {[1D/2D array or like]} -- [normlized data is better]
            eigVect {[1D/2D array or like]} -- [description]
        '''
        self.dataReduct = self.dataNormed * self.eigVectTop
        print('Get_ReductDim_Data:', self.dataReduct, sep='\n')

    def Restored_Data(self):
        '''
        [Restore data from dimension-reducted data]
        Arguments:
            dataReduct {[1D/2D array or like]} -- [description]
        '''
        self.dataNormedRestore = self.dataReduct * self.eigVectTop.T
        print('Data_Restored_Normed:', type(self.dataNormedRestore), self.dataNormedRestore.shape)    # (2000, 2)
        # For matrix: (m,n)x(n,p)-->(m,p) == matA * matB == np.dot(matrix_a, matrix_b) == matrix_a @ matrix_b
        #             (m,n)x(m,n)/(1,n)-->(m,n) == np.multiply(matA, matB)
        self.dataRestore = np.multiply(self.dataNormedRestore, self.std_val) + self.mean_val
        print(self.dataGauss[:5, :], '--------')
        print(self.dataRestore[:5, :])

    def plot_fig(self, color=None, marker=None):
        # data is 2D array: [x,y]
        x = np.arange(-7, 7)
        k = self.eigVectTop[1, 0] / self.eigVectTop[0, 0]
        plt.figure()
        plt.subplot(121)
        # For matrix, slice's shape for one column is a 2D matrix while plot x should be a 1D seq
        # So slice should be transfered to array, 2D matrix (2000,1) --> 1D array (2000,)
        plt.scatter(np.array(self.dataGauss[:, 0]), np.array(self.dataGauss[:, 1]), color=color[0], marker=marker[0])
        plt.scatter(np.array(self.dataNormed[:, 0]), np.array(self.dataNormed[:, 1]), color=color[0], marker=marker[1])
        plt.plot(x, k * x, c=color[1])
        plt.xlim((-8, 8))
        plt.ylim((-8, 8))
        plt.subplot(122)
        plt.hist(self.dataRestore[:, self.eigValIndTop], 40, color=color)
        plt.show()

    def main_run(self):
        self.GenerateGaussData()
        self.NormalizeData(self.dataGauss)
        self.Get_Covariance(self.dataNormed)
        self.Get_Eigen()
        self.Get_ReductDim_Data()
        self.Restored_Data()
        self.plot_fig(color=['r', 'y'], marker=['+', '^'])


if __name__ == '__main__':
    cl = pcaFunc(dimension=2)
    cl.main_run()


'''
 rowvar : bool, optional
        If `rowvar` is True (default), then each row represents a
        variable, with observations in the columns. Otherwise, the relationship
        is transposed: each column represents a variable, while the rows
        contain observations.
'''
