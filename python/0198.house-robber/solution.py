# Created by Chono-Hina at 2026/09/18 22:24
# leetgo: 1.4.18
# https://leetcode.cn/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 滚动数组：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # 偷 i → dp[i-2] + nums[i]；不偷 i → dp[i-1]；只依赖前两个 → O(1) 空间
        dp_ip1 = nums[0]         # dp[i-1]
        dp_ip2 = 0               # dp[i-2]（初始为 0，相当于偷第 0 家之前）
        for i in range(1, len(nums)):
            dp_ip1, dp_ip2 = max(dp_ip1, dp_ip2 + nums[i]), dp_ip1
        return dp_ip1
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)
    print("\noutput:", serialize(ans, "integer"))
