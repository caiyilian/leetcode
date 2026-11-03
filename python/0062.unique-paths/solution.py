# Created by Chono-Hina at 2026/09/19 22:16
# leetgo: 1.4.18
# https://leetcode.cn/problems/unique-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 二维 DP：dp[i][j] = dp[i-1][j] + dp[i][j-1]（从上 + 从左来）
        # 1 索引 + 全 1 初始化：第 1 行/第 1 列天然只有一条路，免越界判断
        dp = [[1] * (n + 1) for _ in range(m + 1)]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().uniquePaths(m, n)
    print("\noutput:", serialize(ans, "integer"))
