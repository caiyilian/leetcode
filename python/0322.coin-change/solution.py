# Created by Chono-Hina at 2026/09/19 11:11
# leetgo: 1.4.18
# https://leetcode.cn/problems/coin-change/

from typing import *
from leetgo_py import *
from math import isinf

# @lc code=begin

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 迭代 DP：dp[i] = min(1 + dp[i-c]) for c in coins（最后一块硬币是 c）
        min_money = min(coins)              # ★ 用 min，别用 coins[0]（coins 不一定排序）
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            best = float("inf")
            if i >= min_money:
                for c in coins:
                    if i < c:
                        continue
                    best = min(best, 1 + dp[i - c])
            dp[i] = best
        return -1 if isinf(dp[-1]) else dp[-1]
        

# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("\noutput:", serialize(ans, "integer"))
