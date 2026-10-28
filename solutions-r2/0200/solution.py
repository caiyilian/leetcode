"""200. 岛屿数量（二刷）——DFS 洪水填充（O(m×n)/O(m×n) 标准解）

用户 AC 版（2026-10-28 19:08 提交 757465424，一次通过，239ms/21.3MB）
- 遍历网格，遇到 '1' 计数 +1，然后 DFS 把整片相连的 '1' 全部置 '0'（淹没），避免重复计数
- 边界检查：越界或 '0' 直接返回；原地改 grid 省 visited 数组
- 图论分类第一题（洪水填充家族母题）
"""

from typing import List


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


if __name__ == "__main__":
    s = Solution()
    g1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(s.numIslands(g1))           # 1
    g2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(s.numIslands(g2))           # 3
    print(s.numIslands([["1"]]))      # 1
    print(s.numIslands([["0"]]))      # 0