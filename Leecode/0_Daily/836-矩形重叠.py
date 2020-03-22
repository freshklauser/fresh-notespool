# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-18 08:57:46
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-18 10:22:55

'''{矩形重叠}
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
给出两个矩形，判断它们是否重叠并返回结果。
示例 1：
    输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
    输出：true
思路：
    分别投影到x轴和y轴，区间可行域
    同时满足：
        max(rec1[0], rec2[0]) < x < min(rec1[2], rec2[2])
        max(rec1[1], rec2[1]) < x < min(rec1[3], rec2[3])
'''

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x_range = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        y_range = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return x_range and y_range

if __name__ == '__main__':
    # rec1 = [0,0,2,2]
    # rec2 = [1,1,3,3]
    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    res = Solution().isRectangleOverlap(rec1, rec2)
    print(res)
