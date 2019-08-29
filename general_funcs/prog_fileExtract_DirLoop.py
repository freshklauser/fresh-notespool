# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:31:17 2019
@author: Klaus
遍历文件夹（包括子文件夹），提取所有文件夹（包括子文件夹）中文件的目录
"""

import os

test_abs = r'D:\1_Foxconn_Work\1_Intelligent_Spindle\0_Data_org\20190107 WX-01-0001 UB'
print('Length of input: {}'.format(len(test_abs)))
lists1_aim = []
lists2_aim = []

def isDirFile(abs_test,lists1,lists2):
    if os.path.isdir(abs_test):
#        print('True')
        filenames = os.listdir(abs_test)
        
        for filename in filenames:
            absPathList = abs_test + '\\' + filename   # '\\'不要忘记了
            print(absPathList)
            print('-------')
            if os.path.isfile(absPathList):
#                print('{} is a file'.format(absPathList))
#                yield absPathList
                lists1.append(absPathList)
                lists2.append(os.path.basename(absPathList))
            else:
                print('############# {} is a directory'.format(absPathList))
                print(absPathList, len(absPathList))
                print(absPathList[len(test_abs):])
                isDirFile(absPathList,lists1,lists2)
    return lists1,lists2

abspaths,filenames = isDirFile(test_abs,lists1_aim,lists2_aim)
print(len(abspaths))
#print(result)

for i,j in zip(filenames,abspaths):
    print(i,'-->',j)
    print(j[len(test_abs):])
    break