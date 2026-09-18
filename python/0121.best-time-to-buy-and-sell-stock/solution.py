# Created by Chono-Hina at 2026/09/18 16:21
# leetgo: 1.4.18
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 一次遍历：维护历史最低价 min_val，每天算"今天卖 - 历史最低买"的利润
        length = len(prices)
        all_min = 0                       # 其实是"最大利润"（用户命名）
        min_val, max_val = prices[0], prices[0]
        for p in prices[1:]:
            if p < min_val:               # 出现更低的买入点
                min_val = p
                max_val = p
            elif p > max_val:             # 出现更高的卖出点
                max_val = p
                all_min = max(all_min, p - min_val)
        return all_min
        

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
