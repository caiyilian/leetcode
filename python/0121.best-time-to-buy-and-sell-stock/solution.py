# Created by Chono-Hina at 2026/09/18 16:21
# leetgo: 1.4.18
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val = prices[0]          # 历史最低买入价
        result = 0                   # 最大利润
        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]  # 更优买入点
            else:
                result = max(prices[i] - min_val, result)
        return result
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
