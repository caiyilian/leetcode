"""62. 不同路径（二刷）——二维 DP（用户 AC 版）

用户二刷（2026-11-03 11:32 提交 758344518，AC 一次通过，4ms/19.1MB）
- dp[i][j] = 从起点到格子 (i,j) 的路径数；只能向右/向下 → 每个格子 = 左 + 上
- ⚡ 技巧：1 索引 + 全 1 初始化——第 1 行/第 1 列天然只有一条路（dp[1][*]=dp[*][1]=1），免边界判断
- 从 (2,2) 开始填即可；答案 dp[m][n]
- 数学等价：C(m+n-2, m-1)（总共走 m+n-2 步，选 m-1 步向下）
"""


# ===== 用户 AC 版（1 索引 + 全 1 边界，O(m·n)/O(m·n)） =====
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (n + 1) for _ in range(m + 1)]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]    # 从上 + 从左来
        return dp[m][n]


# ===== 参考：组合数公式（O(min(m,n)) 空间/时间） =====
from math import comb


class SolutionComb:
    def uniquePaths(self, m: int, n: int) -> int:
        # 总步数 m+n-2，其中向下 m-1 步（或向右 n-1 步）
        return comb(m + n - 2, m - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))      # 28
    print(s.uniquePaths(3, 2))      # 3
    print(s.uniquePaths(1, 10))     # 1
    print(s.uniquePaths(100, 100))  # 22750883079422934966181954039568885395604168260154104734000