# Created by Chono-Hina at 2026/09/24 14:44
# leetgo: 1.4.18
# https://leetcode.cn/problems/burst-balloons/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # 区间 DP：枚举"最后一个戳的气球 k"（反向思维，让左右子问题独立）
        # dp[i][j] = 开区间 (i,j) 内全部戳完的最大金币（不含边界 i、j）
        nums = [1] + nums + [1]          # 补两端哨兵 1
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for each_len in range(2, length):        # 区间长度从小到大
            for i in range(0, length - each_len):
                j = i + each_len
                for k in range(i + 1, j):        # k = 最后戳的气球
                    now = dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    dp[i][j] = max(dp[i][j], now)
        return dp[0][length - 1]
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCoins(nums)
    print("\noutput:", serialize(ans, "integer"))
