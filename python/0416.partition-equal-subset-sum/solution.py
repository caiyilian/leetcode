# Created by Chono-Hina at 2026/09/19 20:10
# leetgo: 1.4.18
# https://leetcode.cn/problems/partition-equal-subset-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0/1 背包（二维 DP）：dp[i][j] = 前 i 个物品、容量 j 的最大价值
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        target = nums_sum // 2
        num_arr = target + 1
        num_obj = len(nums)

        dp = [[0] * num_arr for _ in range(num_obj)]   # 列表推导式（勿用 [[0]*n]*m 浅拷贝）
        for j in range(nums[0], num_arr):
            dp[0][j] = nums[0]                          # 第 0 行：只放第一个物品
        for i in range(1, num_obj):
            for j in range(num_arr):
                val_no_put = dp[i - 1][j]               # 不放物品 i
                if j >= nums[i]:                        # 容量 j 放得下物品 i
                    val_put = dp[i - 1][j - nums[i]] + nums[i]
                else:
                    val_put = 0
                dp[i][j] = max(val_no_put, val_put)
        return dp[num_obj - 1][target] == target        # 价值==重量时，dp 值即凑出的重量
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))
