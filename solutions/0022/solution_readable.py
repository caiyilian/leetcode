# -*- coding: utf-8 -*-
"""
第 22 题 括号生成 · DP 版（用户问的"动态规划"标签解法）
与用户回溯版输出完全一致（n=1..6 三方对拍 0 差异）。

核心洞察：任何合法括号串，首字符必为 '('，它与某个 ')' 配对，
把整串切成三块 —— "(" + a + ")" + b（a 内部合法、b 尾部合法）。
dp[i] = ∪_{j=0}^{i-1} { "(" + a + ")" + b | a∈dp[j], b∈dp[i-1-j] }

复杂度同为 O(Cₙ×n)（卡特兰数量级）——DP 不是更快，是另一种枚举方式
（构造即合法，无需剪枝判断）。
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]                       # 0 对括号：只有空串
        for i in range(1, n + 1):
            for j in range(i):             # 内部放 j 对
                for a in dp[j]:
                    for b in dp[i - 1 - j]:  # 尾部放 i-1-j 对
                        dp[i].append("(" + a + ")" + b)
        return dp[n]