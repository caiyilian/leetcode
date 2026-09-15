# Created by Chono-Hina at 2026/09/15 21:40
# leetgo: 1.4.18
# https://leetcode.cn/problems/number-of-islands/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def land2water_single(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return                      # 越界或水 → 停
            grid[i][j] = '0'                # 沉没：先标记再递归（防死循环）
            land2water_single(i+1, j)       # 四方向扩散
            land2water_single(i-1, j)
            land2water_single(i, j+1)
            land2water_single(i, j-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':       # 发现新大陆
                    count += 1
                    land2water_single(i, j) # 淹掉整片相连的 '1'
        return count
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numIslands(grid)
    print("\noutput:", serialize(ans, "integer"))
