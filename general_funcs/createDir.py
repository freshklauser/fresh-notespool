# -*- coding: utf-8 -*-
# @Author: F1684324
# @Date:   2019-08-14 15:27:35
# @Last Modified by:   F1684324
# @Last Modified time: 2019-08-14 15:44:04

import os

def createDir(dirpath=os.getcwd(), dirname=r'cache'):
    ''' 创建单级目录(默认在当前目录下创建) '''
    dirpath = dirpath
    dir_abspath = os.path.join(dirpath, dirname)        # 路径连接
    try:
        if not os.path.exists(dir_abspath):
            os.mkdir(dir_abspath)
            print('%s 文件夹创建成功' % dirname)
        else:
            print('%s 文件夹已经存在' % dirname)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    createDir()