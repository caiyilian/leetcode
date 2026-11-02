# Created by Chono-Hina at 2026/09/19 20:10
# leetgo: 1.4.18
# https://leetcode.cn/problems/partition-equal-subset-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0-1 背包一维滚动 bool 版：能否选出若干数和 = sum/2
        # ⚡ 内层 t 从大到小倒序：防同一个数被重复使用（完全背包才正序）
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for t in range(target, x - 1, -1):
                dp[t] = dp[t] or dp[t - x]
        return dp[target]
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))
