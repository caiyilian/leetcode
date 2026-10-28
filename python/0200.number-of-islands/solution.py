# Created by Chono-Hina at 2026/09/15 21:40
# leetgo: 1.4.18
# https://leetcode.cn/problems/number-of-islands/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        def fun(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'          # ★ 原地置 0（淹没），防重复计数
            fun(i-1, j)               # 上
            fun(i+1, j)               # 下
            fun(i, j-1)               # 左
            fun(i, j+1)               # 右

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    fun(i, j)         # 淹没整座岛
                    result += 1
        return result
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numIslands(grid)
    print("\noutput:", serialize(ans, "integer"))
