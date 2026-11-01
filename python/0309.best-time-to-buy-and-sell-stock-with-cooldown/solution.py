# Created by Chono-Hina at 2026/09/21 21:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 四状态 DP：0 持有 / 1 保持卖出(非冷冻) / 2 当天卖出 / 3 冷冻
        # 买入只能从"保持卖出或冷冻"来；卖出从持有来；冷冻只能由"当天卖出"产生
        length = len(prices)
        dp = [[0, 0, 0, 0] for _ in range(length + 1)]
        dp[0][0] = -prices[0]
        for i in range(1, length):
            # 持有
            dp[i][0] = max(
                dp[i - 1][0],                 # 前一天持有，保持持有
                dp[i - 1][1] - prices[i],     # 前一天保持卖出，现在买入
                dp[i - 1][3] - prices[i]      # 前一天冷冻，现在可以买入
            )
            # 保持卖出（不是冷冻期）
            dp[i][1] = max(
                dp[i - 1][1],                 # 前一天也是保持卖出
                dp[i - 1][3]                  # 前一天是冷冻
            )
            # 卖出
            dp[i][2] = dp[i - 1][0] + prices[i]   # 前一天是持有股票
            # 冷冻
            dp[i][3] = dp[i - 1][2]               # 必须是前一天卖出
        return max(dp[length - 1])
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
