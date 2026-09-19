# Created by Chono-Hina at 2026/09/19 13:55
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-increasing-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # DP：dp[i] = 以 nums[i] 结尾的 LIS 长度 = max(dp[j]+1) for j<i and nums[j]<nums[i]
        # 依赖前面所有 j → 不能用滚动变量，必须保留整个 dp 数组
        n = len(nums)
        dp = [1] * n
        best = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            best = max(best, dp[i])
        return best
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)
    print("\noutput:", serialize(ans, "integer"))
