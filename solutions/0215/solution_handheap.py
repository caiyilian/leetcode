# -*- coding: utf-8 -*-
"""
第 215 题 数组中的第 K 个最大元素 · 手写堆版（用户 749954422，理解堆机制的里程碑）

用户从"卡在 arr.pop() 弹末尾"到完整手写 shift_up / shift_down，证明吃透了堆：
- 上浮 shift_up：插入时用（新元素放末尾，比父小就上冒）
- 下沉 shift_down：替换堆顶时用（和更小的儿子交换，往下沉）
- 维护 k 个最大：n > arr[0] 时直接 arr[0]=n + shift_down（"替换堆顶"，
  等价于"删顶三步"的简化——替换时不用真删，覆盖后下沉即可）

性能说明：Python 手写堆比 heapq（C 实现）慢 3~5 倍，且逐个 insert 建堆是
O(k log k) vs heapify 的 O(k)——速度差异来自语言/建堆方式，非算法问题。
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def shift_up(nums, i):              # 上浮（插入）
            while i > 0:
                parent_index = (i - 1) // 2
                if nums[i] < nums[parent_index]:
                    nums[i], nums[parent_index] = nums[parent_index], nums[i]
                else:
                    break
                i = parent_index

        def shift_down(nums, i, n):         # 下沉（替换堆顶后恢复）
            while True:
                left, right = 2 * i + 1, 2 * i + 2
                smallest = i
                if left < n and nums[left] < nums[smallest]:
                    smallest = left
                if right < n and nums[right] < nums[smallest]:
                    smallest = right
                if smallest == i:           # 已稳定
                    break
                nums[i], nums[smallest] = nums[smallest], nums[i]
                i = smallest

        arr = []
        for i in range(k):                  # 建堆：逐个插入 + 上浮
            arr.append(nums[i])
            shift_up(arr, i)

        for n in nums[k:]:                  # 维护 k 个最大
            if n > arr[0]:
                arr[0] = n                  # 替换堆顶
                shift_down(arr, 0, len(arr))  # 下沉恢复
        return arr[0]                        # 堆顶 = 第 k 大