# -*- coding: utf-8 -*-
"""
第 78 题 子集 · 标准 start 索引版（与用户递增法结果等价，5 万组对拍一致）
去重机制：for i in range(start, n) + fun(i+1)——下标只往后走，永不回头。
与用户递增法的对照：
  用户递增法 = "值的大小当锁"（path[-1] > n 跳过）
  标准版     = "下标的顺序当锁"（range(start, n) + i+1 免费获得）
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def fun(start, path):
            for i in range(start, len(nums)):   # 这层只能从 start 往后选
                path.append(nums[i])
                result.append(path.copy())      # 每个中间状态都是子集
                fun(i + 1, path)                # 选了 nums[i]，下界推到 i+1
                path.pop()
        fun(0, [])
        return result