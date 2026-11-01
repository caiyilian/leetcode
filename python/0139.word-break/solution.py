# Created by Chono-Hina at 2026/09/19 11:45
# leetgo: 1.4.18
# https://leetcode.cn/problems/word-break/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 前缀 DP：dp[i] = s[0:i] 能否拆分；dp[j] 真 + s[j:i]∈字典 → dp[i] 真
        # 反向排除版：默认 True，找不到任何可接前缀（for-else）才标 False
        length = len(s)
        dp = [True] * (length + 1)
        for i in range(1, length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    break
            else:
                dp[i] = False
        return dp[-1]
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "boolean"))
