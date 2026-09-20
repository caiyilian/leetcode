# -*- coding: utf-8 -*-
"""
第 169 题 多数元素 · 排序法（用户第一种方法）

与摩尔投票版（solution.py）3 万组对拍 0 差异。
核心：多数元素出现 > n/2 次，排序后中位数（index n//2）一定是多数元素。
用户写法用「相距 n//2 两位置相等」判断，等价但标准更简洁为 return nums[n//2]。
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]   # 中位数 = 多数元素