# Created by Chono-Hina at 2026/09/21 21:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 状态机 DP：dp[i][0]=持有, dp[i][1]=卖出(冷冻), dp[i][2]=休息
        length = len(prices)
        dp = [[0] * 3 for _ in range(length + 1)]
        dp[0][0] = -prices[0]        # ★ 持有列 = 买入成本（不是卖出列！）
        for i in range(1, length + 1):
            # 今天持有 = max(昨天持有, 昨天休息 - 今天价)   ← 买入只能从 rest 来
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i - 1])
            # 今天卖出 = 昨天持有 + 今天价                  ← 卖出只能从 hold 来
            dp[i][1] = dp[i - 1][0] + prices[i - 1]
            # 今天休息 = max(昨天卖出, 昨天休息)            ← 冷冻结束 / 继续空仓
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[length][1], dp[length][2])
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
