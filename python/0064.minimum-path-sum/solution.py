# Created by Chono-Hina at 2026/09/19 23:10
# leetgo: 1.4.18
# https://leetcode.cn/problems/minimum-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # 记忆化递归（自顶向下 DP）：fun(i,j) = 到 (i,j) 的最小路径和
        # ⚡ 越界返回 inf 哨兵（不可达路径自然被 min 淘汰）；起点兜底
        m, n = len(grid), len(grid[0])
        mem = {}
        def fun(i, j):
            if (i, j) not in mem:
                if i == 0 and j == 0:
                    return grid[0][0]
                if i < 0 or j < 0:
                    return float('inf')
                mem[(i, j)] = min(fun(i, j - 1), fun(i - 1, j)) + grid[i][j]
            return mem[(i, j)]
        return fun(m - 1, n - 1)
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))
