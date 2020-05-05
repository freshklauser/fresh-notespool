# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-29 10:58:58
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 15:42:25


class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        res = 0
        bound = 2 ** 31 if x < 0 else 2 ** 31 - 1

        while y != 0:
            res = res * 10 + y % 10     # 依次获取个位数字
            if res > bound:
                return 0
            y //= 10                    # 依次弹出个位数字
        return res if x > 0 else -res


if __name__ == '__main__':
    x = -123
    res = Solution().reverse(x)
    print(res)
