# Created by Chono-Hina at 2026/09/19 23:10
# leetgo: 1.4.18
# https://leetcode.cn/problems/minimum-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # 从终点回填 + 一圈 inf 边界（省越界判断）
        # dp[i][j] = min(下方, 右方) + grid[i][j]
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]   # 多一圈 inf
        dp[m][n - 1] = 0    # 终点右方 = 0（终点不需额外 cost）
        dp[m - 1][n] = 0    # 终点下方 = 0
        for i in range(m):
            for j in range(n):
                dp[m - i - 1][n - j - 1] = min(dp[m - i][n - j - 1], dp[m - i - 1][n - j]) + grid[m - i - 1][n - j - 1]
        return dp[0][0]
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))
