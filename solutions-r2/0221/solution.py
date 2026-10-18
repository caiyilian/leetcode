"""221. 最大正方形（二刷）——矩阵 DP（dp=1+min 三邻，O(m×n) 最优解）

用户 AC 版（2026-10-18 20:31 提交 755573653，WA→AC）
状态：dp[i][j] = 以 (i,j) 为右下角的最大正方形边长
转移：dp[i][j] = 1 + min(左上, 上, 左)（三邻取短板！）
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1                    # 边界只能边长 1
                else:
                    # ★ 必须取三邻 min：要扩成边长 k，上/左/左上三方向都得能提供 k-1
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                result = max(result, dp[i][j])
        return result ** 2                          # 边长的平方 = 面积


if __name__ == "__main__":
    s = Solution()
    print(s.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                           ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))  # 4
    print(s.maximalSquare([["0", "1"], ["1", "0"]]))   # 1
    print(s.maximalSquare([["0"]]))                    # 0
    print(s.maximalSquare([["1", "1", "0"], ["1", "1", "1"], ["1", "1", "1"]]))  # 4（WA 反例）