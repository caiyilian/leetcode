# -*- coding: utf-8 -*-
"""
第 416 题 分割等和子集 · 一维滚动数组版（0/1 背包标准写法）

与用户版（solution.py，二维 DP）2 万组对拍 0 差异。
一维优化：空间 O(target)；内层 j 从后往前遍历（避免本轮更新污染旧值）。
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target, num - 1, -1):   # ★ 从后往前
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[target] == target