"""72. 编辑距离（二刷）——二维 DP（用户 AC 版）⭐ 考前重点

用户二刷（2026-11-03 12:36 提交 758353362，AC，44ms/22.5MB）
- dp[i][j] = word1 前 i 个字符 → word2 前 j 个字符的最少操作数
- 边界（这题的灵魂）：dp[i][0]=i（删除 i 次）、dp[0][j]=j（插入 j 次）——是行号列号，不是 1！
- 转移：字符相等 → 直接继承 dp[i-1][j-1]；不等 → min(替换, 插入, 删除)+1
- 卡点复盘：初始化错填成全 1 → 反例一抓一把（horse/ros 算 1 应 3）；边界语义 = "空串那侧的代价"
"""

from typing import List


# ===== 用户 AC 版（二维 DP） =====
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)
        dp = [[1] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(length1 + 1):
            dp[i][0] = i                        # ⚡ 边界1：word1[0:i]→空 = 删除 i 次
        for j in range(length2 + 1):
            dp[0][j] = j                        # ⚡ 边界2：空→word2[0:j] = 插入 j 次
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]     # 相等：不用操作，继承对角
                else:
                    dp[i][j] = min(dp[i - 1][j - 1],  # 替换
                                   dp[i][j - 1],      # 插入（word2 增字符，对齐后一位）
                                   dp[i - 1][j]) + 1  # 删除（word1 删字符）
        return dp[length1][length2]


# ===== 参考：滚动一维版（O(n) 空间，面试加分） =====
class SolutionRoll:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))                 # 第一行 0..n
        for i in range(1, m + 1):
            prev = dp[0]                        # dp[i-1][j-1] 对角值
            dp[0] = i
            for j in range(1, n + 1):
                tmp = dp[j]                     # 旧 dp[j] = dp[i-1][j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(prev, dp[j - 1], dp[j]) + 1
                prev = tmp
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse", "ros"))              # 3
    print(s.minDistance("intention", "execution"))    # 5
    print(s.minDistance("", ""))                      # 0
    print(s.minDistance("abc", "abc"))                # 0