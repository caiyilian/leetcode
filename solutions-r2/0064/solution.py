"""64. 最小路径和（二刷）——记忆化递归（用户 AC 版）

用户二刷（2026-11-03 11:48 提交 758347498，AC 一次通过，47ms/31.4MB）
- 记忆化递归（自顶向下 DP）：fun(i,j) = 从起点到 (i,j) 的最小和
- 转移：min(从左来, 从上来) + grid[i][j]；起点兜底；越界返回 inf（哨兵思想）
- 与 62 不同路径同骨架：加法换 min，路径计数换路径和
"""

from typing import List


# ===== 用户 AC 版（记忆化递归） =====
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mem = {}

        def fun(i, j):
            if (i, j) not in mem:
                if i == 0 and j == 0:
                    return grid[0][0]            # 起点
                if i < 0 or j < 0:
                    return float('inf')          # ⚡ 越界用 inf 哨兵（该路不可达）
                left_road = fun(i, j - 1)        # 从左来
                up_road = fun(i - 1, j)          # 从上来
                mem[(i, j)] = min(left_road, up_road) + grid[i][j]
            return mem[(i, j)]

        return fun(m - 1, n - 1)


# ===== 参考：迭代二维 DP（自底向上，面试更常见） =====
class SolutionIter:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]     # 第一行只能从左来
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]     # 第一列只能从上来
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


# ===== 参考：滚动一维（O(n) 空间） =====
class SolutionRoll:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]   # 上格(dp[j]旧值) vs 左格(dp[j-1]新值)
        return dp[n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))    # 7
    print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))               # 12
    print(s.minPathSum([[5]]))                                 # 5