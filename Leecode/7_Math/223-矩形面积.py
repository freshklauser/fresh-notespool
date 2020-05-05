# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-18 10:44:39
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-18 11:45:56

"""{223. 矩形面积 与 836.矩形重叠 差不多}
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
示例:
    输入: -3, 0, 3, 4, 0, -1, 9, 2
    输出: 45
说明: 假设矩形面积不会超出 int 的范围。
思路：
    重疊：根据矩形重叠问题，可行域可确定x轴与y轴交叉域
    不重叠：area1 + area2
"""


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H) -> int:
        """[summary]
        Arguments:
            A B  -- [矩形1的左下角]
            C D  -- [矩形1的右上角]
            E F  -- [矩形2的左下角]
            G H  -- [矩形2的右上角]
        """

        x_range = min(C, G) - max(A, E)
        y_range = min(D, H) - max(B, F)
        cross_area = 0
        total_area = 0
        print(x_range, y_range)
        if x_range >= 0 and y_range >= 0:
            # print(x_range)
            cross_area = x_range * y_range
            total_area = (D - B) * (C - A) + (H - F) * (G - E) - cross_area
        else:
            total_area = (D - B) * (C - A) + (H - F) * (G - E)
        return total_area


if __name__ == '__main__':
    A, B, C, D, E, F, G, H = 0, 0, 0, 0, -1, -1, 1, 1
    # A, B, C, D, E, F, G, H = 2, -2, 2, 2, 3, 3, 4, 4
    # A, B, C, D, E, F, G, H = -3, 0, 3, 4, 0, -1, 9, 2
    res = Solution().computeArea(A, B, C, D, E, F, G, H)
    print(res)
