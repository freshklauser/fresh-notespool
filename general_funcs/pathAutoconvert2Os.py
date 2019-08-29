# -*- coding: utf-8 -*-
# @Author: F1684324
# @Date:   2019-08-28 13:44:54
# @Last Modified by:   Klaus
# @Last Modified time: 2019-08-29 22:38:52
# ------------------------------------------------------------------------------
# Description: 自动windows或linux下的路径path转化为当前系统下的路径
# ------------------------------------------------------------------------------

import os


def convert_path(path):
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


if __name__ == '__main__':
    path1 = r'C:\Program Files\Common Files'
    path2 = 'C:/Users/packRecomSystem/utility'
    path1_new = convert_path(path1)
    path2_new = convert_path(path2)
    print(path1_new, path2_new, sep='\n')
    print(os.listdir(path1_new))
