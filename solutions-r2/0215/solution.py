"""215. 数组中的第 K 个最大元素（二刷）——最小堆维护前 K 大（O(n log k)/O(k) 标准解）

用户 AC 版（2026-10-31 20:33 提交 757945513，一次通过，53ms/30.5MB）
- 最小堆维护"最大的 k 个数"：堆顶永远是这 k 个里最小的 = 第 K 大
- 新数 > 堆顶 → heappushpop（弹掉最小、加进新数，保持堆大小 k）
- ⚡ 等号不替换：相等元素不比"更大"，堆里已有，无需管（不影响第 K 大值）
- 进阶：快选 O(n) 期望——见 SolutionQuickSelect 参考
"""

import heapq
from typing import List


# ===== 用户 AC 版（最小堆，O(n log k)） =====
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        heap = nums[:k]                # 前 k 个建堆（最小堆）
        heapq.heapify(heap)
        for i in range(k, length):
            if nums[i] > heap[0]:      # 比堆顶（当前第 K 大）大才替换
                heapq.heappushpop(heap, nums[i])
        return heap[0]                 # 堆顶 = 第 K 大


# ===== 快速选择参考（期望 O(n)，进阶） =====
class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第 K 大 = 第 (n-k) 小（0 基）
        target = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while True:
            pivot_idx = self._partition(nums, lo, hi)
            if pivot_idx == target:
                return nums[pivot_idx]
            if pivot_idx < target:
                lo = pivot_idx + 1
            else:
                hi = pivot_idx - 1

    def _partition(self, nums, lo, hi):
        pivot = nums[hi]
        i = lo                      # i 左侧都是 < pivot
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]   # pivot 归位
        return i


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))          # 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(s.findKthLargest([1, 2, 3], 1))                    # 3
    print(s.findKthLargest([7, 7, 7], 2))                    # 7