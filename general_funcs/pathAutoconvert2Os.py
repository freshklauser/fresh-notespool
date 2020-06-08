# -*- coding: utf-8 -*-
# @Author: F1684324
# @Date:   2019-08-28 13:44:54
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-23 17:26:30
# ------------------------------------------------------------------------------
# Description: 自动windows或linux下的路径path转化为当前系统下的路径
# ------------------------------------------------------------------------------

import os


def convert_path(path):
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


def win_2_linux(path):
    return path.replace(r"\\", '/')


if __name__ == '__main__':
    path1 = r'C:\\Users/Administrator\AppData\\Roaming\\Sublime Text 3/Logs'
    print(path1)
    print(os.path.realpath(path1), 'realpath')
    print(os.path.abspath(path1), 'abspath')


    # # path2 = 'C:/Users/packRecomSystem/utility'
    # print(path1)
    # print(os.path.realpath(path1))
    # print()
    # real_path = os.path.realpath(path1)
    # path1_new = convert_path(path1)
    # # path2_new = convert_path(path2)
    # # print(path1_new, path2_new, sep='\n')
    # # print(os.listdir(path1_new))
    # a = 'stddd'
    # # print(help(a.replace))
    # # print(os.sep)
    # # print(r'hell\op'.replace('\\', 'roll'))
    # print(os.path.realpath(path1_new), '--path1_new--', os.path.abspath(path1_new))
    # print('linux path---:', win_2_linux(real_path))
    # print(os.sep)
    # print(path1_new)
    # print('linux path:', win_2_linux(path1_new))
