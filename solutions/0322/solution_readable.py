# -*- coding: utf-8 -*-
"""
第 322 题 零钱兑换 · 标准迭代 DP 版（bottom-up）

与用户版（solution.py，记忆化递归）1 万组对拍 0 差异。
转移：dp[i] = min(dp[i-c] + 1) for c in coins（i-c >= 0）
凑不出用 inf 表示，最终 dp[amount]==inf 返回 -1。
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]