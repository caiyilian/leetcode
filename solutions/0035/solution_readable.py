# -*- coding: utf-8 -*-
"""
第 35 题 搜索插入位置 · ⚡⚡ 标准二分模板（机考之前必看）

与用户"补丁版"（solution.py）结果一致（5 万组对拍 0 差异），但无任何 hack：
- 左闭右开 [left, right)，right = mid / left = mid+1 → 区间必然收敛
- while 结束时 left == right 本身就是答案（可能 0 / 中间 / length）
- 语义：找"第一个 >= target"的位置（= bisect_left）

模板三件套（背住）：
  ① right 取 len(nums)（开区间）
  ② left = mid + 1（防死循环的唯一关键）
  ③ 返回 left
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)              # ① 左闭右开
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:             # ② 找第一个 >= target
                right = mid
            else:
                left = mid + 1                  # ③ 关键：mid+1 保证收敛
        return left                              # left == right == 插入位置