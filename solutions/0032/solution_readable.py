# -*- coding: utf-8 -*-
"""
第 32 题 最长有效括号 · DP 版（"以 i 结尾"的经典 DP）

与用户栈版（solution.py）5 万组对拍 0 差异。
dp[i] = 以 s[i] 结尾的最长有效括号长度：
  s[i]=='('        → dp[i] = 0
  s[i]==')' 且 s[i-1]=='('           → dp[i] = dp[i-2] + 2（...() 形式）
  s[i]==')' 且 s[i-1]==')' 且左侧是 '(' → dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]（...)) 套娃）
"""
from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':                          # 情况1：...()
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':  # 情况2：...))
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
        return max(dp)