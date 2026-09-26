# Created by Chono-Hina at 2026/09/26 17:34
# leetgo: 1.4.18
# https://leetcode.cn/problems/regular-expression-matching/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 二维 DP：dp[i][j] = s 前 i 个字符 与 p 前 j 个字符 是否匹配
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # 空 s 匹配 "x*" / "x*y*" 这类（* 匹配 0 次）
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    # 普通字符 /. ：最后一位能对上，看前面是否匹配
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # * 匹配 0 次：丢掉 p[j-2]*（s 不动）
                    dp[i][j] = dp[i][j - 2]
                    # * 匹配 ≥1 次：s 前进一步，p 不动
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = (dp[i - 1][j] or dp[i][j])
        return dp[m][n]
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().isMatch(s, p)
    print("\noutput:", serialize(ans, "boolean"))
