# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 09:34:27 2018

@author: Administrator
"""

'''
相比较于onePool,功能增加：
1）使用进程池
2）进度条，验证文件拷贝完成，hash算法，拷完一个验证一个hash值
3) 支持文件夹下的文件拷贝 (包括子文件夹及其文件)

Some sysntax of the os module
    a
    Out[92]: 'D:\\1-klaus_AI\\Tools\\RegexTester.exe'
    # os.path.dirname(path): obtain the directory path of file 
    os.path.dirname(a)
    Out[93]: 'D:\\1-klaus_AI\\Tools'
    # os.path.basename(path):obtain the name of the file
    os.path.basename(a)
    Out[94]: 'RegexTester.exe'
'''

import os
import sys
import hashlib
from multiprocessing import Pool
from multiprocessing import Manager

def innercopyFiles(fileName, srcPath, destPath, queue):
    '''
    拷贝一个文件:
        1) 打开源文件，
        2）打开目标文件
        3）源文件中的文件写入目标文件
    '''
    # 拼出源文件的绝对路径和目标文件的绝对路径
    srcFileName= fileName
    destFileName = destPath + '\\' + os.path.basename(fileName)
   
   # 打开源文件，写入到目标文件
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)
#*********************************************************************
    queue.put(fileName)     # 向进程池的队列中放入当前拷贝完成的 ^文件名^
#*********************************************************************
    return True
                
def copyFile(fileName, srcPath, destPath, queue):
    '''
    filename: 完整的路径，包括路径和文件名
    srcPath: input的路径
    destPath: input的路径
    '''
    # 根据fileName更新srcPath和destPath
    length = len(srcPath)
    srcPath_new = os.path.dirname(fileName)
    destPath_new = destPath + srcPath_new[length:]
    
    # 如果源文件夹不存在,则报错，退出操作
    if not os.path.exists(srcPath):
        print('srcPath % is not exists' % srcPath)
        return None
    
    # 如果目标路径不存在，创建目标文件夹(有可能会创建失败)
    if not os.path.exists(destPath_new): 
        # 防御性编程 try: except:
        try:
            os.makedirs(destPath_new)
        except:
            print('makedirs %s error' % destPath_new)
  
    # 真正的开始拷贝文件
    return innercopyFiles(fileName, srcPath_new, destPath_new, queue)


def isDirFile(abs_test,lists1,lists2):
    """
    遍历文件夹（包括子文件夹），提取所有文件夹（包括子文件夹）中文件的目录;
    判断absFilePath是文件还是文件夹，若为文件，将绝对路径保存在list中，若为文件夹
    向下一层搜索，直至所有文件以绝对路径+filename的形式保存在list中
    input: 1) the absolute path of the file or directory;
           2) a list
    output: return a list including the absolute path of all files -> list1
            return a list including name of all files -> list2
    """
    if os.path.isdir(abs_test):
#        print('True')
        filenames = os.listdir(abs_test)
        
        for filename in filenames:
            absPathList = abs_test + '\\' + filename   # '\\'不要忘记了
#            print(absPathList,'\n')
            if os.path.isfile(absPathList):
#                print('{} is a file'.format(absPathList))
#                yield absPathList
                lists1.append(absPathList)
                lists2.append(os.path.basename(absPathList))
            else:
                isDirFile(absPathList,lists1,lists2)    # recursion
    return lists1,lists2


def hashFile(fileName):
    CHUCKSIZE = 4096
    # 注释见hash_test.py 20180711
    h = hashlib.sha256()
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:       # 如果chunk内容为空，break
                break
            h.update(chunk)     # 每读取固定字节内容后更新一次h值
    return h.hexdigest()        # 返回16进制的hash值
    
def poolCopyFiles(srcPath, destPath):
    len_src = len(srcPath)
    
    # 如果源文件夹不存在,则报错，退出操作
    if not os.path.exists(srcPath):
        print('srcPath % is not exists' % srcPath)
        sys.exit()
        
    if not os.path.exists(destPath): 
        # 防御性编程 try: except:
        # 如果目标路径不存在，创建目标文件夹(有可能会创建失败)
        try:
            os.makedirs(destPath)
        except:
            print('makedirs %s error' % destPath)
            print('--------------------------')
            sys.exit()
    else:
        # 如果已经存在，则创建副本，命名+ _1
        destPath = destPath + '_1'
    
    # 记录当前需要拷贝的文件夹下的文件及其个数(方便进度输出)
    lists1, lists2 = [], []
    absAllFileNames,allFileNames = isDirFile(srcPath, lists1, lists2)
    allNum = len(absAllFileNames)
    
    # 记录当前完成拷贝的文件个数
    num_done = 0
    
    # 创建进程池
    pool = Pool()
    queue = Manager().Queue()       # 进程池通信需要的队列
    
    # 拷贝文件夹的操作
    for i in absAllFileNames:       # 包含完整路径和文件名的filename
        pool.apply_async(func=copyFile, args=(i, srcPath, destPath, queue))
    #关闭进程池，不再接受新的进程
    pool.close()
    
    while num_done < allNum:
        # 从队列中取出之前存入的文件(夹)名：在进程池队列取file前需保存所有file的abspath
        fileName = queue.get()  # 如果get不到信息，这里会阻塞   
        
        destFileName = destPath + os.path.dirname(fileName)[len_src:] + '\\' + os.path.basename(fileName)
        print(fileName)
        print(destFileName)
        
        num_done += 1
        rate = num_done / allNum * 100   # 进度值
        
        # hash值的检验
        if hashFile(fileName) == hashFile(destFileName):
            print('%s copied ok' % os.path.basename(fileName))
        else:
            print('%s copied failed' % fileName)
            
        print('Current rate is %.1f%%' % rate + '\n')
        print('Processing...')

    # 等待进程池 , 主进程阻塞等待子进程的退出
    pool.join()
    # Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前
    # 必须先调用close()，让其不再接受新的Process了
    print("Copy Files Done")

def start_main():
    src = input('请输入您要拷贝的文件目录：')
    dest = input('请输入您要拷贝的文件目标目录：')
    poolCopyFiles(src, dest)


if __name__ == '__main__':
    start_main()
    input()





# Manager().lock()和 pool.map()方法处理 
# Manager().queue()和 pool.apply_async()方法处理    
# ????????  为什么没有pool.start();  ??????????????
   
'''
COMMENTS:
1)~~~~~~~~~~~
help(os.path.isdir)
Help on built-in function _isdir in module nt:

_isdir(path, /)
    Return true if the pathname refers to an existing directory.

2)~~~~~~~~~~~~
help(os.path.exists)
Help on function exists in module genericpath:

exists(path)
    Test whether a path exists.  Returns False for broken symbolic links

3)~~~~~~~~~~~~~~
help(multiprocessing.Manager)
Help on method Manager in module multiprocessing.context:

Manager() method of multiprocessing.context.DefaultContext instance
    Returns a manager associated with a running server process
    The managers methods such as `Lock()`, `Condition()` and `Queue()`
    can be used to create shared objects.

4)~~~~~~~~~~~~~~
apply_async(func[, args[, kwds[, callback[, error_callback]]]])

A variant of the apply() method which returns a result object.
If callback is specified then it should be a callable which accepts a single argument. When the result becomes ready callback is applied to it, that is unless the call failed, in which case the error_callback is applied instead.
If error_callback is specified then it should be a callable which accepts a single argument. If the target function fails, then the error_callback is called with the exception instance.
Callbacks should complete immediately since otherwise the thread which handles the results will get blocked.

5)~~~~~~~~~~~~~~
map(func, iterable[, chunksize])
A parallel equivalent of the map() built-in function (it supports only one iterable argument though). It blocks until the result is ready.

This method chops the iterable into a number of chunks which it submits to the process pool as separate tasks. The (approximate) size of these chunks can be specified by setting chunksize to a positive integer.
'''