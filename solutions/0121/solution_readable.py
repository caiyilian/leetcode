# -*- coding: utf-8 -*-
"""
第 121 题 买卖股票的最佳时机 · 标准版（DP 滚动变量，最简洁）

与用户版（solution.py）结果一致（5 万组对拍 0 差异）。
状态转移：dp[i] = max(dp[i-1], prices[i] - 历史最低价)
滚动优化：dp[i] 只依赖 dp[i-1] 和一个 min → 两个变量足够。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')     # 历史最低买入价
        max_profit = 0               # 最大利润
        for p in prices:
            min_price = min(min_price, p)          # 更新历史最低
            max_profit = max(max_profit, p - min_price)  # 今天卖的最大利润
        return max_profit