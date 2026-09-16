# -*- coding: utf-8 -*-
"""
第 39 题 组合总和 · 标准 remaining 版（与用户最终版等价，1.06 倍差距）
区别：传"剩余 target"而非"当前和"——基线直接判断 remaining==0，
      n > remaining 即 break（语义更顺，常数略小）。
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def fun(start, remaining, path):
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(candidates)):
                n = candidates[i]
                if n > remaining:
                    break                  # 排序 + 剪枝
                path.append(n)
                fun(i, remaining - n, path)  # 可重复用 i
                path.pop()
        fun(0, target, [])
        return result