# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-05 18:13:38
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-10 09:12:43


class Solution:
    """贪心算法"""

    def maxSubArray(self, nums):
        max_val, sums = nums[0], nums[0]
        for v in nums[1:]:
            sums = sums + v if sums > 0 else v
            max_val = max(max_val, sums)
        return max_val


class Solution1:
    """dp算法"""

    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        # dp[k]表示以当前元素结尾的子数组的最大值，则dp[k]应该等于max(num[k],dp[k-1]+num[k])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):          # 从前往后遍历
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 100]
    res = Solution().maxSubArray(nums)
    # print(res)

    from itertools import product
    x = [1, 2, 3]
    y = [4, 5, 6]
    c = product(x, y)
    print(list(c))

    import math
    a = float("-inf")       # 负无穷
    b = float("inf")        # 正无穷
    print(math.isinf(a))    # math.isinf(x)  判断x是否是正无穷或负无穷
    print(math.isinf(b))
