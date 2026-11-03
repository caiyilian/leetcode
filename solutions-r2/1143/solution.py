"""1143. 最长公共子序列（二刷）——双串二维 DP（用户 AC 版）⭐ 考前重点

用户二刷（2026-11-03 17:02 提交 758412263，AC 一次通过，347ms/43.4MB）
- dp[i][j] = text1 前 i 个字符与 text2 前 j 个字符的 LCS 长度
- 转移（与 72 编辑距离同一张表）：
  - 末尾相等 → dp[i-1][j-1] + 1（继承对角）
  - 末尾不等 → max(dp[i-1][j], dp[i][j-1])（删 text1 尾 or 删 text2 尾，取大）
- 边界全 0（空串的 LCS = 0）；答案 dp[m][n]
"""


# ===== 用户 AC 版（二维 DP） =====
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1          # 相等：对角 +1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 不等：上/左取 max
        return dp[m][n]


# ===== 参考：记忆化递归（同递推，自顶向下） =====
from functools import lru_cache


class SolutionMemo:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def f(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return f(i - 1, j - 1) + 1
            return max(f(i - 1, j), f(i, j - 1))
        return f(len(text1) - 1, len(text2) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))    # 3
    print(s.longestCommonSubsequence("abc", "abc"))      # 3
    print(s.longestCommonSubsequence("abc", "def"))      # 0
    print(s.longestCommonSubsequence("", "abc"))         # 0