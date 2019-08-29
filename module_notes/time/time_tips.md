



1. 测试`time.sleep(...)`

   ```
   In [16]: 
       ...: state = 1	
       ...: n = 0
       ...: time_init = time.perf_counter()
       ...: timeout = 5
       ...: while state:
       ...:     t1 = time.perf_counter()
       ...:     print("t1:", t1)
       ...:     time.sleep(0.5)
       ...:     print("t2-t1:", time.perf_counter() - t1)
       ...:     n += 1
       ...:     print("recycle for {} times".format(n))
       ...:     if time.perf_counter() - time_init >= timeout:
       ...:         print('timeout')
       ...:         state = 0
       ...:
   t1: 930.2166148
   t2-t1: 0.5082791999999472
   recycle for 1 times
   t1: 930.7263554
   t2-t1: 0.5084653000000117
   recycle for 2 times
   t1: 931.2376594
   t2-t1: 0.507271400000036
   recycle for 3 times
   t1: 931.7480633
   t2-t1: 0.49731180000003405
   recycle for 4 times
   t1: 932.2483803
   t2-t1: 0.4982199999999466
   recycle for 5 times
   t1: 932.7492637
   t2-t1: 0.5071530000000166
   recycle for 6 times
   t1: 933.2580761
   t2-t1: 0.5068931999999222
   recycle for 7 times
   t1: 933.7664687
   t2-t1: 0.498816599999941
   recycle for 8 times
   t1: 934.2666378
   t2-t1: 0.4990500000000111
   recycle for 9 times
   t1: 934.7683923
   t2-t1: 0.49792539999998553
   recycle for 10 times
   timeout
   ```

   