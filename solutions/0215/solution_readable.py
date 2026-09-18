# -*- coding: utf-8 -*-
"""
第 215 题 数组中的第 K 个最大元素 · 堆版（heapq 最小堆维护 k 个最大）

与快速选择版（solution.py）同为 Accepted（力扣 749948206）。
直觉：堆里永远存"当前最大的 k 个数"，堆顶是这 k 个里最小的 = 第 k 大。
复杂度 O(n log k)，空间 O(k)。
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]                 # 前 k 个建最小堆
        heapq.heapify(heap)             # O(k)
        for num in nums[k:]:
            if num > heap[0]:           # 比"第 k 大"还大 → 挤进来
                heapq.heapreplace(heap, num)   # 弹堆顶 + 插入 num
        return heap[0]                  # 堆顶 = 第 k 大