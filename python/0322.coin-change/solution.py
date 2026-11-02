# Created by Chono-Hina at 2026/09/19 11:11
# leetgo: 1.4.18
# https://leetcode.cn/problems/coin-change/

from typing import *
from leetgo_py import *
from math import isinf

# @lc code=begin

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 完全背包一维 DP：dp[i] = min(1 + dp[i-c])，每枚硬币无限用
        # ⚡ 排序后内层 j>i 即 break：防 dp[i-j] 负下标 + 剪枝（RE 复盘：不判 j>i 会越界）
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in coins:
                if j > i:
                    break
                dp[i] = min(1 + dp[i - j], dp[i])
        return dp[amount] if isinf(dp[amount]) is False else -1
        

# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("\noutput:", serialize(ans, "integer"))
