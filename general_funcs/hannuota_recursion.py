# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:16:08 2018
@author: Administrator

time.process_time():
Process time for profiling: sum of the kernel and user-space CPU time.
"""

import time
def move(n,a,b,c):
    if n == 1:
        print(a, '-->', c)
        return
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    return

move(5,'a','b','c')
print(time.process_time())
    
    