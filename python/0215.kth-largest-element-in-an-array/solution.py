# Created by Chono-Hina at 2026/09/18 11:26
# leetgo: 1.4.18
# https://leetcode.cn/problems/kth-largest-element-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        length = len(nums)
        heap = nums[:k]                # 前 k 个建堆（最小堆）
        heapq.heapify(heap)
        for i in range(k, length):
            if nums[i] > heap[0]:      # 比堆顶（当前第 K 大）大才替换
                heapq.heappushpop(heap, nums[i])
        return heap[0]                 # 堆顶 = 第 K 大
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthLargest(nums, k)
    print("\noutput:", serialize(ans, "integer"))
