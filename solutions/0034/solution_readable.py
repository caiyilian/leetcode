# -*- coding: utf-8 -*-
"""
第 34 题 在排序数组中查找元素的第一个和最后一个位置 · 标准哨兵版（无补丁）

与用户补丁版（solution.py）5 万组对拍 0 差异。
区别：lower_bound 用开区间（right = len(nums)），"找不到 ≥ t" 时
返回哨兵 length → 右边界统一 left - 1，无需 if 补丁。

两问合一：lower_bound(target) 是左边界；lower_bound(target+1)-1 是右边界。
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(t: int) -> int:          # 找第一个 >= t 的位置
            l, r = 0, len(nums)                  # ★ 开区间（35 模板）
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= t:
                    r = mid
                else:
                    l = mid + 1
            return l                             # 找不到时 = length（哨兵）

        lo = lower_bound(target)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        hi = lower_bound(target + 1) - 1         # 哨兵机制：-1 永远成立
        return [lo, hi]