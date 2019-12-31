# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:08:09 2019

@author: klaus
"""

import threading

def main():
    print(threading.active_count(), '1')
    print(threading.current_thread(), '2')
    print(threading.enumerate(), '3')
    


if __name__ == "__main__":
    main()