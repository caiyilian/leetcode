# Created by Chono-Hina at 2026/09/19 11:20
# leetgo: 1.4.18
# https://leetcode.cn/problems/perfect-squares/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSquares(self, n: int) -> int:
        # 迭代 DP：dp[i] = min(dp[i-j*j] + 1)（最后一个平方数是 j²）
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            final_count = float("inf")
            j = 1
            while j * j <= i:
                final_count = min(final_count, 1 + dp[i - j * j])
                j += 1
            dp[i] = final_count
        return dp[-1]
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numSquares(n)
    print("\noutput:", serialize(ans, "integer"))
