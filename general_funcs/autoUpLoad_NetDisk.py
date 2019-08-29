# -*- coding: utf-8 -*-
# @Author: F1684324
# @Date:   2019-06-25 10:31:20
# @Last Modified by:   F1684324
# @Last Modified time: 2019-06-26 13:31:27

'''auto up-down-load file to-from baidunet

['bypy' package needed: pip install bypy]
['bypy' package verify: bypy info]
Refer: https://blog.csdn.net/CVSvsvsvsvs/article/details/83625972

ToDo:
    1) 目前只实现了bypy跟目录下的文件上传
'''

from bypy import ByPy
import os
import time
import datetime
import threading
import hashlib


class AutoLoad(object):
    """AutoUp or AutoDown files with baidu netdisk"""

    def __init__(self, abspath_input):
        super(AutoLoad, self).__init__()
        # Input params: a abspath of target directory
        self.ABSPATH_INPUT = abspath_input
        # Define private folder to new create in net disk
        self.DIR_NAME_PRIVATE = 'PrivateFolder'
        self.DIR_NAME_WORK = 'WorkFolder'
        # hash params
        self.CHUCKSIZE = 1024

    def datenow2str(self):
        '''Convert date now to str formatter %Y-%m-%d'''
        date_cursor_input = datetime.date.today()
        # print(datetime.datetime.strftime(date_cursor_input, '%Y%m%d'))
        return datetime.datetime.strftime(date_cursor_input, '%Y%m%d')

    def get_bypy(self):
        '''Get a bypy project packaging all operation for files of baidunetdisk'''
        # Create bypy project
        self.bp = ByPy()
        # Create romote private folder for net disk

    def mkdir_remote(self):
        self.bp.mkdir(remotepath=self.DIR_NAME_PRIVATE)
        self.bp.mkdir(remotepath=self.DIR_NAME_WORK)
        # self.bp.mkdir(remotepath=self.DIR_NAME_WORK + '/' + 'mydir')    # subdir

    def file_upload(self):
        pass

    def path_windows2linux(self, windows_path):
        linux_path = ''
        if windows_path != '':
            path_str_list = windows_path.split('\\')
            linux_path = '/'.join(path_str_list)
            # print('linux path:', linux_path)
        else:
            print('input is null')
        return linux_path

    def upload_onetime(self, abspath):
        '''Get all directory subdir and their files under a given root dirpath'''
        print("Root directory is '{}'".format(
            self.path_windows2linux(abspath)))
        # Walk through all direcory from root: dirpath, dirnames, filenames
        local_root_path = self.path_windows2linux(abspath)
        remote_root_name = os.path.split(local_root_path)[-1]
        print('remote_root_name:', remote_root_name)
        # Create root path with a date mark
        remote_date_root_path = self.DIR_NAME_WORK + '/' + '{}'.format(self.datenow2str())
        self.bp.mkdir(remotepath=remote_date_root_path)
        # Create remote root directory
        remote_root_path = remote_date_root_path + '/' + remote_root_name
        print(remote_date_root_path, remote_root_path)
        self.bp.mkdir(remotepath=remote_root_path)
        # Upload files and directories in local_root_path to baiduyun net disk one-time
        self.bp.upload(localpath=local_root_path, remotepath=remote_root_path, ondup='newcopy')

    def get_file_md5(self, file_input):
        '''[get the hash value of a specified file]
        Arguments:
            file {[type]} -- [abs path of a file]
        Returns:
            [type] -- [hexdigest hash value]
        '''
        m = hashlib.md5()
        while True:
            # if not open with byte mode, content of file needs to be encoded first
            # such as : data = file.read(1024).encode('utf-8')
            data = file_input.read(self.CHUCKSIZE)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

    def compare_2files_md5(self, file1_input, file2_input):
        '''Compare hash value of two files'''
        with open(file1_input, 'rb') as f1, open(file2_input, 'rb') as f2:
            file1_md5 = self.get_file_md5(f1)
            file2_md5 = self.get_file_md5(f2)
            if file1_md5 != file2_md5:
                print('Discordance between original file and up-down-load file.')
            else:
                print('Cordance.')


if __name__ == '__main__':
    abspath_input = r'E:\1-Foxconn\Bearing'
    cl = AutoLoad(abspath_input)
    cl.get_bypy()
    cl.mkdir_remote()
    cl.upload_onetime(abspath_input)
    cl.datenow2str()
    s = r'E:\test\folders\md5sanp'          # 'r' can not be ignored
    cl.path_windows2linux(s)
