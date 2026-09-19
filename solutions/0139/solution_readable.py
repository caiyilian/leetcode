# -*- coding: utf-8 -*-
"""
第 139 题 单词拆分 · 标准 DP 版（bottom-up）

与用户版（solution.py，记忆化递归"第一个单词"）2 万组对拍 0 差异。
标准视角："最后一个单词"（从后拆）：
  dp[i] = 前 i 个字符能否拆分
  dp[i] = any(dp[j] and s[j:i] in wordDict)   for j < i
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wd:
                    dp[i] = True
                    break
        return dp[n]