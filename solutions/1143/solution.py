# Created by Chono-Hina at 2026/09/20 11:37
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-common-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS：dp[i][j] = text1 前 i、text2 前 j 的 LCS 长度
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1          # 相等：左上 +1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 不等：上/左取 max
        return dp[m][n]
        

# @lc code=end

if __name__ == "__main__":
    text1: str = deserialize("str", read_line())
    text2: str = deserialize("str", read_line())
    ans = Solution().longestCommonSubsequence(text1, text2)
    print("\noutput:", serialize(ans, "integer"))
