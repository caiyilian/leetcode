# -*- coding: utf-8 -*-
"""
第 347 题 前 K 个高频元素 · 标准版（堆存 (频次, 数字) 元组）

与用户版（solution.py，堆存频次 + count2num 反查）结果一致（5 万组对拍 0 差异）。
关键差异：堆存 (freq, num) 元组 → 数字跟着频次走，省掉 count2num 反查表和 pop 配对。

技巧：
- Counter 一行计数（替代 hash_dict + count_list 索引）
- 堆存元组，元组按第一元素（频次）比较
- 维护堆大小 k：超过就 heappop（弹出频次最小的）
"""
from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []                                  # (频次, 数字)
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)                # 弹掉频次最小的
        return [num for _, num in heap]