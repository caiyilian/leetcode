# Created by Chono-Hina at 2026/09/20 12:06
# leetgo: 1.4.18
# https://leetcode.cn/problems/edit-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 编辑距离：dp[i][j] = word1 前 i 转 word2 前 j 的最少操作
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = j          # 空 → word2：全插入
        for i in range(m + 1):
            dp[i][0] = i          # word1 → 空：全删除
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]          # 相等：不变
                else:
                    insert_count = dp[i][j - 1] + 1       # 插入（从左来）
                    delete_count = dp[i - 1][j] + 1       # 删除（从上文来）
                    replace_count = dp[i - 1][j - 1] + 1  # 替换（从左上）
                    dp[i][j] = min(insert_count, delete_count, replace_count)
        return dp[m][n]
        

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().minDistance(word1, word2)
    print("\noutput:", serialize(ans, "integer"))
