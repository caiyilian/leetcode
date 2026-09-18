# -*- coding: utf-8 -*-
"""
第 198 题 打家劫舍 · 标准 DP 版（bottom-up 滚动变量）

与用户版（solution.py，记忆化递归"枚举最后偷哪家"）10 万组对拍 0 差异。
标准视角："偷/不偷最后一家"：
  f(i) = max(f(i-1), nums[i] + f(i-2))
滚动优化：只依赖前 2 个 → 两个变量 prev2/prev1。
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0              # prev2=f(i-2), prev1=f(i-1)
        for n in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + n)   # 不偷 vs 偷
        return prev1