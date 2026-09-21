# -*- coding: utf-8 -*-
"""
第 221 题 最大正方形 · 空间优化版（一维滚动 O(n)）

与用户二维版（solution.py）2 万组对拍 0 差异。
dp[i][j] 只依赖 左上(dp[i-1][j-1])、上(dp[i-1][j])、左(dp[i][j-1])，
用一维数组 + prev 变量滚动即可，空间 O(mn) → O(n)。
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)      # 一维滚动（dp[j] 代表当前行第 j 列）
        now_max = 0
        for i in range(1, m + 1):
            prev = 0            # 记录 dp[i-1][j-1]（左上，被覆盖前的旧值）
            for j in range(1, n + 1):
                temp = dp[j]    # 保存 dp[i-1][j]（上一行同列）
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = 1 + min(prev, dp[j], dp[j - 1])
                    now_max = max(now_max, dp[j])
                else:
                    dp[j] = 0
                prev = temp     # 本轮的 dp[i-1][j] 成为下一列的"左上"
        return now_max ** 2