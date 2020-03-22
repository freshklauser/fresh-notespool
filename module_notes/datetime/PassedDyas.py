Python 3.6.8 |Anaconda, Inc.| (default, Feb 21 2019, 18:30:04) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import datetime
>>> # 查询今年一共有多少天
>>> datetime.date(2020,12,31).timetuple()
time.struct_time(tm_year=2020, tm_mon=12, tm_mday=31, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=366, tm_isdst=-1)
>>> datetime.date(2020,12,31).timetuple().tm_yday
366
>>> # 查询年初至现在一共过去了多少天
>>> datetime.datetime.today().timetuple().tm_yday
81
>>> datetime.datetime.today().timetuple()
time.struct_time(tm_year=2020, tm_mon=3, tm_mday=21, tm_hour=10, tm_min=50, tm_sec=11, tm_wday=5, tm_yday=81, tm_isdst=-1)
>>>