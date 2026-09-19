# Created by Chono-Hina at 2026/09/19 22:16
# leetgo: 1.4.18
# https://leetcode.cn/problems/unique-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 迭代 DP（从终点回填）：dp[i][j] = dp[i+1][j] + dp[i][j+1]（下方 + 右方）
        dp = [[1] * n for _ in range(m)]      # 全 1：第一行/列（及边界）都是 1
        for i in range(1, m):
            for j in range(1, n):
                dp[m - i - 1][n - j - 1] = dp[m - i][n - j - 1] + dp[m - i - 1][n - j]
        return dp[0][0]
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().uniquePaths(m, n)
    print("\noutput:", serialize(ans, "integer"))
